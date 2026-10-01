# SFX: what to find, where to get it, when to place it, and how to mix

Search: SFX, sound design, Foley, whoosh, impact, sync, audio, license, mix.

Sound communicates cause, material, mass, space, and personality. Work spotting → sources/layers → processing → mix. Avoid one cinematic boom on every movement. Choose actual sources and listen through an available tool. Filenames and waveforms do not establish suitable timbre.

## 1. Spotting and sound roles

From real playback, build an [event sheet](../assets/event-sheet.md): marker ID, actor, material, distance, drive/contact/aftermath, desired feeling, and accent level. Use a shared timeline origin/FPS. Music does not replace causal effects.

| Event | Source role | Placement | Avoid |
|---|---|---|---|
| Step/support transfer | Surface, footwear, mass | Actual weight acceptance; separate skid | Footsteps for airborne swings |
| Cloth/armor/prop motion | Soft friction and small detail | Visible movement, quieter than main cues | Noise for every bone key |
| Fast swing/pass | Appropriately sized air whoosh | Drive/near pass, ending near contact | Whoosh throughout a hold or after stopping |
| Body contact | Short impact and chosen body layer | Main transient at contact | Metal ring without metal; loudness as mass |
| Metal/stone | Hard transient and material resonance | Contact plus controlled tail | Full tails over the next important beat |
| Ground fall | Body/surface, cloth, debris | Landing, followed by later debris contacts | Every layer starting before contact |
| Charge/release | Tonal/noise envelope and release accent | Buildup → release → hit | Sustain after the source ends |
| Camera whip/edit | Editorial whoosh/sting | Attention transfer/transition | Confusing it with a physical object's sound |
| Environment | Restrained ambience/room tone | Connects shots and space | Unexplained silence on every cut |

Small movement may need no sound. A quieter interval before the main event adds contrast without requiring a riser. Precise characters can use economical accents; impulsive ones reveal motion/recovery; heavy ones communicate body, inertia, and surface rather than pitch-down alone.

## 2. Sources and permission

Start with available project media and original Foley, then external sources. Record author, title/ID, direct URL, license/download date, local path, processing, and attribution. Purchasing libraries/subscriptions needs user authorization. Do not extract effects from films/games/music without established permission.

