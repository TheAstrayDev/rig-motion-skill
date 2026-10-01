# Minecraft animation in Blockbench

Search: Bedrock, Java, groups, pivot, channels, Molang, interpolation, GLB, bbmodel5.

## Format determines capability

Inspect format ID and destination before authoring. [Formats](https://blockbench.net/wiki/blockbench/formats/) have different capabilities; a `.json` extension does not establish a common animation schema.

- Bedrock entity: bones/groups, geometry JSON, animation JSON, client wiring, and controllers as needed.
- Java block/item: vanilla models do not gain arbitrary bone animation from Animate. Animated textures/display transforms are separate features. Choose a mod/runtime for entity or complex motion.
- GeckoLib: matching plugin/project type and the project's library version. Do not convert an entire project to GeckoLib 5 by default.
- Generic/low-poly film: verify animation and 3D export support for that format.

## Structure and pivots

Animate groups/bones containing cubes. Add a root when common visual motion is required; organize head/body/limbs/attachments by function. Keep names unique and stable, and inspect references after renaming.

Custom humanoids may use root → body/head/limbs or root → hips → body/head/limbs. Choose mechanics and runtime requirements. Existing mobs can expect specific names and relationships; no single hierarchy is universal.

Place shoulder pivots at the joint rather than cube center. Jaw, door, and tail pivots differ. Parent rotation moves descendants; large position tracks should not compensate for a wrong pivot. Test neutral, raised arm, and extreme head turn first.

Save editable `.bbmodel` separately from engine exports. In [bbmodel 5](https://blockbench.net/wiki/docs/bbmodel/), group definitions and the outliner hierarchy are separated. External generators must inspect `meta.format_version` and real samples rather than assuming old group data lives entirely in outliner entries.

## Keys and clip duration

Name the clip, set duration/loop mode, key main phases and contacts, then add breakdowns. Timeline snapping is an editor aid, not proof of gameplay FPS. Seconds allow comparison across runtimes.

In the [Animate interface](https://blockbench.net/wiki/guides/blockbench-overview-tips/), rotation/position/scale channels and Graph Editor serve distinct purposes. Verify the selected bone/channel and axis with a small movement. Changing geometry in Edit mode changes the source shape rather than merely repairing a pose.

Play several loop repeats. Set periodic values at 0 and T and check neighboring spacing. Matching endpoint poses can still hesitate at the seam. `hold_on_last_frame` holds a pose; it does not establish a seamless loop.

## Interpolation follows the actual export

Choose Linear for intended uniform spacing, smooth/Bézier for controlled easing, or stepped for deliberate supported holds. None repairs incorrect poses. Inspect what the destination exporter actually writes; exported behavior takes precedence over editor appearance.

Bedrock commonly uses numeric keys, `pre`/`post`, and `lerp_mode: "catmullrom"`; do not substitute invented Blender tangent fields. Numerically bake unsupported curve shapes and inspect intermediate samples. Accept simplification only after comparing contacts and impacts.

## Molang

[Animation Expressions](https://blockbench.net/wiki/guides/animation-expressions/) distinguishes editor placeholders from runtime expressions. For Bedrock, use a verified `query.anim_time` rather than editor-only `time`; trigonometry uses degrees. An author periodic probe is:

`A * math.sin(query.anim_time * 360 / T)`

Replace A/T with actual numeric values; they are not predefined Molang variables. Constant frequency is useful for a probe. Gameplay walking must account for speed/distance and state. Sine on every channel does not create weight transfer or acting.

Expressions inside key values and smooth interpolation can have format limits. Verify export and engine behavior. GLB can carry baked keys, not live environment queries or state changes; variable-driven faces and speed ramps do not transfer automatically.

## Preview and export

Inspect contacts, silhouettes, parents, loops, grips, and clipping; inspect actual triggers/transitions for gameplay. Export a short rotation/position probe before production. Install a plugin because an operation requires it, not because an old tutorial mentions it.

Use GLB/glTF for Blender transfer when supported by [3D Export](https://blockbench.net/wiki/guides/export-formats/). Standard OBJ carries no animation. Engine files and GLB previews may be separate deliverables from one `.bbmodel` source.
