# Motion design for block characters

Search: intention, silhouette, support, rigid limbs, timing, spacing, arcs, anticipation, overlap, acting.

## Intention and pose

Start with a verb and attitude: cautiously peeks, confidently shoves, struggles to lift. Make restrained, stronger, and excessive versions of the decisive pose. Choose the strongest readable version that preserves character.

Check a single-color silhouette. Separate arm/torso overlaps and accidental contour tangencies. Negative space should explain the gesture. Do not open both arms symmetrically when one side should lead.

Build an R6 line of action through torso orientation, head direction, and foot placement. There is no articulated spine to bend. A Minecraft cinematic rig may bend, but inspect UV stretching and the intended angular shape.

## Weight without knees

Identify the receiving support before moving the body. In a quiet stance, the visual center of mass usually projects into the support region; during acceleration or falling, leaving it may be the point. Static balance is not a universal rule for action frames.

Choose an actual rigid-leg contact marker: a lower corner or surface center. If a long flat-foot plant is impossible, shorten the stance, change the step, or use explicitly permitted local translation after testing export. Large head bob does not solve an incompatible leg constraint.

A diagnostic planar model: a downward rod of length `L`, rotated by `theta` from vertical, ends at `z_hip - L*cos(theta)` with horizontal offset `L*sin(theta)`. A fixed endpoint requires coordinated hip position and leg angle. A cuboid's surface contact is offset from the bone axis; 3D rotation complicates this model. Two fixed rigid legs can overconstrain the pose. Change the pose or trajectory rather than asking IK for an impossible solution. This is an author diagnostic model, not a platform specification.

## Timing and spacing

Timing sets phase duration; spacing is the positional/angular distance between consecutive images. Keep the same event times and compare two in-between patterns: identical timing can produce different weight. Inspect evenly timed samples of torso, leg contact corners, hands, and weapon tips.

An author example at 24 FPS: preparation 8 frames, acceleration 3, stop 1, reaction hold 2, recovery 10. This is a starting hypothesis. Gameplay timing follows the required interaction/event.

For floaty action, inspect durations and deceleration placement before changing easing. Falling usually accelerates toward contact; easing out before the ground can remove weight. At the apex, vertical speed is small while horizontal travel and posing can continue.

In Blender, `t=(f-f0)/(fps/fps_base)`. At 24 FPS, frame 1 to 25 spans one second, but an inclusive render has 25 images. A loop video normally renders 1 through 24, with a closing key at 25. Preserve the endpoint in exported clips when the runtime needs it.

## Preparation, impact, recovery

Preparation explains direction and energy through a wind-up, lean, look, or decision pause. Surprise can start without preparation. Separate initial contact, maximum compression, and settling; one key seldom communicates all three.

Rigid squash/stretch is often compositional: lower the torso, widen the arms, compress the silhouette, then extend the gesture. Scaling requires a rig/style that permits it. Standard R6 export does not imply mesh squash, shape keys, or bending support.

## Arcs and overlap

Track hand/weapon endpoints and the head in world space. Clean local curves can produce poor arcs through parent motion. Trace a hook to the responsible parent/control and revise its breakdown.

Choose a leader from intent or force. Look → torso → arm may fit a decision; torso → arms → head may fit a heavy stop. Neither is a universal sequence. Measure delays in seconds. Equal offsets across all parts often produce an unexplained wave. Drag responds to base acceleration; a copied delayed curve is only a starting point.

## Acting without a face

Separate perception, thought, decision, and execution. Head direction identifies attention; a pause before the torso turn can reveal a choice. A small gesture should change the character's relation to the situation.

Do not gesture on every word. Choose the important thought and complete the gesture toward it. Judge broad facial states first; organize lip sync around rhythm and significant shapes. A blink may support an attention change but is not required on every pose.

Primary text discussions of [walk cycles](https://www.animationmentor.com/blog/tutorial-animating-human-walk-cycle/), [timing](https://www.animationmentor.com/blog/tutorial-animate-with-timing-and-spacing-in-mind/), [overlap](https://www.animationmentor.com/blog/tutorial-overlap-pendulum-motion-animation/), and [jumping](https://www.animationmentor.com/blog/tutorial-animate-a-jump-and-land/) support these general techniques. R6/Minecraft adaptations and timing examples are author synthesis. See [tutorial analysis](tutorial-analysis.md).
