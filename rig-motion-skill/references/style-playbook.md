# Choosing and implementing a style

These are author working profiles, not official genre names. The user's reference takes priority. Describe motion behavior rather than calling everything smooth.

Record geometry rigidity, exaggeration, hold/transition rhythm, stop quality, secondary-action amplitude, and camera behavior. Test a one- or two-second beat with simple materials. Motion style and rendering style are distinct choices: realistic lighting can accompany strongly stylized mechanics.

| Profile | Poses and rhythm | Body behavior | Useful for | Common trap |
|---|---|---|---|---|
| Classic rigid | Strong simple poses, moderate transitions | Whole limbs, precise support | R6 gameplay, vanilla-like Minecraft | Sinusoidal motion on every channel |
| Vanilla-enhanced | Recognizable swing with small offsets | Restrained torso/head accents | Mobs, quiet R6 | Detail changes the game's identity |
| Stylized cinematic | Contrasting holds and bursts, large silhouettes | Anticipation, drag, overshoot, recovery | Film; constrained/tested game clips | Effects conceal weak posing |
| Athletic/grounded | Clear support, fast acceleration, controlled stops | Force through the body | Combat, parkour | Human reference requires missing joints |
| Snappy/anime-inspired | Extremes, short transitions, accented stops | Directional silhouettes, selective smears | Film; tested game clips | Accidental airborne hovering |
| Comedic | Surprising pauses, amplified reactions | Asymmetry, chosen elastic settling | Character interaction | Symmetric waving and constant bouncing |
| Heavy/creature | Longer preparation, stable stepping | Broad support and inertial stops | Bulky R6, large mobs | Slowing a lightweight walk |
| Stepped/stop-motion | Holds on twos/threes, selective single-frame changes | Deliberate pose replacements | Film; tested game clips | Export interpolation changes the style |
| Acting/subtle | Thought and gaze lead gestures | Small coordinated shifts | Dialogue, emotion | Many movements with no clear intention |

## One beat, several styles

A character notices a sword, picks it up, and evaluates its weight:

- Classic: head turn, torso turn, exact grip, lift, new stance.
- Athletic: weight shifts before lifting; torso assists the arm; the object accelerates after grip.
- Comedic: confident grab, sword stays put, realization pause, excessive effort, sudden lift and balance correction.
- Snappy: preparation hold, rapid grab into an extreme pose, short settle; inspect in-between intersections.
- Subtle: exploratory touch, hesitation, changed grip, cautious lift.

## Extracting a reference's motion choices

After actually accessing the video, select a complete beat. Mark extrema, contact, maximum speed, and segment start/stop times. Measure fractions of duration for transfer across frame rates. A 30% preparation / 15% action / 55% reaction split is an illustrative example, not a measurement of a specific video.

Compare leading parts, silhouettes, head direction, and trails. Separate camera shake from body movement. A still image supports pose/staging analysis; timing and overlap remain hypotheses. Transfer broad style characteristics and identify changes required by the rigid rig.

## Animation on twos

At 24 FPS, holding each pose for two frames produces 12 pose updates per second and 24 output frames. This differs from rendering at 12 FPS and from smooth interpolation between sparse keys. Camera and characters can update at different rates when the result remains intentional and stable.

Blender Constant interpolation creates holds; selected transitions may move on ones. In Blockbench, test stepped behavior in the actual exporter/runtime. Repeated baked values can approximate the presentation, but gameplay blending may smooth them.

For vanilla-like modeling, the [Minecraft Style Guide](https://blockbench.net/wiki/guides/minecraft-style-guide/) supports simple geometry, texture-based detail, and consistent texel scale. Those modeling principles do not prescribe walking cadence. R6 retains whole arms and legs; a film-only smear or bend does not imply runtime support.