| Source | Useful for | Inspect |
|---|---|---|
| Original Foley | Unique cloth, surface, prop behavior | Actual recording provenance, clean signal, varied takes |
| [Kenney](https://kenney.nl/assets) | Simple stylized/game sources | [Support](https://kenney.nl/support) describes CC0 asset pages; retain the specific pack license |
| [Freesound](https://freesound.org/) | Materials, Foley, ambience, variation | [FAQ](https://freesound.org/help/faq/) explains per-sound licenses; CC0, BY, and BY-NC differ |
| [Sonniss GDC](https://sonniss.com/gameaudiogdc/) | Varied professional source recordings | [Bundle EULA](https://sonniss.com/gdc-bundle-license/) applicable to that download; raw redistribution can be restricted |
| User-owned purchased library | Specific quality/category | Actual license, seat, access, and project-transfer rights |
| Available sound generation tool | Difficult-to-record original form | Service conditions, real output, availability, and listening |

[CC0](https://creativecommons.org/publicdomain/zero/1.0/) and [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) differ: BY requires attribution, license link, and modification notice. BY-NC is not a default choice for commercial work. When use is uncertain, choose an appropriate alternative. Free/royalty-free does not mean unconditional. Processing does not make you the recording's author.

The research-date Sonniss bundle EULA v2 applies to downloads from August 27, 2026 and restricts standalone SFX/library distribution, including redesigned sounds, and AI training/enhancement. Do not bundle these sources into a public skill/template. Earlier downloads need their corresponding license. Recheck terms when selecting actual assets. This instructional text grants no rights to someone else's recordings. Inspect Freesound provenance as well as the license badge.

### Search for a concrete sound

Combine **material + action + perspective + quality**: `cloth movement dry close`, `body fall dirt single`, `metal scrape short`, `air whoosh fast close`, `stone debris small drop`, `room tone small interior`. Search properties rather than only epic adjectives. When you need an isolated layer, filter music/noise, long reverb, and premixed impacts. Listen to onset, body, and tail, then compare in picture context.

Choose a small relevant set rather than downloading huge libraries for a five-second shot. Three to six variants can help repeated events. License/URL records must concern the selected asset, not just a homepage. Use authorized account access when required; do not claim an unperformed download.

## 3. Original Foley and synthesis

Use fabric for cloth, appropriate surface/footwear for steps, and soft objects/pillows plus safe props for impacts. Record several variations, clean head/tail, and room tone with level headroom. Close microphones reveal detail but can add breath, wind, or handling noise. Clean recording precedes shaping.

Author synthesis recipes:

- Whoosh: noise → frequency filter → amplitude envelope, with filter movement suggesting a pass.
- Impact body: short low tone/noise with fast pitch/amplitude decay, plus a separate material transient.
- Charge: rising tone/noise layers that stop or change at release.

These are approaches, not universal plugin settings. For available AI audio tools, specify material, action, intensity, duration, dry/room character, single/variations, and required tail. Save generation provenance/terms, listen for artifacts, and fit the transient to the marker. A promise of generation without a file is not a result.

## 4. Layer by function

[BOOM's trailer discussion](https://www.boomlibrary.com/blog/top-tips-for-trailer-sound-design/) describes functional separation across transient, frequency, sustain, and tail. For a short block fight, adapt to a main onset, useful body/material, and required aftermath. This does not require purchasing tools or always using four layers.

1. Transient: contact and sharpness; begin with this alone on the marker.
2. Body/material: mass and texture. Retain perceived weight on ordinary speakers, not only subwoofers.
3. Detail: cloth, grit, metal rattle from the actual object, quieter and/or later.
4. Space/tail: environment, distance, consequences, preferably controllable separately.

Listen solo and combined. Similar transients can create a flam; overlapping low end can add or cancel. Adjust offsets, gain, and EQ by role rather than maximizing every source. Small purposeful pitch/volume variation should not change character mass between steps.

## 5. Processing and perspective

A starting chain is trim/clean → pitch/time changes → EQ → envelope/gain → space → mix peaks. Adapt it to the source and retain originals/working copies.

- [Filter Curve EQ](https://manual.audacityteam.org/man/filter_curve_eq.html): support a role and remove interfering regions; avoid identical filters on every source.
- [Envelope Tool](https://manual.audacityteam.org/man/envelope_tool.html): shape level over time; inspect version-specific interaction with processing and listen to the exported result.
- [Reverb](https://manual.audacityteam.org/man/reverb.html): control room, wet/dry, gain, and sufficient tail range. Avoid accidental tail truncation.

Distance changes detail and direct/room balance, not just volume. Panning usually follows screen position/movement unless a subjective perspective is chosen. Offscreen sound can prepare an entrance when the scene explains it. Preserve ambience/room continuity through cuts.

For slow motion, choose a sound perspective deliberately; stretching selected layers does not require slowing music or the entire mix. [BOOM on sound, voice, and music](https://www.boomlibrary.com/blog/sound-design-voice-over-and-music-for-film-trailers/) supports joint organization/ducking where actual meaningful layers compete. These source analyses rely on limited accessible excerpts, as recorded in the source ledger.

## 6. Precise synchronization and Blender VSE

Place picture/native scene and [sound strips](https://docs.blender.org/manual/en/latest/video_editing/edit/montage/strips/sound.html) on a shared range. VSE audio channels sum; lower tracks do not conceal upper ones. Use waveforms, animated volume, and fades where useful. External audio remains a dependency to test after reopening.

Align the **audible main transient**, not necessarily file start. If onset is tau seconds into the source, place it at `contact_time-tau`, accounting for trim, stretch, and rate. Whoosh follows drive before contact; impact aligns with contact; debris/tails have separate cues. DAW editing can be sample-accurate. Where a tool rounds placement to frames, account for up to half-frame error and inspect the render.

Effective FPS and audio sample rate differ. Relabeling sample rate does not correctly retime sound. For video, 48 kHz PCM WAV is a convenient author working default when no specification exists, not a universal Roblox/Minecraft rule. Save native audio session/source, required stems, and actual [mixdown](https://docs.blender.org/manual/en/latest/render/output/audio/introduction.html).

## 7. Mix and listen

Organize primary action, Foley/detail, sweeteners, ambience, and optional music/dialogue. Give attention to the meaningful event and preserve quiet contrast. Leave headroom and measure the summed mix; individually clean tracks can clip together. Do not normalize every cue to the same peak.

Without a delivery specification, measured true peak below −1 dBTP is a useful starting margin, not a platform loudness mandate. Do not claim LUFS/true peak from waveform appearance or intuition. Sample peak and inter-sample true peak differ. Inspect encoded output because encoding can alter peaks/sync.

Listen with final normal-speed picture through available headphones/speakers and mono/downmix if available. Check main contact, believable material/distance, unobtrusive repetition, and tails that leave the next beat clear. Report unavailable listening honestly; metadata/waveforms provide technical evidence only.

## Gameplay requires a separate contract

A film's baked stereo mix is not gameplay spatial audio. Wire runtime markers/locators and test playback speed, interruption, retriggering, listener distance, and simultaneous effects. Roblox [animation events](https://create.roblox.com/docs/animation/events) provide `GetMarkerReachedSignal`; actual sound/effect integration still needs implementation/testing. Cosmetic markers do not replace authoritative hit validation.

For Minecraft, verify the actual version/runtime's audio/particle aliases, events, placement, and repeated triggers. Blender audio export does not create sound definitions. Distribute recipes/manifests in the skill; keep restricted library media in authorized projects under their licenses.

## Delivery

Provide native project and permitted dependencies, final mix, needed stems, cue sheet, source/attribution ledger, and an actual viewed/listened preview. If standalone source transfer is restricted, deliver a permitted result or replacement and identify the dependency. Do not describe a mix as professionally verified without listening with the final picture.
