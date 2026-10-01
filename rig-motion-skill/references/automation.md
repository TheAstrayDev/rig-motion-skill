# Automation and audit contracts

## Blender and MCP

Discover available tools and read their real schemas. Python execution capability does not establish bpy version, selected object, or scene context. Inspect the scene and work with named datablocks. Operators need correct mode, active object, and selection. Inspect reference scripts before executing them.

For Blender automation:

- Check `bpy.app.version` and property availability instead of guessing UI from old tutorials.
- Prefer `keyframe_insert`/data APIs when suitable rather than expressing everything through context-sensitive `bpy.ops`.
- Modern Actions use slots/layers/strips/channelbags; legacy `action.fcurves` is not universal. Inspect the API and assigned slot.
- Sample **evaluated** transforms after constraints, drivers, and NLA. A control's raw location is not world foot position.
- Combine evaluated armature `matrix_world` with evaluated pose-bone matrix and the marker's local offset. Bone head/tail may differ from a cube's contact corner.
- Preserve and restore frame/subframe during inspection. Stateful simulations need their own sampling/cache contract; unrelated `frame_set` calls are not equivalent to physical playback.
- Inspect object and pose movement. A moving parent can cause drift despite a constant bone channel.

This package has no universal exporter. Arbitrary Blender rigs do not reveal reliable R6 basis/metadata or Minecraft runtime contracts.

## Motion samples

[samples.example.json](../assets/samples.example.json) contains synthetic helper input, not extracted animation or render evidence.

```text
schema              "rig-motion.samples.v1"
height              positive H in the same units as points
space               "world", "support-local", or "root-local"
loop                true/false
loop_points         names of genuinely periodic points
loop_rotations      names of periodic orientations
samples[].t         strictly increasing seconds, including endpoints
samples[].points    {name: [x,y,z]}
samples[].rotations {name: [w,x,y,z]}, finite nonzero quaternion
contacts[]          {point, start, end}, boundaries inside sampled range
```

For a loop, supply at least one explicit loop label. Exclude intentional traveling root positions from `loop_points`. To inspect periodic posing on a moving character, use a separate root-local dataset computed with the locomotion root's inverse world transform. Root-local contacts are rejected because that space can conceal sliding. Do not mix coordinate spaces within a dataset; use separate files for distinct moving supports.

For in-place walking, reconstruct world contact through the assumed controller trajectory. For moving support, compute `inverse(W_support(t))*P_world(t)`. A stable bone origin does not prove that a rotating cuboid's surface stays planted. Use the real contact marker and adjust contact windows for foot roll.

H is the original model height, not a changing per-frame bounding box. Contacts include start/end and need sampled boundary times. Do not invent contact schedules automatically. Sparse samples can miss defects; choose density through speed and confirm in playback.

From the skill folder:

```powershell
python scripts/motion_audit.py assets/samples.example.json
python scripts/motion_audit.py my-samples.json --output motion-report.json
```

The helper checks position/orientation endpoints, finite-difference **linear** seam velocity, maximum contact displacement from its first sample, and path length. It does not check angular velocity, unsampled interpolation, collision, pose appeal, or event sync. Quaternion comparison uses shortest orientation distance and cannot recover turn count.

Configure `--position-limit`, `--contact-limit`, `--angle-limit`, and `--velocity-limit`. Position/contact values are fractions of H, velocity is H/s, angle is degrees. [Quality review](quality-review.md) explains defaults and sampling limits.

## Static Bedrock audit

```powershell
python scripts/bedrock_audit.py assets/probe.animation.json --geometry assets/probe.geo.json
python scripts/bedrock_audit.py entity.animation.json --geometry entity.geo.json --geometry-id geometry.my_entity --output bedrock-report.json
```

The helper inspects exported `animations`, modern `minecraft:geometry`, unique bones/parents and cycles, positive supplied duration, numeric timestamps/ranges, supported numeric vectors/pre/post, and explicit loop endpoints. Differing rotation Euler endpoints require review because three values alone do not establish orientation; position/scale mismatch fails.

Expressions, missing 0/T keys, unspecified geometry selection, unsupported channel fields, and runtime options remain unverified rather than producing false passes. `format_version` is reported, but the entire official schema is not validated. This is not Mojang certification or a validator for `.bbmodel`, GeckoLib easing, manifests, aliases, or controllers.

Both audits read input and print JSON. `--output` writes a report without allowing input-file overwrite. Exit codes: **0** supported requested checks pass; **1** detected defect; **2** invalid input/CLI; **3** further review required. For code 3, inspect `unverified`; do not automatically label the animation broken.

## Camera data and helper tests

[camera_impulse.py](../scripts/camera_impulse.py) generates offsets; it does not audit or modify Blender. Its units, envelope, frequency checks, overlap, and separate SHAKE-control application are described in [camera direction](camera-direction.md). Exit 0 means data created; 2 means input/output error. Success is not camera acceptance.

```powershell
python -B -m unittest discover -s scripts/tests -v
```

Tests cover numeric invariants, invalid input, actual diagnostic cases, and input preservation. They cannot establish correct Blender, Studio, or Minecraft playback; that needs actual application/runtime QA.
