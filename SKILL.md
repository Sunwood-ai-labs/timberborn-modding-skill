---
name: timberborn-modding
description: Create and debug Timberborn mods with an emphasis on new building assets, GLB/FBX/OBJ import, .timbermesh export, Blueprint wiring, TemplateCollection registration, and Unity AssetBundle material workflows. Use when Codex needs to turn 3D assets into placeable Timberborn buildings, choose between built-in materials and custom textures, troubleshoot Timbermesh or MaterialCollection or AssetBundle loading errors, or automate Blender and Unity CLI steps.
---

# Timberborn Modding

## Start Here

- Read [references/workflow.md](./references/workflow.md) for the standard route selection and end-to-end flow.
- Read [references/troubleshooting.md](./references/troubleshooting.md) when errors or broken visuals appear.
- Read [references/example-route-a.md](./references/example-route-a.md) when the user wants a Timberborn-style built-in material result.
- Read [references/example-route-b.md](./references/example-route-b.md) when the user wants to preserve custom textures with AssetBundles.
- If the local machine already has a Timberborn research workspace, example mods, or a cloned official modding wiki, inspect only the files needed for the current task.

## Build Context Before Acting

- Identify the source asset path, target mod path, faction, building category, footprint, and whether the user wants Timberborn-style materials or the original textured look.
- Inspect the mod's `manifest.json`, building Blueprint, `TemplateCollection`, localization, and latest game error logs before patching.
- If the task touches custom textures or materials, inspect the Unity mod project and built `AssetBundles` output, not only the game mod folder.

## Decide the Route Early

- Use Route A when Timberborn built-in materials are sufficient and the mesh can look correct without custom textures.
- Use Route B when the source `GLB` is texture-baked, the user wants the original look, or built-in material remapping already produced garbled output.
- Switch from Route A to Route B quickly when the mesh shape is simple but the visual detail lives mostly in the texture.

Read [references/workflow.md](./references/workflow.md) for the full decision tree.

## Execute the Standard Flow

1. Scaffold from `Example building` unless the existing mod already provides a better base.
2. Normalize names across Blueprint, model, icon, material, and bundle assets.
3. Export `.timbermesh` from Blender CLI with [assets/export_glb_to_timbermesh_template.py](./assets/export_glb_to_timbermesh_template.py) as the starting point.
4. Update the building Blueprint, `TemplateCollection`, and localization.
5. For Route B, create a Unity `Material`, register it in `MaterialCollection`, and build the AssetBundle.
6. Fully restart Timberborn after material or bundle changes.
7. Verify with file existence, build logs, and latest runtime logs before claiming success.

## Follow These Guardrails

- Keep `.mat` and `.png` basenames distinct. Use `MyHouseBase.mat` with `MyHouseBaseTexture.png`, not `MyHouseBase.png`.
- Put bundle-loadable assets under `Assets/Mods/<mod>/AssetBundles/Resources/...`.
- Prefer lower-case normalized keys in `MaterialCollection`, for example `materials/myhouse/myhousebase`.
- Do not claim that `.timbermesh` alone preserves the original `GLB` texture look.
- Use a single finished model first. Reuse a stock `ConstructionBase...` unfinished model unless the user explicitly wants staged construction visuals.
- Fully restart the game after custom material changes because Timberborn may hold stale repositories across a live session.

## Resolve Local Tool Paths Before Scripting

- Discover the local Blender CLI path before writing automation against it.
- Discover the local Unity CLI path before writing AssetBundle build commands.
- On Windows, common defaults often resemble `C:\Program Files\Blender Foundation\Blender <version>\blender.exe` and `C:\Program Files\Unity\Hub\Editor\<version>\Editor\Unity.exe`, but do not assume those exact paths exist.

## Verify Before Closing the Task

- Confirm the exact files created or updated.
- Confirm whether the route was Route A or Route B.
- For Route B, confirm that built bundle output exists and that the material registration path matches the runtime-loadable key.
- Summarize what was actually tested versus what remains unverified.

## Resources

- [references/workflow.md](./references/workflow.md): end-to-end flow, route split, commands, and deliverables
- [references/troubleshooting.md](./references/troubleshooting.md): common Timberborn asset and material failures
- [references/example-route-a.md](./references/example-route-a.md): minimal built-in material example
- [references/example-route-b.md](./references/example-route-b.md): custom texture and AssetBundle example
- [assets/export_glb_to_timbermesh_template.py](./assets/export_glb_to_timbermesh_template.py): Blender CLI export starter
- [assets/building_blueprint.template.json](./assets/building_blueprint.template.json): minimal building Blueprint skeleton
- [assets/material_collection.template.json](./assets/material_collection.template.json): Route B material registration skeleton
- [assets/template_collection_buildings.template.json](./assets/template_collection_buildings.template.json): building registration skeleton
