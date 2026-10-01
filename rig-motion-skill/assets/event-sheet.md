# Shared events: movement, camera, VFX, and SFX

Use one timeline origin. `t=0` at `frame_start`; Blender effective FPS is `fps/fps_base`; `frame=frame_start+t*effective_FPS`. Fractional times/frames depend on tool support. Record rounding explicitly. Retiming updates all linked cues.

| Project field | Value |
|---|---|
| Scene/shot, frame_start/end, FPS/fps_base | |
| Timeline origin and height H units | |
| Rig, axes, supports | |
| Primary/secondary accents | |

| Event ID | Actual cause/actor/contact | t / frame | Camera cue | VFX anchor/direction/lifetime/seed | SFX asset ID/transient/gain/tail | Verified |
|---|---|---|---|---|---|---|
| prepare_01 | Decision/support transfer | | Base follow or static | Usually none | Meaningful cloth/breath | |
| drive_01 | Limb acceleration | | Keep contact framed | Evaluated-tip trail | Speed/distance-related whoosh | |
| impact_01 | A contacts B | | Brief recoil/shake | Contact-born directed burst | Main transient at contact | |
| land_01 | B contacts floor | | Restrained ground impulse | Surface dust/debris | Body fall, later debris | |
| settle_01 | Recovery/new decision | | Return to base | Expiring tails | Tail, ambience, cloth | |

## Sound and media ledger

| Asset ID | Author/title/direct URL or original recording | License date/version | Permitted use/attribution | Local source | Processing/output | Standalone transfer allowed? |
|---|---|---|---|---|---|---|
| | | | | | | |

This is a working template, not proof of contacts, listening, or rights. Enter actual status after verification.
