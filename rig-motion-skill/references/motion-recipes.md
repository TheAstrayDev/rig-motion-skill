# Motion recipes: author starting points

Search: idle, walk, run, jump, combat, recoil, pickup, acting, quadruped, tail.

All numbers below are artistic starting hypotheses, not platform requirements. Choose duration through reference, personality, and gameplay. For phase `p` in `[0,1]`, time is `t=p*T` and frame is `f=f0+p*T*effective_fps`. Preserve event order when rounding.

## Idle: attention and weight

Choose an asymmetric base pose and attention target. Start a quiet loop around 2–4 seconds: a small breathing beat, delayed head/hand settling, and stable support. For R6, do not scale the torso for breathing by default; small torso tilt/offset and head compensation can suffice. A Minecraft cinematic breathing control still must preserve contacts.

Example phases: 0 base; .25 inhale/small rise; .5 return; .75 secondary settle; 1 endpoint. Begin barely visible and increase for camera size. A rare separate blink/look clip can work better than a short loop with constant repeated blinking.

Check three repeats, no torso drift, stable feet, motivated head motion, and a clean transition into walking.

## Walk: two steps per cycle

For a first test, `T≈0.8–1.2 s` with left and right steps in one cycle. Specify both contact windows and virtual speed `v` for in-place motion. Cycle travel is `D=v*T`; equal-rhythm opposite-foot contacts are approximately `D/2` apart. This is different from one foot's full stride.

| Phase | Event | Rigid R6/Minecraft task |
|---|---|---|
| 0 | Contact A | Forward leg, readable support, arm counter-swing |
| .125 | Down/weight acceptance | Coordinate torso and leg endpoint without a knee bend |
| .25 | Passing | Swing leg passes support; torso travels over it |
| .375 | Up/push | Prepare the next contact without an impossible toe roll |
| .5 | Contact B | Opposite support |
| .625/.75/.875 | Second half | Same tasks with meaningful small asymmetry |
| 1 | Contact A endpoint | Close pose and spacing |

A grounded moving walk keeps its contact marker nearly fixed in world space during stance. An in-place foot can move backward relative to the root: reconstruct its world path using `+v*t` before measuring slip. Backward local motion alone is not an error.

R6 has one torso. Replace human chest/hip counter-rotation with shoulder/head relationships and restrained torso yaw. Apply the same constraint to rigid Minecraft; use separate pelvis/chest controls only if the inspected cinematic rig has them. Mirroring the first half does not prove the second half balances correctly.

## Run: acceleration and flight

Start around `T≈0.45–0.75 s`. Establish contact → compression → push → flight → next contact. Flight depends on the chosen gait; fast walking or shuffling can differ. Torso lean reflects acceleration before settling at steady speed. Keep arm swings clear of torso and props.

R6 cannot literally reproduce folded-knee human recovery. Adapt leg trajectory, torso height/lean, and whole-segment length. For gameplay, compare speed with `D/T` and test start/stop. Playback speed changes cadence but does not necessarily fix stride amplitude or posing.

## Jump and landing

For a roughly 1–1.5 second cinematic one-shot, try: 0 base; .15 preparation; .25 compression; .32 takeoff; .52 apex; .70 first contact; .78 maximum absorption; 1 settle. First contact and deepest compression are different events. R6 compression uses composition/offset, not a knee bend.

Use `z(t)=z0+v0*t-0.5*g*t²` as a constant-gravity starting trajectory, with time measured from takeoff and gravity in scene units. Stylized hanging/retiming is a deliberate deviation. The root path must remain comprehensible even during rapid pose changes.

Gameplay trajectory belongs to the controller/physics. Avoid a second baked world parabola in the visual root unless required. Separate takeoff, airborne, and landing clips when useful. Test different landing heights, re-entry, and early interruption.

## Strike, sword, and shot

Define target, support, leader, and impact point. Example phases: 0 ready; .22 anticipation; .42 acceleration; .50 impact; .58 follow-through; .78 recovery; 1 ready/new state. Responsive gameplay may require different proportions.

Track weapon tip and grip. Maximum spacing often occurs immediately before contact, followed by reaction or continued travel through the target. Identical slow-in/out on both sides weakens impact. A hit reaction begins from its cause, then redistributes support.

R6 force comes through torso and shoulder. Compensate for the absent elbow through body staging and weapon orientation. Check both grips on two-handed weapons without stretching. Recoil is a short impulse followed by slower recovery; symmetric continuous sine motion reads as vibration.

For gameplay, verify impact markers, blending, cancellation, and repeated attacks. One looping attack is not a default solution for every state.

## Pickup and handoff

See → decide → approach → contact → establish grip → lift → settle. The prop must not follow the hand before contact. Preserve world pose at a space switch and inspect neighboring frames. On release, assign a new space/trajectory continuously.

Heavy props change torso and support mechanics. A slow hand on a frozen body communicates little weight. R6 lacks bending for deep reaches: change pose/root offset and object placement. A deep ground pickup may need stylization or a different rig contract.

## Turn, acting, and dance

Turn-in-place: intention/look, support pivot, other-foot repositioning, torso/head settle. Rotating the whole body over glued feet causes slip. Reaction: stimulus → recognition → decision → gesture. One strong beat can outperform continuous wobbling.

For dance, establish accents, downbeats, and contact rhythm before upper-body gestures. Movement on every beat is unnecessary; pauses create character. Do not silently change FPS to retime audio. Check repeat phase compatibility and accumulated travel.

## Mobs and tails

Choose quadruped gait through reference and support, then phase the legs. Do not assign a random biped pattern to four legs. The torso path supports the contact schedule. Heavy mobs benefit from preparation and controlled inertia rather than meaningless high-frequency vibration.

For tails/ears, establish base motion before drag and delayed extremes. Equal offsets are a starting scaffold; refine collisions and the cause of each swing. Tail periods must fit the intended loop. Independent periods may be deliberate, but a single seamless clip must account for them.

When teaching rather than producing a specific shot, progress through rigid weight shift → walk → start/stop → jump → prop grip → attack → short acting beat. Advance through demonstrated quality, not repetition count.
