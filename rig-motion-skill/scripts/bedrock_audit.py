#!/usr/bin/env python3
"""Static checks of exported Bedrock animation JSON; not a runtime validator."""
import argparse
import json
import math
import sys
from pathlib import Path

CHANNELS = {"rotation", "position", "scale"}


def finite(value):
    return not isinstance(value, bool) and isinstance(value, (int, float)) and math.isfinite(value)


def numeric_vector(value):
    if finite(value):
        return [float(value)] * 3
    if isinstance(value, list) and len(value) == 3 and all(finite(v) for v in value):
        return [float(v) for v in value]
    return None


def contains_expression(value):
    if isinstance(value, str):
        return True
    if isinstance(value, list):
        return any(contains_expression(v) for v in value)
    return False


def geometry_names(geometry, identifier=None):
    if not isinstance(geometry, dict) or not isinstance(geometry.get("minecraft:geometry"), list):
        raise ValueError("geometry must use minecraft:geometry array (modern exported schema)")
    candidates = geometry["minecraft:geometry"]
    if not candidates or any(not isinstance(g, dict) for g in candidates):
        raise ValueError("geometry entries must be objects")
    if any(not isinstance(g.get("description", {}), dict) for g in candidates):
        raise ValueError("geometry description must be an object")
    if identifier:
        candidates = [g for g in candidates if g.get("description", {}).get("identifier") == identifier]
    if len(candidates) != 1:
        raise ValueError("select exactly one geometry with --geometry-id")
    bones = candidates[0].get("bones")
    if not isinstance(bones, list) or not bones:
        raise ValueError("geometry must contain a nonempty bones array")
    names = []
    for bone in bones:
        if not isinstance(bone, dict) or not isinstance(bone.get("name"), str) or not bone["name"]:
            raise ValueError("geometry bone requires nonempty name")
        names.append(bone["name"])
    if len(names) != len(set(names)):
        raise ValueError("duplicate bone names in geometry")
    parents = {}
    for bone in bones:
        parent = bone.get("parent")
        if parent is not None and (not isinstance(parent, str) or parent not in names):
            raise ValueError(f"unknown parent of bone {bone['name']}")
        parents[bone["name"]] = parent
    for name in names:
        seen, current = set(), name
        while current is not None:
            if current in seen:
                raise ValueError("cycle in geometry bone hierarchy")
            seen.add(current)
            current = parents[current]
    return set(names)


