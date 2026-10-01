import copy
import importlib.util
import json
import math
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / (name + ".py"))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


motion = module("motion_audit")
bedrock = module("bedrock_audit")
ASSETS = ROOT.parent / "assets"


class MotionTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ASSETS / "samples.example.json").read_text(encoding="utf-8"))

    def test_known_good_and_no_mutation(self):
        original = copy.deepcopy(self.data)
        self.assertEqual(motion.audit(self.data)["status"], "pass")
        self.assertEqual(self.data, original)

    def test_opposite_quaternion_signs(self):
        self.assertAlmostEqual(motion.quaternion_angle([1, 0, 0, 0], [-2, 0, 0, 0]), 0)

    def test_rotation_distance(self):
        self.assertAlmostEqual(motion.quaternion_angle([1, 0, 0, 0], [0, 1, 0, 0]), math.pi)

    def test_zero_quaternion_rejected(self):
        self.data["samples"][0]["rotations"]["head"] = [0, 0, 0, 0]
        with self.assertRaises(ValueError):
            motion.audit(self.data)

    def test_drifting_contact(self):
        self.data["samples"][2]["points"]["left_contact"][0] += 0.1
        report = motion.audit(self.data)
        self.assertEqual(report["status"], "fail")
        self.assertTrue(any("contact drift" in s for s in report["issues"]))

    def test_endpoint_mismatch(self):
        self.data["samples"][-1]["points"]["torso"][0] += 0.1
        self.assertTrue(any("loop position" in s for s in motion.audit(self.data)["issues"]))

    def test_velocity_seam_with_matching_pose(self):
        self.data["samples"][1]["points"]["torso"][0] = 0.2
        self.assertTrue(any("velocity" in s for s in motion.audit(self.data)["issues"]))

    def test_missing_contact_sample_rejected(self):
        del self.data["samples"][2]["points"]["left_contact"]
        with self.assertRaises(ValueError):
            motion.audit(self.data)

    def test_contact_window_boundaries_review(self):
        self.data["contacts"][0].update(start=0.1, end=0.9)
        self.assertEqual(motion.audit(self.data)["status"], "review")

    def test_sparse_contact_review(self):
        self.data["contacts"][0].update(start=0.4, end=0.6)
        self.assertEqual(motion.audit(self.data)["status"], "review")

    def test_nonfinite_rejected(self):
        self.data["samples"][0]["points"]["torso"][0] = float("nan")
        with self.assertRaises(ValueError):
            motion.audit(self.data)

    def test_unordered_time_rejected(self):
        self.data["samples"][1]["t"] = 0
        with self.assertRaises(ValueError):
            motion.audit(self.data)

    def test_local_space_rejected(self):
        self.data["space"] = "local"
        with self.assertRaises(ValueError):
            motion.audit(self.data)

    def test_root_local_loop_supported(self):
        self.data["space"] = "root-local"
        self.data["contacts"] = []
        self.assertEqual(motion.audit(self.data)["status"], "pass")

    def test_root_local_contact_rejected(self):
        self.data["space"] = "root-local"
        with self.assertRaises(ValueError):
            motion.audit(self.data)

    def test_height_normalization(self):
        report0 = motion.audit(self.data)
        self.data["height"] *= 10
        for sample in self.data["samples"]:
            for point in sample["points"].values():
                point[:] = [v * 10 for v in point]
        report1 = motion.audit(self.data)
        self.assertAlmostEqual(report0["contacts"][0]["max_drift_H"], report1["contacts"][0]["max_drift_H"])
        self.assertAlmostEqual(report0["loop"]["point:torso"]["seam_linear_velocity_error_H_per_s"],
                               report1["loop"]["point:torso"]["seam_linear_velocity_error_H_per_s"])

    def test_no_labels_is_not_pass(self):
        self.data["loop"] = False
        self.data["contacts"] = []
        self.assertEqual(motion.audit(self.data)["status"], "review")

    def test_two_samples_velocity_review(self):
        self.data["samples"] = [self.data["samples"][0], self.data["samples"][-1]]
        self.assertEqual(motion.audit(self.data)["status"], "review")


class BedrockTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ASSETS / "probe.animation.json").read_text(encoding="utf-8"))
        self.geo = json.loads((ASSETS / "probe.geo.json").read_text(encoding="utf-8"))
        self.clip = self.data["animations"]["animation.rigmotion.probe"]

    def test_probe_passes_without_mutation(self):
        before = copy.deepcopy((self.data, self.geo))
        self.assertEqual(bedrock.audit(self.data, self.geo)["status"], "pass")
        self.assertEqual((self.data, self.geo), before)

    def test_no_geometry_review(self):
        self.assertEqual(bedrock.audit(self.data)["status"], "review")

    def test_unknown_bone_fails(self):
        self.clip["bones"]["missing"] = {"rotation": [0, 0, 0]}
        self.assertEqual(bedrock.audit(self.data, self.geo)["status"], "fail")

    def test_key_outside_duration(self):
        self.clip["bones"]["probe"]["position"]["2.0"] = [0, 0, 0]
        self.assertEqual(bedrock.audit(self.data, self.geo)["status"], "fail")

    def test_duplicate_numeric_times(self):
        self.clip["bones"]["probe"]["position"]["0"] = [0, 0, 0]
        self.assertEqual(bedrock.audit(self.data, self.geo)["status"], "fail")

    def test_position_loop_mismatch(self):
        self.clip["bones"]["probe"]["position"]["1.0"] = [1, 0, 0]
        self.assertEqual(bedrock.audit(self.data, self.geo)["status"], "fail")

    def test_rotations_360_review_not_false_failure(self):
        self.clip["bones"]["probe"]["rotation"]["1.0"] = [0, 0, 360]
        self.assertEqual(bedrock.audit(self.data, self.geo)["status"], "review")

    def test_pre_post_boundary_discontinuity(self):
        self.clip["bones"]["probe"]["position"]["1.0"] = {"pre": [0, 0, 0], "post": [1, 0, 0]}
        self.assertEqual(bedrock.audit(self.data, self.geo)["status"], "fail")

    def test_expression_is_unverified(self):
        self.clip["bones"]["probe"]["rotation"] = ["math.sin(query.anim_time * 360)", 0, 0]
        self.assertEqual(bedrock.audit(self.data, self.geo)["status"], "review")

    def test_pre_post_expression_is_unverified(self):
        self.clip["bones"]["probe"]["rotation"]["0.0"] = {"pre": [0, 0, 0], "post": ["query.anim_time", 0, 0]}
        self.assertEqual(bedrock.audit(self.data, self.geo)["status"], "review")

    def test_unsupported_easing_is_unverified(self):
        self.clip["bones"]["probe"]["position"]["0.0"] = {"post": [0, 0, 0], "lerp_mode": "bezier"}
        self.assertEqual(bedrock.audit(self.data, self.geo)["status"], "review")

    def test_missing_endpoints_review(self):
        del self.clip["bones"]["probe"]["position"]["1.0"]
        self.assertEqual(bedrock.audit(self.data, self.geo)["status"], "review")

    def test_cyclic_hierarchy_rejected(self):
        self.geo["minecraft:geometry"][0]["bones"][0]["parent"] = "probe"
        with self.assertRaises(ValueError):
            bedrock.audit(self.data, self.geo)

    def test_geometry_selection(self):
        other = copy.deepcopy(self.geo["minecraft:geometry"][0])
        other["description"]["identifier"] = "geometry.other"
        self.geo["minecraft:geometry"].append(other)
        with self.assertRaises(ValueError):
            bedrock.audit(self.data, self.geo)
        self.assertEqual(bedrock.audit(self.data, self.geo, "geometry.rigmotion.probe")["status"], "pass")

    def test_bbmodel_rejected(self):
        with self.assertRaises(ValueError):
            bedrock.audit({"meta": {"format_version": "5.0"}, "animations": []})

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text('{"animations":{},"animations":{}}', encoding="utf-8")
            with self.assertRaises(ValueError):
                bedrock.load(path)


class CliTests(unittest.TestCase):
    def test_fail_exit_code_and_report_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path, output = Path(directory) / "samples.json", Path(directory) / "report.json"
            data = json.loads((ASSETS / "samples.example.json").read_text(encoding="utf-8"))
            data["samples"][2]["points"]["left_contact"][0] += 0.1
            path.write_text(json.dumps(data), encoding="utf-8")
            result = subprocess.run([sys.executable, str(ROOT / "motion_audit.py"), str(path), "--output", str(output)], capture_output=True)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8"))["status"], "fail")

    def test_review_exit_code(self):
        result = subprocess.run([sys.executable, str(ROOT / "bedrock_audit.py"), str(ASSETS / "probe.animation.json")], capture_output=True)
        self.assertEqual(result.returncode, 3)
        self.assertEqual(json.loads(result.stdout)["status"], "review")

    def test_examples_cli_and_input_preservation(self):
        inputs = [ASSETS / "samples.example.json", ASSETS / "probe.animation.json", ASSETS / "probe.geo.json"]
        before = [p.read_bytes() for p in inputs]
        commands = [[sys.executable, str(ROOT / "motion_audit.py"), str(inputs[0])],
                    [sys.executable, str(ROOT / "bedrock_audit.py"), str(inputs[1]), "--geometry", str(inputs[2])]]
        for command in commands:
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["status"], "pass")
        self.assertEqual([p.read_bytes() for p in inputs], before)

    def test_input_overwrite_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "samples.json"
            path.write_bytes((ASSETS / "samples.example.json").read_bytes())
            before = path.read_bytes()
            result = subprocess.run([sys.executable, str(ROOT / "motion_audit.py"), str(path), "--output", str(path)], capture_output=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
