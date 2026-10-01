# Tutorial analysis and adaptation to R6/Minecraft

Research date: **October 1, 2026**. The foundation is primary written lessons, editor/runtime documentation, and published video descriptions. Full videos and paid classes were not watched for this research. There are no invented timestamps, frame-by-frame observations, or claims to have completed an author's entire course. Numeric recipes and style profiles are practical author synthesis to evaluate in actual projects.

## Walk: Jason Martinsen / Animation Mentor

The [written lesson](https://www.animationmentor.com/blog/tutorial-animating-human-walk-cycle/) discusses contact/down/passing/up, upper-body relationships, arm overlap, and moving versus in-place walking.

Transfer the contact schedule and body mass before limb detail. R6 cannot literally copy foot roll, knee cleanup, or separated chest/pelvis controls. Preserve their purpose—weight acceptance and counteraction—through torso placement, whole-limb direction, and real contact markers. A cinematic Minecraft rig may have segmentation; inspect it.

Exercise: one rigid walk at constant v, checking reconstructed world contact and the loop seam. Diagnose D/T and stance trajectory before shoulder polish. This separates mechanics from decorative arm swings.

## Timing/spacing: Martinsen

The [text](https://www.animationmentor.com/blog/tutorial-animate-with-timing-and-spacing-in-mind/) discusses time contrast, holds, rapid transitions, and energy changes.

Large block silhouettes emphasize contrast. Faster transition does not mean fewer keys: duration and interpolation differ. For a weak sword strike, inspect tip velocity before contact and reaction holds. Long gameplay anticipation can reduce responsiveness.

Exercise: two clips with equal extremes and T but different spacing. Compare force and gesture readability at normal speed. Do not attribute the recipe's phase percentages to this source.

## Overlap: Anthony Wong

The [written tutorial](https://www.animationmentor.com/blog/tutorial-overlap-pendulum-motion-animation/) connects drag/offsets to base movement through chain and figure-eight examples.

Apply this to tails, ears, accessories, and head settling. Do not add another R6 arm joint by default. A copied delayed curve can create an unexplained wave when base speed is inconsistent. Later extremes should follow an impulse or stop.

Exercise: abrupt torso stop and two secondary-motion variants. Trace base/accessory endpoint, checking weight, loop, and collision. Support for the principle does not establish exporter support for a procedural chain.

## Jump/landing: Martinsen

The [lesson](https://www.animationmentor.com/blog/tutorial-animate-a-jump-and-land/) separates preparation, takeoff, offsets, airborne arc, contact/compression, and settling.

Preserve causal structure on a rigid body through silhouette compression/extension. Separate trajectory and pose: an appealing airborne shape cannot fix a root slowing before the ground. Gameplay physics owns the path; film authors it.

Exercise: equal root trajectories with two landing reactions. Inspect time to absorption and torso/head/arm sequence when weight is weak. Combining contact and settle into one pose loses distinct consequences.

## Anticipation and body mechanics

[Anticipation](https://www.animationmentor.com/blog/anticipation-the-12-basic-principles-of-animation/) frames preparation as a readable cause. [Wayne Gilbert's discussion](https://www.animationmentor.com/blog/animation-tips-tricks-what-makes-or-breaks-a-good-body-mechanics-shot/) emphasizes intention and forces beyond attractive pose changes.

For a faceless block character, head direction and support shifts explain decisions. Preparation can be an attention pause rather than a large backward swing. A heavy walk should not turn into a weightless stop without a deliberate style reason.

Exercise: notice danger → decide → retreat, without face or effects. Evaluate intention through normal playback/silhouette before polish. These sources do not provide platform-specific R6 numeric standards.

## Microsoft/Blockbench: model, clip, trigger

The [Bedrock lesson](https://blockbench.net/wiki/guides/bedrock-modeling/) connects bones, keys, and controllers. Conditional blending is not equivalent to restarting a one-shot.

Check repeated and interrupted events, not only the first successful preview. Motion design and runtime wiring are separate concerns; correct keys can coexist with wrong aliases or transitions.

Exercise: reaction one-shot with state re-entry. Compare first/second trigger, early interruption, and reload. Java needs its own runtime; a Bedrock controller is not ready-made GeckoLib code.

## BPS / Squared Media Minecraft Blender series

Research covered descriptions of [Getting Started](https://www.youtube.com/watch?v=Ik7jPH2sZNk) and [Scene Setup](https://www.youtube.com/watch?v=0-gA7O6SCdw), not footage. They describe world export → Blender/MCprep → set, rig, skin, and props, using older Blender 2.7.

The production organization remains useful: prepare environment/assets before final shot polish. Update collections, materials/rendering, addons, and rigs through current documentation. Descriptions cannot establish specific arcs, acting choices, or frame-level curves. Do not present historical installers/download links as guaranteed current.

## Blender Studio and current tools

The [Blender Fundamentals announcement](https://studio.blender.org/blog/blender-fundamentals-training-update-3d-animation/) describes basic timing/spacing/weight education. An announcement is not evidence of completing the exercises. Transfer simple-form motion control before complicated rigs and verify current UI/API, including Actions/slots, in the manual.

## Reconciling common advice

| Advice | Useful principle | Necessary check |
|---|---|---|
| Make it smooth | Easing can serve a transition | Pose, contact, force, export interpolation |
| Add overlap | Secondary action can express inertia | Base trajectory, collisions, silhouette, loop |
| Copy a human walk | Contacts, weight, rhythm transfer | Actual available joints |
| Bake everything | Some exporters need evaluated transforms | Preserved source, correct target, no doubled constraints |
| Export succeeded | A potential engine input exists | Wiring, trigger, blend, version, real playback |
| More FPS/keys | Sampling accuracy may improve | Style and actual intermediate errors |

This compares common interpretations rather than quoting particular authors. Work through action clarity, mechanics/contact, timing/spacing, polish, and verified transfer. [Sources](sources.md) records access scope.

## Camera, effects, and sound

[Advanced analysis](advanced-tutorial-analysis.md) covers staging/reference lessons, Blender Studio procedural production, Simulation Nodes, physics, and sound layering. It distinguishes inspected text, lesson descriptions, search excerpts, and uninspected videos/production files.
