# Quality review and completion criteria

Search: silhouette, contact, loop, velocity, export, preview, score, acceptance.

## Review from cause to presentation

1. Intention/staging: the beat reads without audio/effects and the decisive gesture is visible.
2. Pose/mechanics: support, force direction, and sequence are clear; rigidity matches the contract.
3. Timing/spacing: useful contrast, sharp action, finite purposeful settling.
4. Contact/geometry: support, grips, and impacts agree; intentional clipping is documented.
5. Arcs/overlap: no accidental hooks/flips; secondary action follows its cause.
6. Loops/transitions: repeats plus entry/exit; matching endpoints do not establish velocity continuity.
7. Export/runtime: names, rest pose, units, duration, channels, retriggers, blending, and access.
8. Presentation: camera, light, texture fidelity, frame rate, and stable moving imagery.

Runtime checks do not apply to film-only work. A narrow curve repair needs relevant checks and assurance that its surrounding beat remains intact.

## Viewing set

Review normal speed for rhythm/weight, slow motion for contact/arc causes, keys and midpoints for transfer, neutral front/side/three-quarter views for hidden geometry, and final camera for staging. Inspect at least three loop repeats. Gameplay needs real transitions, speeds, and repeated events rather than only editor playback.

A small contact sheet can show preparation, drive/takeoff, extreme/apex, impact, absorption, and settle. It proves poses, not timing. A JSON report is not visual verification.

## Author rating scale

| Score | Observable result |
|---|---|
| 0 | Unchecked or essential function broken |
| 1 | Action is guessable but obvious defects interfere |
| 2 | Working base with defects visible at normal speed |
| 3 | Convincing and clean in its intended context |
| 4 | Expressive; nuance supports intention and required technical checks pass |

Rate intention, mechanics, timing, contact, arcs, style consistency, and delivery. Do not average a critical defect away with attractive lighting. Wrong mapping, a failed required endpoint, or a broken trigger blocks readiness of the relevant product.

## Quantitative diagnostics

`motion_audit.py` normalizes by explicit height `H`. Starting author thresholds are loop point `.002H`, contact drift `.005H`, endpoint angle `.5 degrees`, and linear seam-velocity mismatch `.05H/s`. These are diagnostic defaults, not Roblox/Minecraft limits or artistic certification.

Choose rigid-stance tolerance according to contact marker and visible scale. Measure moving support in support-local space; reconstruct world travel for in-place walking. Intentional foot roll needs actual rotating contact geometry or separate windows rather than treating the foot center as fixed.

Compare quaternion orientation through angular distance. Euler 360 and 0 can share orientation but differ in path. Finite-difference seam velocity is approximate: coarse sampling can flag a smooth curve incorrectly. Increase density before changing motion.

## Acceptance for a scene from a sketch

Each gate requires evidence, not an intention to check later. Use only affected criteria for small edits.

| Pass | Evidence | Readiness blocker |
|---|---|---|
| Reference/character | Observations separated from reconstruction; acting follows supplied/delegated cards | Silently invented unknown personality or contradictory story |
| Neutral motion | Initiative, support, contact, and consequences read without camera accents/FX/audio | Sliding, unexplained reactions, invisible impact, prohibited joints |
| Base camera/edit | Important silhouettes and events remain visible; screen direction is clear | Cropped contact, accidental axis reversal, missing partner |
| Camera impulse | A cause, readable peak, and return to the base | Per-frame noise, endless vibration, excess roll/near clipping |
| VFX render | Correct birth, anchor, plane, lifetime, seed, and readable layering | Hidden mechanics, alpha/sorting artifacts, flicker, stale/missing cache |
| SFX with picture | Contact transient, material, perspective, and contrast read | Missing media, desync, clipped sum, excessive tails, unknown source |
| Delivery/runtime | Reopened source with dependencies; required runtime replay | Broken media, required untested transfer/trigger, unusable external assets |

Professional presentation requires reliable mechanics, characteristic acting, clear staging, and coherent effects/audio. Glow cannot repair support, and loudness does not establish weight. Keep artistic review distinct from helper reports.

## Comparisons for a complete shot

1. Neutral normal-speed playback: who wants what and why the partner moves.
2. Final camera without shake/FX: framing, axis, contacts, reactions.
3. Same camera with accents/VFX, muted: effects support the event.
4. Rendered video with mix: whoosh, impact, aftermath, contrast, perspective.
5. Reopened source and render samples, including nonconsecutive frames for baked simulations.

Use actual viewport/render/video and available listening. Contact sheets prove poses; JSON proves limited numeric properties; neither proves final timing or timbre. Inspect before contact, contact, first reaction, and settling plus continuous playback. Check encoded audio itself; metering and listening provide different evidence.

Retiming or camera-target changes update linked cues and affected reviews. Seek regressions in meaning, clipping, synchronization, and expiry. Do not repeat unrelated runtime testing without a reason.

## Result package

Deliver what the task needs: native source, clip/range/FPS metadata, preview, and required engine export/runtime evidence. Describe a specific test, such as three retriggers after returning to idle, instead of claiming perfection.

For a remaining material defect, report frame/time, cause, and next repair. Without application access, static checks remain static. Never label a dummy GIF as a preview of an actual animation.
