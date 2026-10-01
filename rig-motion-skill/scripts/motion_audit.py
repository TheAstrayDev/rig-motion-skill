#!/usr/bin/env python3
"""Read-only audit of explicitly labelled motion samples; no DCC dependencies."""
import argparse
import json
import math
import sys
from pathlib import Path


def number(value, label, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{label}: expected finite number")
    if positive and value <= 0:
        raise ValueError(f"{label}: expected positive number")
    return float(value)


def vector(value, size, label):
    if not isinstance(value, list) or len(value) != size:
        raise ValueError(f"{label}: expected {size}-component array")
    return [number(v, label) for v in value]


def norm(v):
    return math.sqrt(sum(x * x for x in v))


def difference(a, b):
    return [x - y for x, y in zip(a, b)]


def quaternion_angle(a, b):
    """Shortest orientation distance, radians; both wxyz and sign-equivalence."""
    na, nb = norm(a), norm(b)
    if na < 1e-12 or nb < 1e-12:
        raise ValueError("zero-length quaternion")
    dot = abs(sum(x * y for x, y in zip(a, b)) / (na * nb))
    return 2 * math.acos(min(1.0, max(0.0, dot)))


def audit(data, position_limit=0.002, contact_limit=0.005,
          angle_limit=0.5, velocity_limit=0.05):
    if not isinstance(data, dict) or data.get("schema") != "rig-motion.samples.v1":
        raise ValueError("expected schema rig-motion.samples.v1")
    if data.get("space") not in ("world", "support-local", "root-local"):
        raise ValueError("space must be world, support-local or root-local")
    height = number(data.get("height"), "height", positive=True)
    if not isinstance(data.get("loop"), bool):
        raise ValueError("loop must be boolean")
    for label, threshold in (("position_limit", position_limit), ("contact_limit", contact_limit),
                             ("angle_limit", angle_limit), ("velocity_limit", velocity_limit)):
        number(threshold, label, positive=True)
    samples = data.get("samples")
    if not isinstance(samples, list) or len(samples) < 2:
        raise ValueError("at least two samples required")
    previous = -math.inf
    for i, sample in enumerate(samples):
        if not isinstance(sample, dict):
            raise ValueError(f"sample {i}: expected object")
        t = number(sample.get("t"), f"sample {i}.t")
        if t < 0 or t <= previous:
            raise ValueError("sample times must be nonnegative and strictly increasing")
        previous = t
        for field, size in (("points", 3), ("rotations", 4)):
            values = sample.get(field, {})
            if not isinstance(values, dict):
                raise ValueError(f"sample {i}.{field}: expected object")
            for name, value in values.items():
                vec = vector(value, size, f"{field}.{name}")
                if field == "rotations" and norm(vec) < 1e-12:
                    raise ValueError(f"rotations.{name}: zero-length quaternion")

    result = {"scope": "sampled endpoint, linear velocity and labelled contact checks only",
              "space": data["space"], "height": height, "sample_count": len(samples),
              "loop": {}, "contacts": [], "issues": [], "unverified": []}

    def require(sample, field, name):
        if name not in sample.get(field, {}):
            raise ValueError(f"missing {field}.{name} at t={sample['t']}")
        return sample[field][name]

    def labels(field):
        value = data.get(field, [])
        if not isinstance(value, list) or any(not isinstance(n, str) or not n for n in value):
            raise ValueError(f"{field}: expected array of nonempty names")
        if len(value) != len(set(value)):
            raise ValueError(f"{field}: duplicate names")
        return value

    point_names, rotation_names = labels("loop_points"), labels("loop_rotations")
    if data["loop"]:
        if not point_names and not rotation_names:
            raise ValueError("loop=true requires explicit loop_points or loop_rotations")
        for name in point_names:
            first = require(samples[0], "points", name)
            last = require(samples[-1], "points", name)
            displacement = norm(difference(last, first)) / height
            row = {"endpoint_error_H": displacement}
            if displacement > position_limit:
                result["issues"].append(f"loop position mismatch: {name}")
            if len(samples) >= 3:
                second = require(samples[1], "points", name)
                penultimate = require(samples[-2], "points", name)
                dt0 = samples[1]["t"] - samples[0]["t"]
                dt1 = samples[-1]["t"] - samples[-2]["t"]
                v0 = [x / dt0 for x in difference(second, first)]
                v1 = [x / dt1 for x in difference(last, penultimate)]
                mismatch = norm(difference(v1, v0)) / height
                row["seam_linear_velocity_error_H_per_s"] = mismatch
                if mismatch > velocity_limit:
                    result["issues"].append(f"sampled seam velocity mismatch: {name}")
            else:
                result["unverified"].append(f"seam velocity needs at least three samples: {name}")
            result["loop"]["point:" + name] = row
        for name in rotation_names:
            angle = math.degrees(quaternion_angle(require(samples[0], "rotations", name),
                                                  require(samples[-1], "rotations", name)))
            result["loop"]["rotation:" + name] = {"endpoint_error_degrees": angle}
            if angle > angle_limit:
                result["issues"].append(f"loop orientation mismatch: {name}")

    contacts = data.get("contacts", [])
    if not isinstance(contacts, list):
        raise ValueError("contacts: expected array")
    if contacts and data["space"] == "root-local":
        raise ValueError("contact checks require world or support-local samples; root-local may hide sliding")
    for contact in contacts:
        if not isinstance(contact, dict) or not isinstance(contact.get("point"), str) or not contact["point"]:
            raise ValueError("contact requires point name")
        start = number(contact.get("start"), "contact.start")
        end = number(contact.get("end"), "contact.end")
        if start < samples[0]["t"] or end > samples[-1]["t"] or start >= end:
            raise ValueError("contact window must lie inside sampled range and have positive length")
        window = [s for s in samples if start <= s["t"] <= end]
        points = [require(s, "points", contact["point"]) for s in window]
        row = {"point": contact["point"], "start": start, "end": end, "samples": len(points)}
        if len(points) < 2:
            result["unverified"].append(f"contact has fewer than two samples: {contact['point']}")
        else:
            if abs(window[0]["t"] - start) > 1e-9 or abs(window[-1]["t"] - end) > 1e-9:
                result["unverified"].append(f"contact window boundaries not sampled: {contact['point']}")
            drift = max(norm(difference(p, points[0])) for p in points) / height
            path = sum(norm(difference(b, a)) for a, b in zip(points, points[1:])) / height
            row.update({"max_drift_H": drift, "path_length_H": path})
            if drift > contact_limit:
                result["issues"].append(f"contact drift: {contact['point']} [{start}, {end}]")
        result["contacts"].append(row)
    if not data["loop"] and not contacts:
        result["unverified"].append("no loop or contact checks requested")
    result["status"] = "fail" if result["issues"] else "review" if result["unverified"] else "pass"
    result["thresholds"] = {"position_H": position_limit, "contact_H": contact_limit,
                            "angle_degrees": angle_limit, "velocity_H_per_s": velocity_limit}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--position-limit", type=float, default=0.002)
    parser.add_argument("--contact-limit", type=float, default=0.005)
    parser.add_argument("--angle-limit", type=float, default=0.5)
    parser.add_argument("--velocity-limit", type=float, default=0.05)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8-sig"))
        report = audit(data, args.position_limit, args.contact_limit, args.angle_limit, args.velocity_limit)
        if args.output and args.output.resolve() == args.input.resolve():
            raise ValueError("output must not overwrite input")
        output = json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False)
        if args.output:
            args.output.write_text(output + "\n", encoding="utf-8")
        else:
            print(output)
        return 1 if report["status"] == "fail" else 3 if report["status"] == "review" else 0
    except (ValueError, TypeError, OSError) as exc:
        print(f"Audit error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
