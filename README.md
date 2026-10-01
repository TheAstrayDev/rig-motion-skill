# Rig Motion Skill

An English-language agent skill for **Roblox R6 animation in Blender** and **Minecraft animation in Blender and Blockbench**. It connects character acting, rough-reference interpretation, body mechanics, staging, cameras, original procedural VFX, sound design, and target-specific delivery.

Maintained by [TheAstrayDev](https://github.com/TheAstrayDev). The repository name and installed skill name are both **`rig-motion-skill`**. Invoke it as **`$rig-motion-skill`**. This is the sole maintained edition; there is no separate `-en` package.

## Why this exists

A request such as “animate this drawing professionally” leaves many decisions unstated: who the characters are, which pose comes first, where force transfers, whether a rigid leg can reach, what the camera must show, and which sound should happen at contact. Merely adding smooth curves, glow, and loud impacts does not resolve those decisions.

This skill gives an agent a production method for making them coherently. It helps the agent interpret a simple sketch, distinguish evidence from assumptions, build action from personality, establish a technical route early, and carry the scene through editable sources, previews, effects, audio, and relevant export checks.

It is an **instruction/resource package for an agent**, not a Blender addon, a new model, or model-weight training. Loading it does not install Blender, Blockbench, Roblox Studio, Minecraft, rigs, plugins, or media libraries. It does not grant tools that the agent lacks. With application access, the agent should execute the requested work; without it, the agent must identify the limitation and deliver the useful work it can actually complete.

## Supported work

| Route | What the skill helps create | Important boundary |
|---|---|---|
| Roblox R6 gameplay | Rigid clips, contacts, props, loops, exporter probes, Studio verification | Actual six-part rig/joint mapping; no invented knees or elbows |
| R6 cinematic in Blender | Acting/action shots, cameras, lighting, effects, soundtrack | Extra articulation requires an explicit cinematic rig choice |
| Minecraft cinematic in Blender | Rigid or permitted bending animation, skin/UV handling, world/props | Film deformation does not automatically become game animation |
| Minecraft Bedrock in Blockbench | Bone clips, geometry/export checks, entity/controller integration | Geometry, clips, aliases, controllers, and triggers are distinct |
| Minecraft Java | Animation for a chosen mod/runtime, including version-specific GeckoLib guidance | Vanilla item/block JSON is not a general bone-animation runtime |
| Blockbench → Blender | A tested animated GLB/glTF transfer | OBJ is static; runtime expressions/state machines do not transfer automatically |
| Review/repair | Sliding, weak impact, loops, unwanted spins, camera noise, export failures | Scope the repair to the demonstrated problem |

The written guidance is in English. The agent should still communicate in the user's language unless asked otherwise.

## Install

### Through Codex's skill installer

Ask Codex:

```text
$skill-installer Install rig-motion-skill from
https://github.com/TheAstrayDev/rig-motion-skill/tree/main/rig-motion-skill
```

The repository root contains the README and maintenance files. **The installable folder is the nested `rig-motion-skill/` directory**, which contains `SKILL.md`.

If running the bundled installer directly, its arguments are:

```text
python <path-to-skill-installer>/scripts/install-skill-from-github.py --repo TheAstrayDev/rig-motion-skill --path rig-motion-skill
```

The default destination is `$CODEX_HOME/skills/rig-motion-skill`, or `~/.codex/skills/rig-motion-skill` when CODEX_HOME is unset. The installer refuses an existing destination. The installed skill becomes available on the next turn.

### Manual installation on Windows

Run from a directory where you want the repository checkout:

```powershell
git clone https://github.com/TheAstrayDev/rig-motion-skill.git
$rigMotionHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$rigMotionSource = Join-Path (Get-Location) 'rig-motion-skill/rig-motion-skill'
$rigMotionDestination = Join-Path $rigMotionHome 'skills/rig-motion-skill'
if (Test-Path -LiteralPath $rigMotionDestination) { throw 'Skill already exists. Back up and review it before updating.' }
New-Item -ItemType Directory -Path (Split-Path $rigMotionDestination) -Force | Out-Null
Copy-Item -LiteralPath $rigMotionSource -Destination $rigMotionDestination -Recurse
```

For other agent systems, load `rig-motion-skill/SKILL.md` according to that system's instruction-loading mechanism and retain its relative folders. Codex-specific UI metadata is optional outside Codex. No universal cross-agent compatibility is claimed.

For updates, preserve local changes, review the new revision, and replace the installed folder intentionally. Do not install another English copy under an `-en` name. If migrating from the earlier `rig-motion` skill, back it up outside active skill directories and use `rig-motion-skill` as the maintained installation.

## Give the agent a useful request

Attach the drawing/video/project when relevant. Specify the destination, character personalities, major action/outcome, style, and output expectations. Supply duration/FPS/versions when important. You can delegate story, timing, camera, and effect choices instead of directing every keyframe.

For new acting, the skill requires a practical character description: **how they behave, what they want, and how they respond when things go wrong**. If this is missing or ambiguous, the agent asks a compact question while continuing independent inspection/layout. It does not infer personality from stick-figure color. If you know the personality but not the story, it builds the story from that personality. If you explicitly delegate personality too, it states its choices and proceeds.

### One sketch to an R6 cinematic

```text
Use $rig-motion-skill. Turn the attached rough drawing into a complete
Blender cinematic with rigid Roblox R6 characters. A is calm, precise,
and trying to stop the confrontation. B is proud and impulsive, wants
the initiative, and becomes frustrated after mistakes.

I do not know the exact choreography. Reconstruct a coherent sequence
from the drawing and those personalities. Choose the duration, staging,
camera, restrained shake, original Blender VFX, and suitable SFX.
Create the editable .blend, actual preview with sound, and cue/source
records. Verify mechanics without effects before the final pass.
```

### Minecraft action in Blender

```text
Use $rig-motion-skill with the attached Minecraft rig and skin.
Create a short jump across a gap, a difficult landing, and a relieved
final reaction. The character is cautious but determined. Keep the
limbs rigid, preserve pixel textures, and choose the camera and timing.
Build the dust in Blender and design surface-appropriate landing sound.
Deliver source, preview, and the actual checks performed.
```

### Bedrock clip and runtime wiring

```text
Use $rig-motion-skill. In this Blockbench Bedrock project, create a
one-shot startled reaction for a shy creature that briefly recoils,
checks the threat, and returns to idle. Use the project's existing
bone names and Minecraft version. Export the clip and wire a repeatable
controller trigger. Test repeated entry and early interruption when
the runtime is available; identify any checks you cannot perform.
```

### Focused repair

```text
Use $rig-motion-skill. Fix the planted-foot sliding and loop hitch in
this R6 walk. Preserve the character's acting and clip duration.
Inspect evaluated world contacts and compare the exported result.
```

### Fully delegated characters

```text
Use $rig-motion-skill to turn this sketch into a Minecraft Blender film.
Choose the personalities and a short story yourself, state the choices,
and complete the scene with original VFX and appropriate sound.
```

Explicit delegation lets the agent choose missing creative details. It does not authorize unrelated publishing, purchases, or external messaging.

## What the agent should do

1. Inspect the actual reference/project and separate visible facts from reconstruction.
2. Establish destination, rig limits, character goals, and a minimal technical probe.
3. Build causal beats, geography, early camera, and a stepped animatic.
4. Solve root travel, support, grips, impacts, force transfer, and partner reactions.
5. Refine timing, spacing, arcs, and personality before decorative motion.
6. Refine motivated camera movement and finite impulses around shared event markers.
7. Build original Blender effects with correct birth space, lifetime, seeds, and caches.
8. Select/create sound sources, record provenance, align audible transients, and mix.
9. Review neutral movement, camera/effects, picture with sound, and reopened dependencies.
10. Deliver real files/previews and verify requested runtime behavior where available.

The passes are working steps, not automatic approval stops. A significant retime updates reactions, camera impulses, VFX, and SFX together. A film-only task does not require game export.

## Camera, VFX, and sound coverage

**Camera:** attention, shot purpose, interaction axis/screen direction, focal length versus perspective, framing, DOF, static/follow/dolly/orbit choices, whips, snaps, recoil, and controlled shake. Shake is a caused finite event with return to the base, measured in seconds and scene-relative units. No preset is described as universally perfect.

**Original Blender VFX:** contact burst, independent-width shockwave ring, evaluated-history ribbon trail, seeded sparks, block debris, stylized/volumetric dust, and charge → projectile → hit. It covers geometry, lifecycle, coordinate spaces, stable identities, materials, compositing, caching, and render checks. Effects must preserve readable acting/contact.

**SFX:** spotting, material/action/perspective searches, project libraries, original Foley/synthesis, Kenney/Freesound/Sonniss source selection, per-asset permission, layering, EQ/envelopes/reverb, VSE placement, audible-onset alignment, mix headroom, listening, stems, and game-versus-film audio. No third-party sample library is bundled.

## A rough-reference example

![User-supplied stick-figure reference](rig-motion-skill/assets/reference-stickfight.png)

This is **input**, not an animation result. The [case study](rig-motion-skill/references/reference-case-stickfight.md) records what is visible, what remains ambiguous, and one explicitly labeled author reconstruction. It does not claim the drawing uniquely specifies a named combo, timing, or personality.

## Package map

The installable package contains 21 reference guides, three editable Markdown templates, four JSON examples, one reference image, three Python helpers, two test modules, and skill/UI metadata.

| Area | Guides |
|---|---|
| Motion and style | [Design](rig-motion-skill/references/animation-design.md), [styles](rig-motion-skill/references/style-playbook.md), [recipes](rig-motion-skill/references/motion-recipes.md) |
| Acting and references | [Character](rig-motion-skill/references/character-direction.md), [sketch reconstruction](rig-motion-skill/references/sketch-to-shot.md), [case study](rig-motion-skill/references/reference-case-stickfight.md) |
| Production | [Full workflow](rig-motion-skill/references/cinematic-production.md), [camera](rig-motion-skill/references/camera-direction.md), [VFX](rig-motion-skill/references/vfx-blender.md), [SFX](rig-motion-skill/references/sfx-sound-design.md) |
| Applications | [Blender](rig-motion-skill/references/blender-workflow.md), [R6](rig-motion-skill/references/roblox-r6.md), [Minecraft/Blender](rig-motion-skill/references/minecraft-blender.md), [Blockbench](rig-motion-skill/references/blockbench-workflow.md) |
| Transfer and checks | [Runtime](rig-motion-skill/references/runtime-export.md), [quality](rig-motion-skill/references/quality-review.md), [troubleshooting](rig-motion-skill/references/troubleshooting.md), [automation](rig-motion-skill/references/automation.md) |
| Research | [Motion tutorials](rig-motion-skill/references/tutorial-analysis.md), [advanced analysis](rig-motion-skill/references/advanced-tutorial-analysis.md), [71-source ledger](rig-motion-skill/references/sources.md) |
| Working templates | [Shot brief](rig-motion-skill/assets/shot-brief.md), [character card](rig-motion-skill/assets/character-card.md), [event/media sheet](rig-motion-skill/assets/event-sheet.md) |

The agent reads relevant references progressively, rather than loading all guides for every small task.

## Python helpers

Python 3.10+; standard library only. No `pip install` is required for these helpers. Run the following from the **repository root**:

```powershell
python -B rig-motion-skill/scripts/motion_audit.py rig-motion-skill/assets/samples.example.json
python -B rig-motion-skill/scripts/bedrock_audit.py rig-motion-skill/assets/probe.animation.json --geometry rig-motion-skill/assets/probe.geo.json
python -B rig-motion-skill/scripts/camera_impulse.py rig-motion-skill/assets/camera-shake.example.json --output camera-offsets.json
```

| Helper | Purpose | What it cannot prove |
|---|---|---|
| `motion_audit.py` | Endpoints, sampled linear seam velocity, sampled contact drift/path | Acting, collision, unsampled motion, rendering; it does not extract Blender transforms |
| `bedrock_audit.py` | A limited numeric subset of exported Bedrock geometry/animation | Full schema compliance, expressions, aliases/controllers, game behavior |
| `camera_impulse.py` | Deterministic finite local camera-offset samples | A camera rig, Blender application, subframe accuracy, artistic quality |

The two audits return **0** for supported checks passing, **1** for detected defects, **2** for input/CLI error, and **3** for required review. Read `unverified` when code 3 appears. The camera generator returns **0** for created data and **2** for an error. All reject overwriting their own input through `--output`.

Schema identifiers remain `rig-motion.samples.v1`, `rig-motion.camera-impulse.v1`, and `rig-motion.camera-offsets.v1` for data compatibility. They are not alternate installed skill names. Example inputs are synthetic demonstrations, not footage or a complete resource pack. See [automation contracts](rig-motion-skill/references/automation.md) before supplying production samples.

## Validation and evidence

From the repository root:

```powershell
python -B tools/validate_package.py
python -B -m unittest discover -s rig-motion-skill/scripts/tests -v
```

The package checker inspects local links, English-text consistency, metadata, source IDs, JSON, and Python syntax. The helper suite has **53 tests** covering numerical behavior, invalid inputs, uncertainty reporting, deterministic impulses, and input-file preservation. GitHub Actions runs package checks and tests on Python 3.10 and 3.14.

These checks validate packaging and helpers. They do **not** demonstrate that an agent has produced professional animation, that a Blender render is artifact-free, that sound has been heard, or that an export has played in Roblox/Minecraft. Those require actual project evidence.

The research ledger records 71 primary-source entries as of October 1, 2026. Full embedded videos, paid lessons, and restricted production files were not inspected; some sources were available only as descriptions or search excerpts. Recipes, numerical starting ranges, style profiles, and rating scales are author synthesis. Production must recheck version-sensitive documentation and the specific media license.

## Results and feedback

**Animation results are pending user-provided testing.** No finished-shot gallery or measured model-performance benchmark is claimed yet. This release does not include a fabricated `.blend`, runtime replay, or demonstration movie.

Useful future reports include the original prompt/reference, character description, software/addon/runtime versions, rig profile, source/export, normal-speed preview, checks actually performed, and the most visible remaining defect. A before/after comparison of neutral mechanics and final camera/effects/audio is particularly helpful.

Share project/media files only when you can redistribute them. Improvements should follow observed failures: missing contacts, ambiguous acting, hidden impact, stale effects, wrong sound perspective, or broken runtime triggers. Add focused guidance and reproducible cases rather than accumulating universal rules without evidence.

## Asset and repository licensing

This repository includes instructional synthesis, helper code, synthetic examples, and the supplied reference drawing. Linked manuals, rigs, libraries, demo scenes, and recordings retain their respective terms; a source link grants no asset rights. No repository-wide license has been selected. Restricted third-party SFX and production assets are not bundled.
