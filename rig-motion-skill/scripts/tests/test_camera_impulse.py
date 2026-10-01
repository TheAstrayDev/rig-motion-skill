import copy
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import camera_impulse as camera


def example():
    return {
        'schema': 'rig-motion.camera-impulse.v1', 'fps': 30,
        'frame_start': 11, 'frame_end': 71, 'height': 2,
        'events': [{'time': 0.4, 'duration': 0.6, 'translation_h': [0.01, 0.02, 0],
                    'rotation_deg': [1, 0.5, 0], 'seed': 7, 'decay': 6,
                    'frequencies_hz': [3, 6, 9]}],
    }


class ImpulseTests(unittest.TestCase):
    def test_repeatable_and_seeds_change_result(self):
        spec = example()
        self.assertEqual(camera.generate(spec), camera.generate(spec))
        other = copy.deepcopy(spec)
        other['events'][0]['seed'] = 8
        self.assertNotEqual(camera.generate(spec)['samples'], camera.generate(other)['samples'])

    def test_fps_changes_sampling_not_seconds(self):
        a = example()
        b = copy.deepcopy(a)
        b.update(fps=60, frame_end=131)
        result_a = camera.generate(a)['samples']
        result_b = camera.generate(b)['samples']
        for low, high in zip(result_a, result_b[::2]):
            self.assertEqual(low['time'], high['time'])
            self.assertEqual(low['location'], high['location'])
            self.assertEqual(low['rotation_euler_rad'], high['rotation_euler_rad'])

    def test_zero_outside_events_and_at_endpoints(self):
        spec = example()
        result = camera.generate(spec)['samples']
        for sample in result:
            if sample['time'] <= 0.4 or sample['time'] >= 1.0:
                self.assertEqual(sample['location'], [0, 0, 0])
                self.assertEqual(sample['rotation_euler_rad'], [0, 0, 0])

    def test_single_event_bound_and_units(self):
        result = camera.generate(example())
        self.assertGreater(result['peak_abs_location'][0], 0)
        self.assertLessEqual(result['peak_abs_location'][0], 0.02)
        self.assertLessEqual(result['peak_abs_location'][1], 0.04)
        self.assertLessEqual(result['peak_abs_rotation_rad'][0], math.radians(1))
        self.assertEqual(result['peak_abs_location'][2], 0)

    def test_height_only_scales_translation(self):
        a = example()
        b = copy.deepcopy(a)
        b['height'] = 4
        for x, y in zip(camera.generate(a)['samples'], camera.generate(b)['samples']):
            self.assertEqual([v * 2 for v in x['location']], y['location'])
            self.assertEqual(x['rotation_euler_rad'], y['rotation_euler_rad'])

    def test_overlapping_events_add(self):
        a = example()
        b = copy.deepcopy(a)
        b['events'].append(copy.deepcopy(b['events'][0]))
        for x, y in zip(camera.generate(a)['samples'], camera.generate(b)['samples']):
            self.assertEqual([v * 2 for v in x['location']], y['location'])
            self.assertEqual([v * 2 for v in x['rotation_euler_rad']], y['rotation_euler_rad'])

    def test_envelope_normalization_and_zero_derivative(self):
        for decay in [0, 6, 100]:
            peak = math.atan2(2 * math.pi, decay) / math.pi
            self.assertAlmostEqual(camera.envelope(peak, decay), 1)
            self.assertEqual(camera.envelope(0, decay), 0)
            self.assertEqual(camera.envelope(1, decay), 0)
            step = 1e-8
            self.assertLess(camera.envelope(step, decay) / step, 0.001)

    def test_invalid_inputs_rejected(self):
        cases = [
            ('fps', 0), ('fps', True), ('fps', float('nan')), ('height', -2),
            ('frame_start', 0.5), ('frame_end', 11), ('frame_end', 400_000),
            ('events', []), ('schema', 'other'),
        ]
        for key, value in cases:
            with self.subTest(key=key, value=value):
                spec = example()
                spec[key] = value
                with self.assertRaises(camera.InputError):
                    camera.generate(spec)

    def test_bad_events_rejected(self):
        cases = [
            ('time', -1), ('duration', 0), ('duration', 3), ('decay', -1),
            ('decay', 101), ('seed', True), ('translation_h', [1, 2]),
            ('rotation_deg', [1, float('inf'), 0]), ('frequencies_hz', [15]),
            ('frequencies_hz', [0]), ('frequencies_hz', []),
        ]
        for key, value in cases:
            with self.subTest(key=key, value=value):
                spec = example()
                spec['events'][0][key] = value
                with self.assertRaises(camera.InputError):
                    camera.generate(spec)

    def test_nonfinite_output_rejected(self):
        spec = example()
        spec['height'] = 1e308
        spec['events'][0]['translation_h'] = [1e308, 0, 0]
        with self.assertRaises(camera.InputError):
            camera.generate(spec)

    def test_axes_have_independent_phases(self):
        spec = example()
        spec['events'][0]['translation_h'] = [0.01, 0.01, 0.01]
        sample = camera.generate(spec)['samples'][18]
        self.assertEqual(len(set(sample['location'])), 3)


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, '-X', 'utf8', '-B', str(Path(camera.__file__)), *map(str, args)],
                              capture_output=True, text=True, encoding='utf-8')

    def test_cli_writes_valid_output_and_preserves_input(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / 'input.json'
            output = Path(folder) / 'output.json'
            source.write_text(json.dumps(example()), encoding='utf-8')
            before = source.read_bytes()
            result = self.run_cli(source, '--output', output)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(source.read_bytes(), before)
            self.assertEqual(json.loads(output.read_text(encoding='utf-8'))['schema'], 'rig-motion.camera-offsets.v1')

    def test_cli_rejects_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / 'input.json'
            source.write_text(json.dumps(example()), encoding='utf-8')
            before = source.read_bytes()
            self.assertEqual(self.run_cli(source, '--output', source).returncode, 2)
            self.assertEqual(source.read_bytes(), before)

    def test_cli_rejects_duplicate_keys_and_nonstandard_numbers(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / 'input.json'
            for data in ['{"schema":1,"schema":2}', '{"value": NaN}']:
                source.write_text(data, encoding='utf-8')
                self.assertEqual(self.run_cli(source).returncode, 2)

    def test_cli_invalid_input_does_not_create_output(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / 'input.json'
            output = Path(folder) / 'output.json'
            source.write_text('{bad json}', encoding='utf-8')
            self.assertEqual(self.run_cli(source, '--output', output).returncode, 2)
            self.assertFalse(output.exists())


if __name__ == '__main__':
    unittest.main()
