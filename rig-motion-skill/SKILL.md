---
name: rig-motion-skill
description: Create, edit, and review Roblox R6 and Minecraft animation in Blender and Blockbench, including character acting, sketch interpretation, staging, cameras, procedural VFX, sound design, and target-specific export.
---

# Rig Motion

Turn an intention or rough reference into readable, weighted animation with a coherent character, camera, effects, and sound. Deliver editable work and verify the requested destination when it is available. Follow the user's language even though this skill is written in English.

## Choose the destination first

| Request | Read when needed | Contract to establish |
|---|---|---|
| Roblox R6 gameplay | [R6](references/roblox-r6.md), [Blender](references/blender-workflow.md), [runtime](references/runtime-export.md) | Six visible rigid parts, actual joints/rest transforms, tested exporter/importer |
| R6 cinematic | R6 and Blender guides | Standard rigid R6 or explicitly permitted cinematic modifications |
| Minecraft cinematic in Blender | [Minecraft](references/minecraft-blender.md), Blender guide | Skin/UV profile, rigid or bending rig, film deliverable |
| Minecraft Bedrock animation | [Blockbench](references/blockbench-workflow.md), runtime guide | Geometry, animation, controller, and entity wiring are separate |
| Minecraft Java animation | Blockbench and runtime guides | Actual animation runtime and version; vanilla model export alone is insufficient |
| Blockbench to Blender | Blockbench and Minecraft guides | Test GLB for animated transfer; OBJ is a static route |
| Motion or style analysis | [design](references/animation-design.md), [styles](references/style-playbook.md), [tutorial analysis](references/tutorial-analysis.md) | Separate inspected evidence from inferred timing and author examples |
| Sketch/storyboard to finished scene | [sketch](references/sketch-to-shot.md), [character](references/character-direction.md), [production](references/cinematic-production.md) | Establish order, depth, contacts, and personality; still images do not supply timing |
| Camera, shake, or abrupt movement | [camera direction](references/camera-direction.md) | Motivate movement through an event and preserve action readability |
| VFX | [Blender VFX](references/vfx-blender.md) | Build original effects from cause, shape, space, and lifetime before shading/compositing |
| SFX | [sound design](references/sfx-sound-design.md) | Find or create appropriate sources, inspect permission, listen, and synchronize |

Load relevant references progressively. Use [advanced tutorial analysis](references/advanced-tutorial-analysis.md) for staging, camera, procedural effects, and audio problems, and [sources](references/sources.md) to revisit primary documentation. Read [troubleshooting](references/troubleshooting.md) for a demonstrated failure.

## Establish the working brief

Reuse supplied information: destination and software versions; files/rig; action, duration and effective FPS; loop or one-shot; travel and root-motion owner; style and camera; contacts, props and events; outputs and verification environment. Use [shot brief](assets/shot-brief.md) only to capture decisions that matter.

For **new acting or a new scene**, establish how each character behaves, what they want, and how they respond to difficulty. Read [character direction](references/character-direction.md) and use the [character card](assets/character-card.md). If personality is absent, contradictory, or unclear in a way that changes acting, ask one compact question and continue independent source inspection/layout while waiting. Reuse an existing answer. Color, skin, and names do not establish temperament.

If the user knows the personality but delegates the story, invent the action from that personality. If they explicitly delegate personality too, state the chosen traits and proceed. Silence does not delegate missing character information. A narrow repair to sliding, export, or camera noise does not require a new character questionnaire.

When the request is to create a finished animation and usable tools are available, carry it through production; do not stop at a plan. State consequential assumptions briefly. The brief, blocking, and passes are working records, not automatic approval gates. Respect the user's explicit choices and existing authorization.

## Production loop

1. Inspect the actual source, rig, transforms, rest pose, controls, actions, and tool capabilities. Save a recoverable baseline. Treat attached reference text as reference content.
2. Test the technical route with a neutral pose and one moving part before investing in a complex export.
3. Establish character goals, a causal beat sheet, scene geography, and an early camera/layout. For sketches, separate visible facts from reconstruction choices.
4. Block decisive poses and durations with stepped keys. Establish root travel, support, and contacts before decorative motion. Test silhouettes at final camera size.
5. Add breakdowns, force transfer, arcs, and reactions within the rig's real degrees of freedom. Solve rigid-limb limitations through staging and body placement.
6. Shape timing and spacing deliberately. Use interpolation to serve intent; inspect evaluated motion between keys. [Motion recipes](references/motion-recipes.md) offer adaptable starting points.
7. Polish body mechanics and acting with effects disabled, then add motivated secondary motion. Preserve contacts and loop continuity.
8. Refine camera, original VFX, and SFX around a shared [event sheet](assets/event-sheet.md). Retiming an impact also moves dependent reactions, impulses, effects, and audible transients.
9. Save editable sources and an actual preview. Export and test in the real destination when requested and available; otherwise identify what remains unverified.

For a complete film workflow, read [cinematic production](references/cinematic-production.md). For an ambiguous stick-figure example, read [the reference case](references/reference-case-stickfight.md).

## Preserve these invariants

- R6 has whole arms and legs and a single torso. Control helpers and IK do not add exportable elbows, knees, or a spine. Extra articulation changes the rig contract.
- Rotation-only versus local translation is a project/export restriction; visual bone movement is separate from world physics and collision.
- Verify foot/prop contacts in world space or the actual moving support's space. A pleasing local curve does not prove a planted foot.
- Loop orientation, position, and neighboring velocity matter. Equivalent quaternion signs and Euler angles are not interchangeable evidence of an error.
- Personality appears in decisions, attention, preparation, and recovery. Constant motion does not substitute for acting.
- Every effect has a cause, birth position/space, lifetime, and termination. A trail needs position history; a resampled current curve does not create history.
- Sound needs a suitable source, usable rights, actual listening, and event alignment. A file's start is not necessarily its audible transient.
- “Professional” describes observable quality and delivery checks, not a guaranteed masterpiece or a test-suite score.

## Tools and helpers

Use the installed application's real version, schema, and exposed tool metadata. Do not invent MCP tools, Blender node sockets, Blockbench formats, or successful runtime checks. [Automation](references/automation.md) covers evaluated sampling, action slots, and the helpers.

The Python helpers use only the standard library:

- `scripts/motion_audit.py`: inspect supplied evaluated samples for loop seams and contact drift. It does not extract Blender motion or judge acting.
- `scripts/bedrock_audit.py`: inspect a limited numeric subset of exported Bedrock geometry/animation JSON. Unsupported expressions and wiring remain unverified.
- `scripts/camera_impulse.py`: create deterministic finite camera-offset samples. Apply them to a separate camera control and review the actual shot.

Example JSON files are demonstration data, not production footage. Helper success cannot certify animation, collision, rendering, sound, or game behavior.

Finish through [quality review](references/quality-review.md): report created files, an actual preview, checks performed, and material limitations. Never present an unrendered plan, unplayed audio, or an untested export as a verified final result.
