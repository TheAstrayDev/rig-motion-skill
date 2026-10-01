# Runtime transfer and playback verification

Search: Animator, priority, group, Bedrock aliases, controller, triggers, GeckoLib5 paths.

## Roblox R6

Complete the [R6 probe](roblox-r6.md), then import production onto the same destination rig. Compare matching seconds, including intermediate poses. Agree on range, FPS, and sampling.

[Animation Editor](https://create.roblox.com/docs/animation/editor) covers local saving, loop endpoints, priority, and publishing. Match loop endpoint poses; when replacing default clips, follow the current workflow, including an ending `End` when required. A locally saved sequence and published asset are distinct. For group-owned experiences, verify animation creator/access.

[Using animations](https://create.roblox.com/docs/animation/using) describes `Animator:LoadAnimation()` and `AnimationTrack:Play()`. Inspect the existing Animator, character lifecycle, and execution context rather than creating duplicates. Verify current replication rules for the actual player/NPC workflow.

Check intentional priority/weight against default Animate; non-looping one-shots and valid retriggers; agreement between visual root motion and controller/collision; entry/exit at real blend durations; prop position; and impact markers against contact. Damage/hit validation belongs to gameplay logic. A marker alone does not prove a hit.

[Marketplace animation packs](https://create.roblox.com/docs/avatar/animation-packs) have separate standard-R15 requirements. Do not silently turn a requested R6 experience clip into avatar-pack publishing or apply pack requirements indiscriminately.

## Minecraft Bedrock

Verify bone → geometry, short alias → full animation/controller ID, and `scripts.animate` → alias. Merely placing a file in `animations` does not start playback. [Animations Overview](https://learn.microsoft.com/en-us/minecraft/creator/documents/animations/animationsoverview?view=minecraft-bedrock-stable) explains channel application; simultaneous clips may combine/change transforms.

This is a **fragment** of `minecraft:client_entity.description`, to integrate with the project's materials, textures, geometry, and render controllers:

```json
{
  "animations": {
    "probe": "animation.rigmotion.probe"
  },
  "scripts": {
    "animate": ["probe"]
  }
}
```

It is not a standalone resource pack. The example `probe.geo.json` and `probe.animation.json` test channel transfer; entity definition, wiring, and textures are separate project work.

Geometry commonly uses model units at 1/16 block; animation rotation uses degrees. Probe axes/transforms instead of copying Blender radians. Animation, geometry, and controller schemas can have different `format_version` values; these are not the Minecraft release number.

A repeated one-shot needs appropriate state logic. A conditional blend expression does not necessarily restart the clip at zero for every event. The [Bedrock tutorial](https://blockbench.net/wiki/guides/bedrock-modeling/) discusses this trap. Use a controller for required re-entry/retriggering.

The [controller reference](https://learn.microsoft.com/en-us/minecraft/creator/documents/animations/animationcontroller?view=minecraft-bedrock-stable) defines states, ordered transitions, and `blend_transition`. Establish entry, exit, and interruption conditions before choosing transition smoothness. One successful event does not establish correct reset behavior.

Test spawn/load, idle → walk → stop, two or three repeated events, interruption before completion, leaving the condition, reload, and look-at/locomotion overlays. Inspect content logs. Visual bone displacement does not automatically change collision shape.

## Minecraft Java and GeckoLib

Vanilla Java block/item JSON is not an arbitrary bone-animation destination. Identify the project's actual runtime. CEM, EMF, OptiFine, and other routes need their own documentation; Minecraft context does not justify substituting GeckoLib JSON.

The [GeckoLib plugin guide](https://wiki.geckolib.com/docs/geckolib5/making-models/blockbench-plugin-usage/) describes its project type. [Export](https://wiki.geckolib.com/docs/geckolib5/making-models/exporting-the-files/) separates geometry and clips. Conversion requires inspecting properties/bones and does not create runtime code.

[GeckoLib 5 asset locations](https://wiki.geckolib.com/docs/geckolib5/making-models/placing-the-files/) include:

```text
assets/<modid>/geckolib/models/
assets/<modid>/geckolib/animations/
assets/<modid>/textures/
```

Do not apply these paths to GeckoLib 4 without checking that major's documentation. Verify constructors/imports before transferring older Java examples into version 5.

In [GeckoLib 5 controllers](https://wiki.geckolib.com/docs/geckolib5/concepts/animation/controller/overview/), one controller owns one current playback; multiple controllers permit independent actions but require resolving bone conflicts. Use the project's trigger workflow for appropriate one-shots rather than an eternal attack loop.

Verify asset paths/IDs, GeoModel references, clip names, controller registration, triggers, reset/re-entry, transitions, overlays, and movement speed. Synchronize visual triggers with gameplay events; distinguish game ticks from JSON seconds.

## If the runtime is unavailable

Deliver editable source, export, static audit, and editor preview. Name the missing check precisely, such as import and repeated triggering on Minecraft X/GeckoLib Y. Do not claim game-ready status before that check. A film-only request does not need an engine gate.
