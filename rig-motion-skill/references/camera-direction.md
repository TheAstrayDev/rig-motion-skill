# Staging, camera movement, whip pans, and controlled shake

Search: cinematography, lens, shake, recoil, whip pan, snap, 180, staging, camera.

## Decide what the viewer must see

For each shot, record whose beat it is, what changes, where attention moves, and why this framing/movement is useful. For a fight, establish distance/axis before emphasizing contacts and consequences. Avoid a close-up when the meaning depends on both support feet.

[John Nguyen's staging discussion](https://www.animationmentor.com/blog/staging-the-12-basic-principles-of-animation/) connects composition, attention, and stable screen direction to clarity. Adapt through subject size, value separation, negative space, and the partner's gaze. Keep silhouettes distinct before contact. Thirds are an aid, not a compulsory grid.

Define the A↔B/action axis. Stay on one side until a motivated transition is visible through continuous travel, a neutral view, or a new establishing shot. Deliberate axis crossing can be expressive; accidental left/right reversal confuses causality. At cuts, compare gaze/action direction, size, and contact phase. Do not accidentally replay one strike twice.

## Lens, distance, and composition

[Blender Cameras](https://docs.blender.org/manual/en/latest/render/cameras.html) documents projection, focal length/sensor, focus, and aperture. Focal length changes FOV; camera position changes perspective relationships. Apparent compression at equal framing comes from moving farther away with a longer lens, not lens change alone at a fixed position.

| Choice | Purpose | Check |
|---|---|---|
| Wider FOV, nearer camera | Space, approaching speed, depth contrast | Edge distortion and partner size |
| Moderate FOV/three-quarter | Readable two-character contact and mass | Clear limbs/torso and room for reaction |
| Narrower FOV, farther camera | Emotional distance or isolated reaction | Fall/body fit and understandable depth |
| Low/high position | Scale, status, vulnerability | Visible ground, support, and contact |
| Orthographic | Diagrammatic/isometric style | Dolly does not produce perspective enlargement |

An author starting test is 35–50 mm with 36 mm sensor width for a medium scene. Choose through actual FOV/framing: sensor fit, aspect, distance, and character height affect results. Leave room in the travel direction and required trajectory; inspect extremes and final crop.

Focus on the meaningful attention target rather than the nearest emissive effect. Two-actor contact often needs adequate depth of field around the contact plane. A rack focus needs a reason and readable timing. Establish silhouettes with DOF/blur disabled before judging detail loss.

## Movement: cause → move → stop

| Move | Useful for | Failure |
|---|---|---|
| Static/small drift | Difficult mechanics or a tense pause | Unmotivated vibration obscures precision |
| Dolly/push/pull | Approach a decision or reveal consequences | Tempo disagrees with the action |
| Track/follow | Preserve traveling actors/geography | Head bob transfers directly into framing |
| Orbit | Reveal relations or form | Aimless continuous circle or accidental axis change |
| Whip pan | Rapid attention transfer | Important contact occurs entirely in blur |
| Snap/recoil | An event-specific accent | Identical accents everywhere, no quiet contrast |
| Shake | Impact, ground force, machinery, chosen handheld | Constant noise replaces a motivated response |

For following, use a separate target near torso/action center and suppress irrelevant bob. With two actors, control a weighted center plus framing instead of blindly averaging positions. Lag must keep significant contact visible. Shape path acceleration/braking and inspect accidental easing plateaus.

## A camera rig without feedback

One useful new-rig layout is `CAM_PATH → CAM_AIM → CAM_SHAKE → Camera`. PATH owns travel, AIM owns orientation/target, SHAKE owns local offsets, and Camera owns lens/DOF. Adapt existing controls instead of automatically rebuilding parents.

A Blender camera looks along local **−Z**, with +Y up and +X right. Check rest offsets and parent inverse. A tracking constraint on the camera can cancel shake rotation; aim above the offset control or use coordinated keys. Do not parent a target to the camera that tracks it. Put the shake pivot at the optical center when intended; a distant rotation pivot also creates translation.

## Shake as a finite response

Separate base movement, directed recoil, decaying vibration, and subtle handheld. Establish directed recoil first: contact → quick displacement → smaller return → stop. Add vibration when scale/material justify it. A heavy event can produce a slow shove plus smaller fast residue. Frequency and strength are different parameters.

Use `offset(t)=A*E(t)*N(t)`: axis amplitude A, finite attack/decay envelope E, continuous deterministic signal N. Express translation as fractions of height H, rotation in degrees/radians, and time in seconds with effective FPS. Give six axes distinct phases/seeds and chosen proportions. Per-evaluation randomness makes rerenders/subframes inconsistent.

These are author starting ranges, to review in the actual image:

| Event | Active-axis rotation | Translation | Duration |
|---|---|---|---|
| Small contact | About 0.1–0.35 degrees | 0–0.002H | About 0.12–0.25 s |
| Featured impact | About 0.4–1.0 degrees | About 0.002–0.008H | About 0.2–0.45 s |
| Heavy ground landing | About 0.5–1.5 degrees, usually less roll | About 0.003–0.015H | About 0.3–0.7 s |

These are neither perfect presets nor platform rules. Begin weaker and judge at final resolution/FOV. For perspective, `f_px=width/(2*tan(FOV_x/2))`; small translations give approximately `delta_px=f_px*delta_x/Z`, and small rotations `delta_px=f_px*delta_theta` in radians. Nearby subjects amplify the same world displacement. Keep contact in frame at peak and preserve the next reaction.

Trigger from contact/physical cause rather than wind-up onset. A slightly delayed peak may help, but choose through playback. Two frames at 24 FPS is a different duration at 60 FPS. Return to the controlled base before the next readable beat.

### Manual implementation

Key zero before the event, an impact offset, a smaller reverse offset, and zero after settling. Use deliberate Linear/Bézier handles, avoiding uncontrolled overshoot. For continuous noise, [F-Curve modifiers](https://docs.blender.org/manual/en/latest/editors/graph_editor/fcurves/modifiers.html) support distinct phases and restricted/blended ranges. Check signal bias: Add/Subtract combinations can shift the center. Noise Scale is a curve-time parameter, not directly frequency in Hz. Keep it on a separate control from important base keys.

### Deterministic sample generation

From the skill folder:

```powershell
python scripts/camera_impulse.py assets/camera-shake.example.json --output camera-offsets.json
```

Input [example](../assets/camera-shake.example.json) uses `rig-motion.camera-impulse.v1`: positive effective `fps`, integer `frame_start/end`, positive `height` in scene units, and events with `time` from the first frame, duration in seconds, `translation_h[3]`, `rotation_deg[3]`, `frequencies_hz`, `decay`, and `seed`. The range must contain complete envelopes. Overlapping events sum and can increase peaks. Frequencies at/above frame-sampling Nyquist are rejected. Lower frequencies still need review because the envelope adds frequency content.

The helper's envelope has zero value and derivative at its boundaries; seeded continuous components keep results repeatable. Output schema `rig-motion.camera-offsets.v1` includes sampled frame/time/location and local camera-aligned XYZ `rotation_euler_rad`. Apply values to a separate neutral SHAKE control using the actual Action/slot API in [automation](automation.md). Do not repeatedly add offsets to already processed values.

Linear keys preserve the sampled path but limit subframe blur accuracy. Analytic evaluation or denser sampling in an adapted Blender tool may be needed. The helper does not open Blender, build a rig, or certify camera quality. Reported peaks are sampled peaks rather than continuous extrema.

## Whip pan and snap as a complete path

Choose two stable framing endpoints and a reason to transfer attention. Establish the departure and give the destination a readable hold. Build preparation/lead → fast middle → braking/small overshoot → hold. Show contact before the whip or after stopping when it cannot read during travel. A whip should not conceal an unresolved transition.

Build world path/rotation without blur and inspect flips/axis. Then use [motion blur](https://docs.blender.org/manual/en/latest/render/eevee/render_settings/motion_blur.html) for the actual renderer/version and adjust shutter through a rendered fragment. Viewport blur can differ from final output. Camera whoosh is an editorial accent, distinct from a physical object's sound. A snap can be rotation or short dolly; motivated framing determines whether lens changes help.

## Review

Compare neutral view, base camera, and camera with impulse. Preserve contact/reaction, needed limbs within edges, purposeful horizon/roll, stable attention focus, cut continuity, and return to zero. Halving shake should leave the action forceful. If force disappears, revise mechanics/rhythm before camera accents.
