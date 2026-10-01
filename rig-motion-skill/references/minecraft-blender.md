# Minecraft characters and cinematic shots in Blender

Search: rigid, bending, skin UV, texels, GLB, MCprep, Mineways, camera, face.

## Choose the rig profile

Choose vanilla-like rigid, cinematic bending, or a limited hybrid. Film elbows/knees/faces may expand expression. Returning to gameplay requires a specific runtime and geometry/bone checks; mesh deformation or shape keys do not automatically become Bedrock cubes or Java animation.

Before using a downloaded rig, check author, permission, Blender version, controls, skin format, IK/FK, extreme poses, and UV preservation. A familiar old rig is not automatically compatible with a new Blender. Use actual author sources rather than arbitrary mirrors in old tutorials.

For a custom rigid rig, bind whole visible parts to their intended bones/objects without distributed stretching weights. Weight-1 groups or separate object parenting can preserve rigidity; automatic weights may deform neighboring cubes. Choose according to export requirements.

For bending, test large elbow/knee angles for gaps, pinched faces, stretched skin, and volume loss. Smooth shading cannot fix deformation topology. Match subdivisions/topology to the rig and style.

## Skin and materials

Inspect the actual layout: classic/slim and legacy/current UV layouts differ. Steve/Alex naming alone does not prove mapping. Check face, head sides/back, both arms, torso, legs, and outer layers with an asymmetric test skin. Do not mirror UVs automatically for an asymmetric skin.

Keep pixel art readable at camera distance. Use appropriate nearest/Closest image sampling, then inspect motion shimmer. Also check texel scale, mipmapping/AA, and output resolution. Assign color spaces by data type; normal/roughness maps are not skin color.

Outer layers need suitable offset and alpha handling. Check z-fighting, transparent interiors, and shadows. Do not enable alpha blending on every material. Render-method UI changes across Blender versions; inspect the installed version.

The [Minecraft Style Guide](https://blockbench.net/wiki/guides/minecraft-style-guide/) supports simple shapes, texture detail, and consistent pixels. An explicitly chosen cinematic deviation is valid; realistic lighting does not require a rounded character.

## Transfer from Blockbench

Initially test GLB/glTF for animated Blender transfer. The [3D Export guide](https://blockbench.net/wiki/guides/export-formats/) discusses format differences, including incompatibility between its described ASCII FBX and Blender's standard binary-FBX importer. Verify current versions rather than universally recommending FBX.

After import, inspect hierarchy, pivots, axes, duration, endpoints, texture/alpha, and intermediate poses. GLB does not carry gameplay state machines, live queries, or Blender-style control rigs. Create convenient authoring controls separately if required; do not promise unchanged quads or expressions.

Choose a supported converter/runtime early for an in-game destination. OBJ is useful for static worlds/meshes, not clips. A plugin's metadata-bearing OBJ workflow is a separate verified exception.

## World and props

[Mineways](https://www.realtimerendering.com/erich/minecraft/public/mineways/) exports selected world regions; [MCprep](https://github.com/Moo-Ack-Productions/MCprep) assists Blender workflows. Neither is mandatory for a simple set. Bound world complexity by camera/action first, then inspect scale, materials, foliage/glass transparency, normals, and prop origins.

Record sword/tool grip orientation and hand-relative placement. Visible floors/ledges and contact references must agree. A block strike needs matched contact, reaction, and effect at impact.

## Staging and mechanics

Rigid movement uses torso/head and whole-limb arcs. Bending can amplify compression but cannot replace a coherent trajectory. Acceleration, takeoff, apex, and landing explain a jump more than the mere presence of knees.

A square head can communicate clear attention turns. Add facial detail where close-ups need it. For small framing, silhouette and head direction may outperform elaborate lip sync. Match face assets to texture style/detail level.

Choose camera before full polish so props do not obscure gestures. Preserve geography and readable important poses. Test shake, DOF, and blur after mechanics; narrow focus or strong blur can erase pixel art and contact.

Maintain coherent lighting/color management and compare moving frames. Verify motion on a simple set before adding expensive world detail. The older BPS series provides a useful [production structure](tutorial-analysis.md), while its Blender 2.7 UI is not a current checklist.
