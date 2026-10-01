# A professional VFX pass: build effects in Blender

Search: VFX, FX, impact, trail, shockwave, sparks, dust, debris, Geometry Nodes, emission.

By default, **build the required effects yourself in Blender** using geometry, curves, Geometry Nodes, materials, Grease Pencil, and compositing. Use references for form/rhythm. External effect packs need a user request or a concrete justified dependency. All numerical timings below are author starting recipes, not platform standards.

## Design before nodes

Establish cause, space, and lifecycle: source → buildup/birth → main impulse → development → decay. For contact, record point, normal, relative-velocity direction, and [event ID](../assets/event-sheet.md). Express scale relative to H and framing, velocity in scene units/second, and duration in seconds. Distinguish Blender gravity axes from game coordinates.

Choose the role: indicate direction, clarify contact, reveal material/energy, explain consequence, or guide attention. Reduce an effect when pose, light, or another effect already serves that role. The main impulse must preserve contact silhouette and the first reaction pose.

| Style | Graphic language | Avoid accidental mixing |
|---|---|---|
| Rigid/vanilla Minecraft | Square particles, limited palette, simple clusters | Dense realistic smoke or photographic glare without a chosen deviation |
| Stylized R6 | Readable ribbons/rings, short graphic flashes | Huge luminous blobs at every touch |
| Cinematic Minecraft | Environment-related material, dust/debris | Unrelated photoreal effects on flat block shading |
| Graphic/anime influence | Asymmetric bursts, 2D accents, rhythmic holds | Blur that erases decisive graphic poses |

These are artistic options. Preserve the user's choice and [motion style](style-playbook.md).

## Scene organization and dependencies

Use an `FX_<shot>` collection, separate objects/materials/node groups, and event-linked controls with editable names/ranges. Separate source geometry, instance source, and final controller. Before scripting, inspect actual Blender version, context, node types, sockets, and enums rather than localized display names.

A burst usually stays at its birth contact or follows the contacted material. Already-born dust should not follow the moving foot wholesale. Charge/grip may be actor-local until release; projectile/trail becomes world-space. Check parent inverse, conversion, and scale application. Stable particle IDs/seeds prevent changing color/size on every evaluation.

Start with inexpensive controlled meshes. Use simulation when history/collisions solve a visible problem. A [Simulation Zone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/simulation/simulation_zone.html) retains state and uses Delta Time. [Baking](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/baking.html) requires a saved blend file; caches are not universal cross-version exports. Test baked nonconsecutive frames for out-of-order rendering.

## Recipe 1: short contact flash / graphic burst

Use for a featured physical contact or stylized accent, not automatically every light touch.

1. Place an Empty at evaluated contact. Choose the physical plane or an intentional camera-facing layer. Test the latter across frames/views to avoid a sticker covering both actors.
2. Build a filled radial star mesh with alternating long/short vertices and several tapered triangles. Direct asymmetry through force rather than uniformly radiating everything.
3. Try size `0.1–0.25H`. Keep it absent before the marker, expand over roughly `0.02–0.06 s`, and shrink/fade over `0.08–0.18 s`. Scale and opacity/emission can differ. Verify sampling when the impulse is shorter than an output frame.
4. Begin with an opaque silhouette, then a simple palette and controlled emission/alpha using supported renderer settings. Check backfaces and sorting explicitly.
5. An optional brief separate light can illuminate the actor. Emissive surfaces do not guarantee neighboring illumination in every renderer; glow and lighting are different.

Check visible contact before/after, a flash shorter than the reaction, and a clean last opacity frame. A localized weaker burst often reads better than a full-screen white flash unless the story asks for exposure emphasis.

## Recipe 2: expanding ring / shockwave

Use for surface impact, energy release, or a stylized heavy landing.

