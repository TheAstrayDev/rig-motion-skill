# Sources and research boundaries

Research date: **October 1, 2026**. The 71 entries below are primary sources. Text access means page content was inspected; a video description does not mean footage was watched. Search-excerpt access is identified separately. Phase maps, thresholds, quality ratings, camera/VFX/SFX recipes, and style profiles are author synthesis rather than platform requirements.

Blender, Blockbench, addons, and Minecraft evolve. Match installed versions to documentation during production. `latest` is a moving URL; GeckoLib URLs identify a major version. A verified current project schema/API takes precedence over a general guide. This is a record of the original research, not a claim that every source was revalidated during translation.

## Roblox and Blender bridge — 11

| ID | Source | Access and purpose |
|---|---|---|
| R01 | [Animation Editor](https://create.roblox.com/docs/animation/editor) | Text: loops, priority, local saving/publishing |
| R02 | [Use animations](https://create.roblox.com/docs/animation/using) | Text: Animator playback and default animations |
| R03 | [Animator](https://create.roblox.com/docs/reference/engine/classes/Animator) | Text: methods and playback contract |
| R04 | [Pose](https://create.roblox.com/docs/reference/engine/classes/Pose/MaskWeight) | Text/search excerpt: mapping/Transform; URL includes a deprecated property, class description supplies context |
| R05 | [Motor6D](https://create.roblox.com/docs/reference/engine/classes/Motor6D) | Text: joint offsets, timing, avatar-joint changes |
| R06 | [Animation packs](https://create.roblox.com/docs/avatar/animation-packs) | Text: separate Marketplace R15 workflow |
| R07 | [RBXMonkey/Cautioned repository](https://github.com/Cautioned/Blender-Animations-Plugin) | README: paired tools, synchronization, rig selection |
| R08 | [RBXMonkey releases](https://github.com/Cautioned/Blender-Animations-Plugin/releases) | Text: time ranges, slots, easing fixes, import evolution |
| R09 | [Den_S Creator Store](https://create.roblox.com/store/asset/716953901/Blender-rig-exporteranimation-importer) | Text/search result: historical tool; DevForum thread blocked by a JavaScript challenge |
| R10 | [Animation events](https://create.roblox.com/docs/animation/events) | Text: markers, GetMarkerReachedSignal, presentation sync |
| R11 | [Particle emitters](https://create.roblox.com/docs/effects/particle-emitters) | Text: attachments, particles/flipbooks, quality/performance |

Do not combine a modern bridge with legacy OBJ/clipboard steps indiscriminately or infer R6 compatibility from R15 documentation. These sources do not establish a successful round-trip of a user's particular rig.

## Blender manual — 18

Some pages were unavailable through the web reader and were retrieved directly through HTTPS during original research. The distributed skill includes links and synthesis rather than copied manuals or raw research captures.

| ID | Source | Inspected topic |
|---|---|---|
| B01 | [Actions](https://docs.blender.org/manual/en/latest/animation/actions.html) | Text: slots, channels, ranges, cyclic intent |
| B02 | [Graph Editor editing](https://docs.blender.org/manual/en/latest/editors/graph_editor/fcurves/editing.html) | Text: curve editing |
| B03 | [Child Of](https://docs.blender.org/manual/en/latest/animation/constraints/relationship/child_of.html) | Text: inverse, influence, parent relations |
| B04 | [Rotation modes](https://docs.blender.org/manual/en/latest/advanced/appendices/rotations.html) | Text: Euler, quaternion, axis-angle |
| B05 | [NLA editing / Bake Action](https://docs.blender.org/manual/en/latest/editors/nla/editing/strip.html) | Text: evaluated motion, Visual Keying, bake options |
| B06 | [FBX](https://docs.blender.org/manual/en/latest/files/import_export/fbx.html) | Text: format support; inspect installed exporter settings |
| B07 | [IK solver](https://docs.blender.org/manual/en/latest/animation/constraints/tracking/ik_solver.html) | Text: chain length and constraints |
| B08 | [Cameras](https://docs.blender.org/manual/en/latest/render/cameras.html) | HTTPS text: lens, sensor, projection, focus, composition |
| B09 | [F-Curve modifiers](https://docs.blender.org/manual/en/latest/editors/graph_editor/fcurves/modifiers.html) | HTTPS text: Noise, phase/scale, blending, bias |
| B10 | [Glare](https://docs.blender.org/manual/en/latest/compositing/types/filter/glare.html) | HTTPS text: highlights, modes, threshold/strength |
| B11 | [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_mesh.html) | HTTPS text: profiles/conversion, not temporal trail recording |
| B12 | [Simulation Zone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/simulation/simulation_zone.html) | HTTPS text: state, Delta Time, cache, nonsequential rendering |
| B13 | [Geometry Nodes baking](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/baking.html) | HTTPS text: saving, bake, version limits |
| B14 | [Volumes](https://docs.blender.org/manual/en/latest/render/materials/components/volume.html) | HTTPS text: density, shading, mesh/world, renderer limits |
| B15 | [Grease Pencil](https://docs.blender.org/manual/en/latest/grease_pencil/index.html) | HTTPS text: purpose/workflows; exact bpy stroke API not tested |
| B16 | [EEVEE Motion Blur](https://docs.blender.org/manual/en/latest/render/eevee/render_settings/motion_blur.html) | HTTPS text: shutter, viewport/final distinction, sampling |
| B17 | [Sound Strip](https://docs.blender.org/manual/en/latest/video_editing/edit/montage/strips/sound.html) | HTTPS text: dependencies, layers, waveform, volume keys |
| B18 | [Audio Rendering](https://docs.blender.org/manual/en/latest/render/output/audio/introduction.html) | HTTPS text: mixdown, channels, rate |

## Blockbench — 7

| ID | Source | Inspected topic |
|---|---|---|
| C01 | [Formats](https://blockbench.net/wiki/blockbench/formats/) | Text: project-format capabilities |
| C02 | [Overview & Tips](https://blockbench.net/wiki/guides/blockbench-overview-tips/) | Text: hierarchy, pivots, channels, interface |
| C03 | [Minecraft Style Guide](https://blockbench.net/wiki/guides/minecraft-style-guide/) | Text: simplicity, UV/texel consistency, vanilla aesthetic |
| C04 | [Bedrock Modeling and Animation](https://blockbench.net/wiki/guides/bedrock-modeling/) | Text: clips/controllers/retrigger trap; duplicated Microsoft tutorial not counted twice |
| C05 | [Animation Expressions](https://blockbench.net/wiki/guides/animation-expressions/) | Text: Molang, editor syntax, export/bake limits |
| C06 | [3D Export](https://blockbench.net/wiki/guides/export-formats/) | Text: GLB/OBJ/FBX transfer |
| C07 | [.bbmodel format](https://blockbench.net/wiki/docs/bbmodel/) | Text: format evolution and split groups/outliner in 5.0 |

## Minecraft Bedrock — 2

| ID | Source | Inspected topic |
|---|---|---|
| M01 | [Animations Overview](https://learn.microsoft.com/en-us/minecraft/creator/documents/animations/animationsoverview?view=minecraft-bedrock-stable) | Text: aliases, scripts.animate, channels, degrees/order |
| M02 | [Animation Controllers Reference](https://learn.microsoft.com/en-us/minecraft/creator/documents/animations/animationcontroller?view=minecraft-bedrock-stable) | Text: states, transitions, blending, model units |

## GeckoLib 5 — 4

| ID | Source | Inspected topic |
|---|---|---|
| G01 | [Blockbench plugin usage](https://wiki.geckolib.com/docs/geckolib5/making-models/blockbench-plugin-usage/) | Text: project type and conversion |
| G02 | [Exporting files](https://wiki.geckolib.com/docs/geckolib5/making-models/exporting-the-files/) | Text: geometry/animation export |
| G03 | [Placing files](https://wiki.geckolib.com/docs/geckolib5/making-models/placing-the-files/) | Text: major-5 model/animation paths |
| G04 | [Controller overview](https://wiki.geckolib.com/docs/geckolib5/concepts/animation/controller/overview/) | Text: registration, overlays, triggers, speed |

Recheck before transferring major-5 information into major 4. JSON preview does not establish valid Java code/asset registration.

## Artistic lessons and class pages — 9

| ID | Primary material | Access scope |
|---|---|---|
| A01 | [Jason Martinsen: human walk](https://www.animationmentor.com/blog/tutorial-animating-human-walk-cycle/) | Written discussion: poses, weight, overlap, in-place |
| A02 | [Jason Martinsen: timing and spacing](https://www.animationmentor.com/blog/tutorial-animate-with-timing-and-spacing-in-mind/) | Written discussion: holds and contrast |
| A03 | [Anthony Wong: overlap/pendulum](https://www.animationmentor.com/blog/tutorial-overlap-pendulum-motion-animation/) | Written discussion: base, drag, offsets |
| A04 | [Jason Martinsen: jump and land](https://www.animationmentor.com/blog/tutorial-animate-a-jump-and-land/) | Written discussion: takeoff, arc, landing |
| A05 | [Anticipation](https://www.animationmentor.com/blog/anticipation-the-12-basic-principles-of-animation/) | Text: preparation and action clarity |
| A06 | [Wayne Gilbert: body mechanics](https://www.animationmentor.com/blog/animation-tips-tricks-what-makes-or-breaks-a-good-body-mechanics-shot/) | Text: intention and forces |
| A07 | [John Nguyen: Staging](https://www.animationmentor.com/blog/staging-the-12-basic-principles-of-animation/) | Reader text: attention, halves/thirds, screen direction |
| A08 | [Zachary Rahman: Green Screen Reference](https://www.animationmentor.com/blog/tutorial-green-screen-video-reference/) | Reader text: layout/framing; Maya, not bpy |
| A09 | [Ere Santos: Cameras and Cinematography](https://www.animationmentor.com/blog/cameras-and-cinematography-for-animators/) | Page/workshop description; video not watched, specific camera presets not attributed |

Embedded videos were not watched. Adaptations, rig differences, and exercises are in [tutorial analysis](tutorial-analysis.md).

## Minecraft production and training — 5

| ID | Source | Access and purpose |
|---|---|---|
| P01 | [Mineways](https://www.realtimerendering.com/erich/minecraft/public/mineways/) | Text: world export |
| P02 | [MCprep](https://github.com/Moo-Ack-Productions/MCprep) | Repository text: Minecraft/Blender workflow; verify versions before installation |
| P03 | [Squared Media/BPS: Getting Started](https://www.youtube.com/watch?v=Ik7jPH2sZNk) | Published description: Blender 2.7/world import |
| P04 | [Squared Media/BPS: Scene Setup](https://www.youtube.com/watch?v=0-gA7O6SCdw) | Published description: set, rig, skin, props |
| P05 | [Blender Studio Fundamentals update](https://studio.blender.org/blog/blender-fundamentals-training-update-3d-animation/) | Announcement text: basic exercises, not completed course |

## Blender Studio / procedural production — 5

| ID | Source | Access and limits |
|---|---|---|
| T01 | [Simon Thommes: Simulation Nodes 3.6](https://studio.blender.org/training/geometry-nodes-from-scratch/how-to-use-the-new-simulation-nodes-in-blender-36/) | HTTPS page and author reply on seconds, initial state, loops; video not watched |
| T02 | [Official Demo Files](https://www.blender.org/download/demo-files/) | HTTPS catalog: puff/particle/fracture examples, licenses/versions; blend files not downloaded/inspected |
| T03 | [Impulse Purchase production file](https://studio.blender.org/blog/impulse-purchase-production-file/) | HTTPS article: procedural setup, camera, simulation, VSE; restricted file not inspected |
| T04 | [Beau Gerbrands: Bcon 2023 Interstitials](https://studio.blender.org/blog/creating-the-bcon-2023-festival-interstitials/) | HTTPS text: drawing, blocking, bake/art direction, audio iteration; audiovisual examples not inspected |
| T05 | [Jacques Lucke: Geometry Nodes Physics](https://code.blender.org/2026/07/geometry-nodes-physics/) | HTTPS text: experimental 5.2 LTS hair/cloth and XPBD; roadmap is not an implemented API |

## Sound: sources, conditions, tools — 10

| ID | Source | Access and purpose |
|---|---|---|
| S01 | [Freesound FAQ](https://freesound.org/help/faq/) | Text: per-asset licenses, attribution, provenance, formats/descriptions |
| S02 | [Kenney Support](https://kenney.nl/support) | Text: CC0 game assets; verify the selected pack |
| S03 | [Sonniss GDC Bundle EULA](https://sonniss.com/gdc-bundle-license/) | Text: v2 from 2026-08-27, media sync, redistribution/AI limits, download-date version |
| S04 | [Creative Commons CC0](https://creativecommons.org/publicdomain/zero/1.0/) | Deed text: public-domain dedication and rights limits |
| S05 | [Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Deed text: attribution, license, change indication |
| S06 | [Audacity Envelope Tool](https://manual.audacityteam.org/man/envelope_tool.html) | HTTPS text: amplitude envelope and processing interaction |
| S07 | [Audacity Filter Curve EQ](https://manual.audacityteam.org/man/filter_curve_eq.html) | HTTPS text: frequency shaping and clip processing |
| S08 | [Audacity Reverb](https://manual.audacityteam.org/man/reverb.html) | HTTPS text: wet/dry, room/tail, gain, tail range |
| S09 | [BOOM: Top Tips for Trailer Sound Design](https://www.boomlibrary.com/blog/top-tips-for-trailer-sound-design/) | Meaningful search excerpts: roles/contrast; full reader retrieval failed |
| S10 | [BOOM: Sound, Voice Over and Music](https://www.boomlibrary.com/blog/sound-design-voice-over-and-music-for-film-trailers/) | Meaningful search excerpts: layering/EQ/mix; audio examples not heard |

No third-party SFX samples or their rights are distributed here. Verify current conditions for the actual selected source/use. Adaptation exercises are in [advanced analysis](advanced-tutorial-analysis.md).

## Research again when needed

Investigate the specific question when a rig/plugin version is supplied, a style video is attached, a Java runtime differs, a probe mismatches, project format changes, or exact UI/compatibility matters. Also verify renderer/node APIs, cache portability, event wiring, delivery loudness, and selected audio licenses. The catalog's date alone does not establish current compatibility.
