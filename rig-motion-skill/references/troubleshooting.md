# Troubleshooting: symptoms, checks, and focused repairs

Reproduce on a copy and identify the responsible relationship. Change one cause at a time. Repeated failed attempts should lead to version/log collection and a minimal probe rather than endless reinstalling.

| Symptom | First check | Focused repair |
|---|---|---|
| Bone moves, mesh does not | Parent, modifier, groups, disabled evaluation | Connect the intended part rather than retarget everything |
| Blender moves, export is empty | Action/slot, clip, range, selected rig | Assign actual animation data and target |
| Studio torso is frozen | Part mapping, parenting, root representation | Torso-only probe and local-offset comparison |
| Wrong side/axis | Neutral and axis probes, basis conversion | Correct mapping/basis on export copy |
| Wrong scale | Units, exporter/object scale, joint offsets | Consistent scale and repeated probe |
| Detached limb | Rest offsets and C0/C1 mapping | Restore the destination rig contract |
| Foot slide | World/support coordinates, stance, speed | Coordinate torso/leg/travel rather than freeze a local curve |
| IK pop | Reach, chain length, stretch, pole, parents | Reachable pose and the specific chain settings |
| Prop jumps at grab | Space, inverse, influence, pose match | Preserve world pose and compensate at switch |
| Unwanted spin | Euler wrap/order, quaternion sign, parent turn | Repair representation while retaining intentional turns |
| Smooth becomes floaty | Timing/tangents approaching impact | Sharp arrival and meaningful holds |
| Loop hesitation | Endpoint values, neighboring spacing, range | Correct period/boundary without an extra render frame |
| No Blockbench Animate | Project format capability | Choose the required format after identifying runtime |
| Wandering pivot | Group pivot versus cube origin, parent rotation | Correct joint structure, then recheck keys |
| Blockbench FBX will not import | ASCII/binary distinction in installed versions | Verified GLB/glTF or another route |
| Minecraft clip does not play | Names, paths, aliases, scripts/controllers | Repair the broken reference and inspect content log |
| One-shot plays once | Re-entry/reset and blend/state logic | Repeatable trigger/state transition |
| Doubled animation | Active layers/controllers, additive tracks | Establish bone/channel ownership |
| Molang works only in editor | Editor placeholders, unsupported expressions | Supported runtime query or justified numeric bake |
| Java export does nothing | Actual runtime, registration, major version | Wire according to installed runtime documentation |
| Missing GeckoLib asset | Version-4/5 paths, IDs, GeoModel | Correct paths/API for the actual major |
| Face on back of skin | Layout, UVs, mirroring | Asymmetric test skin and focused UV repair |
| Blurred/shimmering skin | Sampling, camera scale, AA, alpha | Adjust and test a moving sequence |
| Flickering outer layer | Z-fighting, offset, alpha/depth | Repair that layer/material |

Before calling a plugin bug, exclude wrong rig, slot, range, and destination. A useful report includes app/addon/runtime versions, source/export, observed seconds, expected/actual pose, and minimal reproduction. Do not request an entire project when a short probe is sufficient.
