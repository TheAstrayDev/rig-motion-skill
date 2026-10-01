# Blender: staging, curves, rigging, and baking

Search: Action slots, NLA, Constant, Bézier, quaternion, Euler, space switching, bake, preview.

## Prepare without damaging the rig

Inspect object transforms, rotation modes, parents, constraints, control visibility, rest/bind pose, animation data, range, and FPS/fps_base. Identify controls that actually move visible parts. For linked rigs, inspect edit restrictions/library overrides; do not automatically make the entire project local.

For a new rig, settle scale/axes before binding and keys. Applying all transforms to an already animated rig can damage rest offsets or constraints. Diagnose scale mismatch first; correct on an export copy and repeat the probe.

With [Action slots](https://docs.blender.org/manual/en/latest/animation/actions.html), Action and slot jointly determine a datablock's animation. Check both. Assigning an Action does not guarantee the right curves; modern Actions need not expose legacy `.fcurves`. Active NLA strips, time remapping, and influence can alter correctly assigned motion.

Preserve existing Actions. Name versions explicitly, such as `walk_r6_v03`. Verify retention of used/unassigned Actions through the installed version's users, fake-user, or asset workflow.

## Blocking and curves

Establish poses and durations first. Constant interpolation helps blocking; conversion to Bézier should preserve event times. Spline root/torso, then support, limbs, and secondary action. Review the complete beat at normal speed after each group.

A keyed control does not guarantee a stationary limb endpoint because parents can move. Inspect a world marker. For moving support, measure support-local contact and inspect world travel separately.

In the [Graph Editor](https://docs.blender.org/manual/en/latest/editors/graph_editor/fcurves/editing.html), repair the meaningful interval rather than every handle:

| Symptom | Inspect | Repair |
|---|---|---|
| Floaty approach to impact | Speed decreases before contact | Rebuild spacing/tangents for a sharp arrival |
| Unwanted overshoot | Curve exceeds the intended extreme | Local clamped/manual handles; recheck pose |
| Unwanted hard stop | Velocity breaks without cause | Breakdown and coordinated tangents |
| Foot drift | World marker moves during stance | Parent/foot relationship, not only leg curves |
| Loop hesitation | Different endpoint tangents | Neighboring periods and world trails |

A linear channel need not produce a straight world trajectory. Rotation curves alone do not describe a hand endpoint arc.

## Euler and quaternion

Choose rotation modes before extensive keying. Euler is convenient for editable axis turns, but axis order can produce gimbal lock. Quaternion can help free orientations but does not guarantee the intended path or encode the number of complete turns from a single endpoint. Inspect actual results and [rotation modes](https://docs.blender.org/manual/en/latest/advanced/appendices/rotations.html).

For unwanted spins, compare world orientations and curves. A ±180-degree jump can be representational; 0→360 can be intentional. Apply Euler Discontinuity Filter on a copy only when it preserves the desired path. Custom quaternion generation should normalize values and maintain sign continuity: if `dot(q_prev,q)<0`, negate q. Endpoint comparison treats q and -q as equivalent.

## IK/FK and space switching

Use IK for contact/precise targets and FK where convenient for free arcs. Inspect existing snapping tools. Changing influence without matching pose produces pops. Check [IK Chain Length](https://docs.blender.org/manual/en/latest/animation/constraints/tracking/ik_solver.html): zero may affect the entire available chain rather than one segment.

For grab/release, use the rig's space switch or [Child Of](https://docs.blender.org/manual/en/latest/animation/constraints/relationship/child_of.html). Preserve world transform, coordinate inverse, and key influence/compensation at the switch. Inspect neighboring frames for continuity. Do not apply Set Inverse indiscriminately; evaluation state and constraint order matter.

Handoffs need two precise grip moments and a motion leader. Avoid dependency cycles where the sword follows the hand while the hand follows the sword.

## Bake a separate copy

If the exporter samples the evaluated rig correctly, use that workflow. Otherwise:

1. Duplicate the production file/export rig and record range/effective FPS.
2. Select actual destination/deform bones rather than arbitrary controls.
3. Use [Bake Action](https://docs.blender.org/manual/en/latest/editors/nla/editing/strip.html) with Visual Keying for constraint results; choose Pose/Object from the real source and initially use step 1.
4. Clear constraints only on the export copy. Clearing parents is not a default: hierarchy can be required.
5. Disable live constraints on the copy and compare poses/contacts at keys and intermediate times. A mismatch means the bake is not accepted.
6. Reduce keys only after comparison; preserve contacts, impacts, closing endpoints, and deliberate stepped rhythm.

Step 1 does not prove subframe accuracy. Fast rotations/strikes require sampling and destination-interpolation checks. For FBX, verify clip, range, bones, leaf-bone settings, Action/NLA selection, and simplification in the installed exporter. No preset fits every R6/Minecraft route.

## Preview and render

Make a diagnostic preview with a floor, simple camera, clear silhouettes, and normal speed. Inspect front/side/three-quarter and final camera. Render at the authored FPS; encoding must not accidentally speed it up.

For final film, an image sequence followed by video assembly supports recovery from interrupted rendering. Choose samples/resolution from noise and output size rather than “maximum.” Inspect blur, denoising, and pixel patterns across moving frames. Retain editable source and export.