1. Build an annulus: outer and inner rings joined by faces in the contact plane. Use fewer segments or a square contour for a block style. Align normal with the propagation plane.
2. Animate radius and width independently: `inner=max(0,outer-width)`. Uniform torus scaling also expands thickness and often communicates the wrong development.
3. Try radius expanding to `0.4–0.8H` over `0.15–0.35 s`, width reducing from `0.04H` toward `0.005H`, and fading opacity/emission. Start at contact and offset slightly above the surface to avoid z-fighting.
4. Add purposeful nonuniformity, gaps, or material masks. Ground dust follows ground; energy can use another plane. A water-like circle on dry floor needs an intentional style reason.

Check near clipping, occlusion by obstacles, and agreement with reaction energy/distance rather than material brightness alone.

## Recipe 3: limb/sword ribbon trail

Use during a short high-speed phase when direction needs emphasis. Constant idle trails remove contrast.

1. Place a marker at the real limb/weapon endpoint. Sample **evaluated world positions**, including parents and constraints. Resample Curve does not record moving-object history.
2. For an authored one-shot, build a world-space curve from those samples and reveal a time-limited segment whose newest point meets the current tip. Interactive history needs a Simulation Zone with positions/ages and cache/bake.
3. [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_mesh.html) needs a profile for a tube. For ribbons, use a thin profile or paired edges `p_i ± width_i*b_i` with a stable transverse direction. Camera-facing ribbons need large-turn twist/flip tests.
4. Taper width/opacity by age. A blade ribbon can sample two real blade points rather than derive width from an arbitrary camera vector.
5. Try a tail of `0.06–0.18 s`; extinguish it during holds. Retiming requires resampling history/age, not just changing visibility endpoints.

Check attachment to the source, no delayed chasing, history that stays in world space, and an arc consistent with partner contact. Topology generated anew per frame can produce motion-blur artifacts; test subframes.

## Recipe 4: directed sparks without expensive simulation

Match material: metal, stone, or energy may justify sparks; body impacts do not always produce them.

1. Try 8–30 points for a small stylized burst with stable IDs/seed. Assign contact birth position, initial velocity in a controlled cone around force/normal, lifespan, and size.
2. Use a stateless ballistic path `p=p0+v0*tau+0.5*g*tau²`, where `tau=max(0,t-birth)` and g is a scene vector. Retain initial values per ID. This formula does not provide drag or collision; those need an explicit solver/integration.
3. Instance small tapered meshes/cubes. Align length to current velocity and vary size/brightness by age rather than orienting every instance identically toward camera.
4. Begin with a short dense cluster, then dispersed sparks and fading residue. Remove each when age reaches lifespan. Establish geometry before glow.

Check repeatable rerenders, correct birth time, and expiry. Simple-floor bounce can be implemented separately; complex collisions need actual solver/playback evidence.

## Recipe 5: block debris

1. Match fragments to the broken material through shape/texture/color. Contact without destruction does not necessarily require debris.
2. For a small controlled shot, use ballistic paths and differing rotation axes/speeds. For collisions/stacking, test rigid-body scale/shapes and bake. Retain seed and initial state.
3. Birth occurs in the destruction region with force-directed velocity. Larger pieces remain readable longer and create later impacts; small pieces can expire sooner. Avoid a uniform confetti sphere.
4. Inspect floor contact, initial overlaps, and visible versus collision shapes from side views. Do not make all large fragments vanish together without an intentional graphic treatment.

## Recipe 6: dust/smoke at the appropriate cost

**Inexpensive stylized approach:** low-poly clusters or planes born from the surface, with fast outward expansion, smaller rise, modest growth, fading opacity, and decelerating motion. Preserve actor silhouette. For cards, build an original Noise/Color Ramp mask with radial falloff, test alpha in a real render, and avoid facing-camera flips during pans.

