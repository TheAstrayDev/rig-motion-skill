# Roblox R6 in Blender

Search: RootJoint, Motor6D, C0 C1, rigid, proxy, IK, export mapping, translation.

## What counts as R6

Classic R6 has visible `Head`, `Torso`, `Left Arm`, `Right Arm`, `Left Leg`, and `Right Leg`. Technical `HumanoidRootPart` is additional to those six. A typical arrangement is:

```text
HumanoidRootPart
└─ Torso                 RootJoint
   ├─ Head               Neck
   ├─ Left Arm           Left Shoulder
   ├─ Right Arm          Right Shoulder
   ├─ Left Leg           Left Hip
   └─ Right Leg          Right Hip
```

This guides inspection; it is not an instruction to rename every Blender bone. An importer may require its own names and metadata. Inventory actual Studio joints and part mapping. An arbitrary six-bone humanoid does not prove compatible joint frames.

R6 lacks separate pelvis/chest, elbows, knees, wrists, and feet. Torso yaw affects shoulders and hips together. Use head, independent shoulder/hip rotations, and support placement for counteraction. Standard R6 does not have chest/pelvis counter-rotation controls.

## Three rig levels

1. Destination rig: actual Studio R6 and its joint frames.
2. Animation/control rig: convenient FK/IK controls and optional proxy, with potentially different naming.
3. Export representation: final transforms for the verified destination mapping.

Extra controls can drive existing exported parts. Extra deform joints change the model and require a different runtime rig. A cinematic R6-inspired rig is a valid film choice with a different contract.

## Current and historical transfer routes

[RBXMonkey/Cautioned](https://github.com/Cautioned/Blender-Animations-Plugin) documents a paired Blender addon/Studio plugin, synchronization, and armature selection. [Releases](https://github.com/Cautioned/Blender-Animations-Plugin/releases) include changes to timing ranges, slots, easing, and import routes. Record installed versions; a README does not establish future Blender compatibility.

The [Den_S exporter/importer](https://create.roblox.com/store/asset/716953901/Blender-rig-exporteranimation-importer) is a historical route. Its OBJ references may describe plugin-specific metadata, not animation in standard OBJ. Do not mix old and new addon procedures.

For a new gameplay R6 clip, a useful initial choice is the actual Studio rig exported through a compatible tool pair with an early round-trip. FBX is appropriate only after verifying this rig/importer combination; it is not a universal R6 transfer solution.

## Matrices and rest pose

A Motor6D relation can be reasoned about as:

`W_child = W_parent * C0 * Transform * inverse(C1)`

The target animation transform follows world relationship and C0/C1, not three copied Blender Euler numbers. Basis conversion includes orientation, handedness, units, and multiplication order. Prefer a tested exporter. A custom converter must reproduce identity/rest pose and separate axis rotations in a minimal probe.

[Pose documentation](https://create.roblox.com/docs/reference/engine/classes/Pose/MaskWeight) describes part-name mapping and animation offsets through Motor6D.Transform rather than changing C0/C1. The linked property is deprecated; use class documentation for current context rather than adopting that property. CFrame can contain translation, but transfer depends on rig/exporter. Distinguish a rotation-only project restriction from technical offset capability.

Changes concerning [avatar joints](https://create.roblox.com/docs/reference/engine/classes/Motor6D) in R15 workflows do not automatically prescribe an R6 migration. Inspect the actual instance and Studio version.

## Minimal probe

In a copy, animate neutral → one arm rotated roughly 30 degrees → neutral. Separately test torso tilt and any required small translation. Preserve rest skeleton and part names. Check duration, axes, pivot, handedness, parenting, first/last pose, and a prop joint if needed.

Compare Blender and Studio at the same seconds, including between keys. Equal key poses can still differ through easing. Resolve discrepancies before complex combat.

## Posing and contacts

Use a contact marker at the leg endpoint. Single-segment IK can assist direction but supplies neither bending nor universal foot lock. Do not silently allow limb stretch in gameplay. Lower the torso through permitted offsets and leg placement; a deep human crouch with both flat feet may be geometrically impossible.

Preserve arm length and silhouette for grips. Two-handed weapons may require a compromise between pose and weapon orientation because R6 lacks elbows. Adjust torso, shoulders, and prop rather than secretly stretching a limb.

Gameplay walking commonly uses in-place motion coordinated with controller speed. Torso offset does not move HumanoidRootPart/collision. Jump anticipation must not delay a jump that has already occurred; takeoff/airborne/landing states can be separated.

## Delivery

Save `.blend`, the agreed Action range, export/local Studio animation, preview, and destination-rig notes. Check priorities/weights, blending, default Animate, retriggering, and asset access. An uploaded animation ID is a separate actual result; a local KeyframeSequence is not a published asset.