def audit(data, geometry=None, geometry_id=None, tolerance=1e-4):
    if not isinstance(data, dict) or not isinstance(data.get("animations"), dict):
        raise ValueError("expected exported animation JSON with animations object; not .bbmodel")
    if not data["animations"]:
        raise ValueError("animations object must not be empty")
    if not isinstance(data.get("format_version"), str):
        raise ValueError("format_version string is required")
    if not finite(tolerance) or tolerance <= 0:
        raise ValueError("tolerance must be positive and finite")
    names = geometry_names(geometry, geometry_id) if geometry is not None else None
    report = {"scope": "static names, times and numeric loop endpoints; no curve or runtime evaluation",
              "format_version": data["format_version"], "clips": {}, "issues": [], "unverified": []}
    if names is None:
        report["unverified"].append("geometry not supplied; bone mapping unverified")
    for clip_name, clip in data["animations"].items():
        if not isinstance(clip, dict):
            raise ValueError(f"{clip_name}: expected object")
        issues, unknown = [], []
        length = clip.get("animation_length")
        length_ok = finite(length) and length > 0
        if length is not None and not length_ok:
            issues.append("animation_length must be positive and finite")
        loop = clip.get("loop", False)
        if not isinstance(loop, bool) and loop != "hold_on_last_frame":
            issues.append("unsupported loop value")
        if not length_ok:
            unknown.append("effective duration not evaluated")
        for option in ("anim_time_update", "start_delay", "loop_delay", "blend_weight", "override_previous_animation"):
            if option in clip:
                unknown.append(f"{option} runtime behavior not evaluated")
        bones = clip.get("bones", {})
        if not isinstance(bones, dict):
            raise ValueError(f"{clip_name}.bones: expected object")
        if not bones:
            unknown.append("no bone transforms; effects-only clip not evaluated")
        channels_checked = 0
        for bone_name, bone in bones.items():
            if names is not None and bone_name not in names:
                issues.append(f"unknown geometry bone: {bone_name}")
            if not isinstance(bone, dict):
                raise ValueError(f"{clip_name}.{bone_name}: expected object")
            for channel, value in bone.items():
                if channel not in CHANNELS:
                    unknown.append(f"{bone_name}.{channel} not evaluated")
                    continue
                label = f"{bone_name}.{channel}"
                constant = numeric_vector(value)
                if constant is not None:
                    channels_checked += 1
                    continue
                if contains_expression(value):
                    unknown.append(f"{label}: expression not evaluated")
                    continue
                if not isinstance(value, dict) or not value:
                    issues.append(f"{label}: unsupported channel structure")
                    continue
                keys = []
                for raw_time, key in value.items():
                    try:
                        t = float(raw_time)
                    except (ValueError, TypeError):
                        issues.append(f"{label}: invalid timestamp {raw_time}")
                        continue
                    if not math.isfinite(t) or t < 0 or (length_ok and t > length + tolerance):
                        issues.append(f"{label}: timestamp outside clip: {raw_time}")
                        continue
                    before, after = key, key
                    if isinstance(key, dict):
                        mode = key.get("lerp_mode", "linear")
                        if mode not in ("linear", "catmullrom"):
                            unknown.append(f"{label}: unsupported lerp_mode {mode}")
                        if set(key) - {"pre", "post", "lerp_mode"}:
                            unknown.append(f"{label}: extra key fields not evaluated")
                        before = key.get("pre", key.get("post"))
                        after = key.get("post", key.get("pre"))
                    pre, post = numeric_vector(before), numeric_vector(after)
                    if pre is None or post is None:
                        if contains_expression(before) or contains_expression(after):
                            unknown.append(f"{label}@{raw_time}: expression not evaluated")
                        else:
                            issues.append(f"{label}@{raw_time}: expected scalar/vector or pre/post")
                    keys.append((t, pre, post))
                keys.sort(key=lambda k: k[0])
                if len({k[0] for k in keys}) != len(keys):
                    issues.append(f"{label}: duplicate numeric timestamps")
                channels_checked += 1
                if loop is True and keys:
                    first, last = keys[0], keys[-1]
                    if not length_ok or abs(first[0]) > tolerance or abs(last[0] - length) > tolerance:
                        unknown.append(f"{label}: explicit 0/T loop keys not available")
                    elif first[2] is not None and last[1] is not None and last[2] is not None:
                        error = max(abs(a - b) for endpoint in (last[1], last[2])
                                    for a, b in zip(first[2], endpoint))
                        if channel == "rotation":
                            # Euler component equivalence is insufficient for general orientation.
                            if error > tolerance:
                                unknown.append(f"{label}: Euler endpoints differ; compare evaluated orientations")
                        elif error > tolerance:
                            issues.append(f"{label}: numeric loop endpoint mismatch")
                    else:
                        unknown.append(f"{label}: numeric loop endpoints unavailable")
        for effect in ("sound_effects", "particle_effects", "timeline"):
            if effect in clip:
                unknown.append(f"{effect} events not evaluated")
        row = {"length": length if length_ok else None, "loop": loop,
               "channels_checked": channels_checked, "issues": issues,
               "unverified": sorted(set(unknown))}
        report["clips"][clip_name] = row
        report["issues"].extend(f"{clip_name}: {issue}" for issue in issues)
        report["unverified"].extend(f"{clip_name}: {item}" for item in row["unverified"])
    report["status"] = "fail" if report["issues"] else "review" if report["unverified"] else "pass"
    return report


def load(path):
    def invalid(value):
        raise ValueError(f"non-standard JSON numeric constant: {value}")
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(path.read_text(encoding="utf-8-sig"), parse_constant=invalid, object_pairs_hook=unique)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--geometry", type=Path)
    parser.add_argument("--geometry-id")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = load(args.input)
        geometry = load(args.geometry) if args.geometry else None
        if args.geometry_id and geometry is None:
            raise ValueError("--geometry-id requires --geometry")
        if args.output and args.output.resolve() in {p.resolve() for p in (args.input, args.geometry) if p}:
            raise ValueError("output must not overwrite source")
        report = audit(data, geometry, args.geometry_id)
        content = json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False)
        if args.output:
            args.output.write_text(content + "\n", encoding="utf-8")
        else:
            print(content)
        return 1 if report["status"] == "fail" else 3 if report["status"] == "review" else 0
    except (ValueError, TypeError, OSError) as exc:
        print(f"Audit error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
