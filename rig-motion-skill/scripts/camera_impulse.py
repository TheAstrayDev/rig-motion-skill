"""Deterministic local camera offsets. Does not open Blender or judge a shot."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
import math
from pathlib import Path
import random
import sys


class InputError(ValueError):
    pass


def number(value, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise InputError(f'{label}: expected a finite number')
    result = float(value)
    if not math.isfinite(result):
        raise InputError(f'{label}: expected a finite number')
    return result


def integer(value, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise InputError(f'{label}: expected an integer')
    return value


def vector(value, label: str) -> tuple[float, float, float]:
    if not isinstance(value, list) or len(value) != 3:
        raise InputError(f'{label}: expected [x, y, z]')
    return tuple(number(v, label) for v in value)


@dataclass(frozen=True)
class Event:
    time: float
    duration: float
    translation: tuple[float, float, float]
    rotation: tuple[float, float, float]
    frequencies: tuple[float, ...]
    decay: float
    phases: tuple[tuple[float, ...], ...]


def parse_spec(spec: dict):
    if not isinstance(spec, dict) or spec.get('schema') != 'rig-motion.camera-impulse.v1':
        raise InputError('schema: expected rig-motion.camera-impulse.v1')
    fps = number(spec.get('fps'), 'fps')
    height = number(spec.get('height'), 'height')
    first = integer(spec.get('frame_start'), 'frame_start')
    last = integer(spec.get('frame_end'), 'frame_end')
    if fps <= 0 or height <= 0:
        raise InputError('fps and height must be positive')
    if last <= first or last - first > 200_000:
        raise InputError('frame range must contain 2..200001 samples')
    length = (last - first) / fps
    raw_events = spec.get('events')
    if not isinstance(raw_events, list) or not raw_events:
        raise InputError('events: expected a nonempty array')
    events = []
    for i, raw in enumerate(raw_events):
        if not isinstance(raw, dict):
            raise InputError(f'events[{i}]: expected an object')
        time = number(raw.get('time'), 'event.time')
        duration = number(raw.get('duration'), 'event.duration')
        decay = number(raw.get('decay', 6.0), 'event.decay')
        seed = integer(raw.get('seed', i), 'event.seed')
        if time < 0 or duration <= 0 or time + duration > length + 1e-10:
            raise InputError(f'events[{i}]: full envelope must fit the clip')
        if not 0 <= decay <= 100:
            raise InputError('decay must be in [0, 100]')
        translation = vector(raw.get('translation_h'), 'event.translation_h')
        rotation = vector(raw.get('rotation_deg'), 'event.rotation_deg')
        raw_freq = raw.get('frequencies_hz', [3.0, 6.0, 9.0])
        if not isinstance(raw_freq, list) or not 1 <= len(raw_freq) <= 8:
            raise InputError('frequencies_hz: expected 1..8 frequencies')
        frequencies = tuple(number(f, 'frequency') for f in raw_freq)
        if any(f <= 0 or f >= fps / 2 for f in frequencies):
            raise InputError('frequencies must be positive and below frame-sampling Nyquist')
        rng = random.Random(seed)
        phases = tuple(tuple(rng.uniform(-math.pi, math.pi) for _ in frequencies) for _ in range(6))
        events.append(Event(time, duration, translation, rotation, frequencies, decay, phases))
    return fps, height, first, last, events


def envelope(u: float, decay: float) -> float:
    """Finite, normalized pulse with zero value and derivative at both ends."""
    if u <= 0 or u >= 1:
        return 0.0
    peak = math.atan2(2 * math.pi, decay) / math.pi
    maximum = math.sin(math.pi * peak) ** 2 * math.exp(-decay * peak)
    return math.sin(math.pi * u) ** 2 * math.exp(-decay * u) / maximum


def event_offset(event: Event, time: float, height: float):
    age = time - event.time
    env = envelope(age / event.duration, event.decay)
    if not env:
        return [0.0] * 6
    weights = [0.5 ** i for i in range(len(event.frequencies))]
    denominator = sum(weights)
    amplitudes = [a * height for a in event.translation] + [math.radians(a) for a in event.rotation]
    offsets = []
    for amplitude, phases in zip(amplitudes, event.phases):
        wave = sum(w * math.sin(2 * math.pi * f * age + p)
                   for w, f, p in zip(weights, event.frequencies, phases)) / denominator
        offsets.append(amplitude * env * wave)
    return offsets


def generate(spec: dict) -> dict:
    fps, height, first, last, events = parse_spec(spec)
    samples = []
    peaks = [0.0] * 6
    for frame in range(first, last + 1):
        time = (frame - first) / fps
        values = [0.0] * 6
        for event in events:
            values = [a + b for a, b in zip(values, event_offset(event, time, height))]
        if not all(math.isfinite(v) for v in values):
            raise InputError('amplitudes overflow; reduce height or event amplitudes')
        peaks = [max(a, abs(b)) for a, b in zip(peaks, values)]
        samples.append({'frame': frame, 'time': time, 'location': values[:3],
                        'rotation_euler_rad': values[3:]})
    return {
        'schema': 'rig-motion.camera-offsets.v1',
        'fps': fps, 'frame_start': first, 'frame_end': last,
        'space': 'local-camera-aligned', 'rotation_order': 'XYZ',
        'height': height,
        'peak_abs_location': peaks[:3], 'peak_abs_rotation_rad': peaks[3:],
        'notes': ['Sampled offset data only; Blender rig and visual review are separate.',
                  'Overlapping events add. Reported peaks are sampled, not continuous maxima.',
                  'Envelope modulation and interpolation require final render review.'],
        'samples': samples,
    }


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise InputError(f'duplicate JSON key: {key}')
        result[key] = value
    return result


def invalid_constant(value):
    raise InputError(f'nonstandard JSON number: {value}')


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args(argv)
    try:
        if args.output and args.input.resolve() == args.output.resolve():
            raise InputError('output must not overwrite input')
        spec = json.loads(args.input.read_text(encoding='utf-8-sig'),
                          object_pairs_hook=unique_object, parse_constant=invalid_constant)
        result = generate(spec)
        output = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
        if args.output:
            args.output.write_text(output, encoding='utf-8')
            print(f'Wrote {len(result["samples"])} samples to {args.output}')
        else:
            print(output, end='')
        return 0
    except (InputError, OSError, ValueError, OverflowError) as error:
        print(f'Input/output error: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