**Volume approach:** a bounded container with [volume materials](https://docs.blender.org/manual/en/latest/render/materials/components/volume.html), spatial density mask, and animated development. Density/scale affect clarity and render cost; high-frequency noise may flicker. Physical smoke history needs an actual fluid solver/cache rather than presenting animated noise as fluid simulation.

Work shape/trajectory → density/opacity → color/light → breakup. Judge contrast on the final background. Identical dense smoke on dry ground, metal, and water fails to explain material. Try `0.25–0.8 s` for short contact dust, then adapt to scale and air.

## Recipe 7: charge → projectile → hit

Use three independent controlled objects/events. Actor-local charge communicates intention; release transfers the projectile to world space; hit births a separate burst/aftermath. Avoid doubled parent transforms. Establish trajectory/contact before emission. Projectile light follows its source, trails store world history, and the projectile ends according to the scene at hit.

Build a mesh core with thin curves/rings or Grease Pencil accents. Limit noise displacement to a readable silhouette. Uneven charge development can reveal personality and decision. Charge sustain sound should stop at release unless continuity is intentional. Game export requires runtime assets rather than Blender compositing.

## Grease Pencil accents

[Grease Pencil](https://docs.blender.org/manual/en/latest/grease_pencil/index.html) supports 2D animation in 3D. Use selective arcs, impact shapes, and action lines with explicit placement plane/lifetime. Check occlusion/camera. Old APIs may differ from the installed version: inspect current types/functions before creating strokes through Python.

## Materials, lighting, and compositing

Establish geometry/opacity, then emission/light, then [Glare](https://docs.blender.org/manual/en/latest/compositing/types/filter/glare.html). Glare creates halos from highlights; tune threshold/strength to preserve detail. When historical EEVEE Bloom controls are absent, inspect current compositor/renderer instead of guessing a checkbox.

Maintain chosen color management and palette. High emission can whiten the intended color. Inspect final view transform, alpha edges, premultiplication, and backgrounds. Compositor glow is a screen effect; object lights illuminate surfaces. Separate effect masks/passes when useful without assuming identical renderer APIs.

## What reaches gameplay

Collections, Geometry Nodes simulations, volumes, and compositing do not automatically become Roblox/Minecraft effects. For film, retain them in source/render. For games, create appropriate textures, flipbooks, or supported geometry and wire the real runtime mechanism.

[Roblox particles](https://create.roblox.com/docs/effects/particle-emitters) and [animation events](https://create.roblox.com/docs/animation/events) support presentation assets/cues. Check quality/device performance, repeated triggering/interruption, and asset access. Minecraft needs actual Bedrock/Java particle/audio and locator/alias contracts. Blockbench preview does not establish runtime success.

## Learning progression

Teach short exercises when asked to teach; apply the relevant technique directly during production. Do not require a course before creating the requested shot.

| Stage | Build | Evidence |
|---|---|---|
| Lifecycle | Burst without glow/textures | Distinct birth/peak/expiry, readable contact |
| Space | Ring on a tilted surface | Correct plane, independent radius/width, no z-fighting |
| History | One fast tip trail | World history, fading tail, stable subframes |
| IDs/time | Seeded sparks at two FPS values | Seconds-based paths/lifetimes, stable identity |
| Material | Dust/debris from two surfaces | Distinct material rather than identical confetti |
| Render | Light, alpha, and glare added individually | Useful changes without washed-out skin |
| Integration | Contact, camera impulse, SFX cue | Shared marker, neutral-readable reaction, retiming sync |
| Reopen/bake | Reopen and render out of order | Dependencies/caches and reproducible output |

[Advanced analysis](advanced-tutorial-analysis.md) records primary learning sources and limits. The [physics article](https://code.blender.org/2026/07/geometry-nodes-physics/) discusses an experimental Blender 5.2 hair/cloth framework; planned future solvers must not be assumed implemented. Inspect [demo files](https://www.blender.org/download/demo-files/) separately with their licenses/minimum versions.

## Acceptance

Verify cause/time, material-related scale, finite life, correct anchor/plane/direction, stationary world history, visible face/contact, coherent form/palette, and varied accents. Test IDs/seeds, alpha, normals, occlusion, near clip, and reopened caches in actual renders. Watch before/during/after the event and a continuous normal-speed fragment. Neutral mechanics must also work.

Report source controls, event IDs, actual render checks, and limitations. A node tree alone does not establish a completed professional VFX pass.
