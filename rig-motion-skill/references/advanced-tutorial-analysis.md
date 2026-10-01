# Learning analysis: staging, procedural VFX, and sound design

Research date: **October 1, 2026**. Sources include written articles/manuals, accessible lesson pages, and search excerpts from two BOOM articles. Full embedded videos, paid classes, demo blend files, and restricted production assets were not inspected. Each section separates source support, practical adaptation, and an exercise. Do not attribute this skill's author recipes to frame-by-frame tutorial observation.

## Staging — John Nguyen / Animation Mentor

The [article](https://www.animationmentor.com/blog/staging-the-12-basic-principles-of-animation/) discusses halves/thirds, attention lines, and consistent screen direction. Its value is a clear center of meaning rather than a collection of attractive angles.

Adaptation: block limbs/torso merge easily. Negative space and subject/background separation can matter more than facial detail. Exercise: frame one contact in three layouts without effects. Choose the view that explains pre-contact distance and consequence, then preserve screen direction through the next cut. Inspect the fast phase, not only the key pose.

## Reference in layout — Zachary Rahman

The [written lesson](https://www.animationmentor.com/blog/tutorial-green-screen-video-reference/) explains inserting reference performance into a 3D layout to catch framing problems early, through a Maya/Resolve workflow. It is not a Blender API lesson.

Adaptation: a stick sketch becomes useful when tied to camera and actor positions. Remove irrelevant visual interference; 2D matching does not prove 3D mechanics. Exercise: compare a reconstructed pose in camera and side views. Author missing foot support explicitly rather than claiming the drawing supplies it. See [the reference case](reference-case-stickfight.md).

## Cameras and Cinematography — Ere Santos

The [workshop page](https://www.animationmentor.com/blog/cameras-and-cinematography-for-animators/) describes the topic and guest instructor. The video was not watched; do not attribute shake amplitudes, constraint ordering, or lens presets to Santos.

The skill's independent workflow is shot purpose → geography → framing → base path → motivated accent → preview. [Camera direction](camera-direction.md) provides practical guidance with Blender manual references. Exercise: compare static and following views of one beat through meaning/readability, not movement quantity.

## Simulation Nodes — Simon Thommes / Blender Studio

The [lesson page](https://studio.blender.org/training/geometry-nodes-from-scratch/how-to-use-the-new-simulation-nodes-in-blender-36/) exposes description/file links and an author reply discussing fixed initial birth state, seconds/Delta Time, and difficult stateful loops. Student comments are not documented APIs. The video was not watched.

Adaptation: stable birth state/IDs support reproducible sparks/trails. Age-based ballistic formulas can serve controlled one-shots; stateful history/collision requires the relevant simulation. Exercise: directed burst at 30 and 60 effective FPS with identical second-based birth/lifespan, then bake and render nonconsecutive frames. Compare path, expiry, and stale-cache artifacts.

## Demo files and newer physics

The [official catalog](https://www.blender.org/download/demo-files/) includes particle, mesh-fracture, and 2D-puff examples with different licenses/minimum versions. The catalog was read; file node trees were not. Inspect these as separate examples, not evidence of automatic rig compatibility.

[Jacques Lucke's physics article](https://code.blender.org/2026/07/geometry-nodes-physics/) discusses hair/cloth and an XPBD framework for Blender 5.2 LTS, with experimental status and further solver plans. Adaptation: verify installed assets/API rather than treating roadmap solvers as implemented. Exercise: inspect the actual version and use a separate test scene before production. Do not replace a missing solver with guessed node names.

## Production — Impulse Purchase

The [Blender Studio article](https://studio.blender.org/blog/impulse-purchase-production-file/) describes procedural character/environment, dynamic camera, simulation elements, and VSE soundtrack in a realtime workflow. Its restricted production file was not inspected. The author's viewport performance concerns their setup, not arbitrary rigs.

Adaptation: camera, effects, and performance are connected systems. Simple shapes/shaders and clear controls help direct the whole shot. Exercise: separate camera-target/effect-birth controls, then change character scale/speed and recheck framing/sync. R6 does not require facial mocap without a face rig.

## Drawing to graphic staging — Bcon interstitials

[Beau Gerbrands](https://studio.blender.org/blog/creating-the-bcon-2023-festival-interstitials/) describes visual experiments, camera blocking, Geometry Nodes/shaders, audio iteration, and selected baking/art-direction adjustments. Text describes revising overly heavy drums/robotic texture; the audiovisual iterations were not watched/listened to.

Adaptation: test simple original shapes, simplify for timing, and use simulation as a possible art-direction starting point. Exercise: one impact ring with two mixes; remove the layer that steals attention and retain coherent visual/audio accents. Do not copy another production's graphics/music as original work.

## BOOM Library — layers and mix hierarchy

Accessible excerpts of [Top Tips](https://www.boomlibrary.com/blog/top-tips-for-trailer-sound-design/) separate transient/sustain/tail/frequency roles and crowded layering. [Sound, Voice and Music](https://www.boomlibrary.com/blog/sound-design-voice-over-and-music-for-film-trailers/) discusses emotional source choice and processing/mix organization. Full pages could not be reopened through the reader; this is a research limit, not access to paid training.

Adaptation: a small contact needs appropriate material/body/space, not every trailer accent. Exercise: transient alone, then body, then detail/tail individually. Compare at similar perceived overall loudness: is mass clearer or only louder? Remove time/frequency duplicates. Functional layering does not mandate a fixed track count.

## Manual to an original practical recipe

[Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_mesh.html) supports profile conversion, not recorded tip history. [Glare](https://docs.blender.org/manual/en/latest/compositing/types/filter/glare.html) supports highlight effects, not body mechanics or physical illumination. [Sound strips](https://docs.blender.org/manual/en/latest/video_editing/edit/montage/strips/sound.html) support layering and media dependencies, not automatic taste.

Connect evaluated contact → effect lifecycle → audible transient. Exercise: move contact by 0.1 seconds and update all dependent cues. Verify retained sync with an optional diagnostic marker, then review without effects/audio too.

## Use the analysis

Choose a source relevant to the present problem, run a short exercise on a copy, and compare in equal conditions. Equations, camera organization, and FX recipes in [camera](camera-direction.md), [VFX](vfx-blender.md), and [SFX](sfx-sound-design.md) are author synthesis. A user-supplied specific video needs separate accessible footage/transcript inspection; this catalog does not prove it was watched.
