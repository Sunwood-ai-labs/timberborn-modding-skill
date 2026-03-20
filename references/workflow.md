# Workflow

## Route Selection

### Use Route A

- Use Timberborn built-in materials.
- Skip Unity AssetBundles.
- Prefer this when geometry and material assignment can carry the look.

Typical signs:

- The model is already split into meaningful surfaces such as wood, plaster, and roof pieces.
- The desired result is "Timberborn-style" rather than "match the original render exactly."

### Use Route B

- Preserve custom textures.
- Add a Unity `Material`.
- Build an AssetBundle.

Typical signs:

- The source `GLB` is texture-baked.
- The mesh is simple but the look depends on the image.
- Route A produced garbled or noisy visuals.

## Standard Inputs to Gather

- Source asset path
- Target mod path
- Unity project path if Route B is likely
- Faction, category, footprint, and desired display name
- Whether the user wants the original look or a Timberborn-style reinterpretation

## Standard File Layout

### Built mod

Minimum:

- `manifest.json`
- `Buildings/.../MyHouse.Folktails.blueprint.json`
- `Buildings/.../MyHouse.Folktails.Model.timbermesh`
- `TemplateCollections/TemplateCollection.Buildings.Folktails.blueprint.json`
- `Localizations/enUS.csv`

Route B adds:

- `MaterialCollections/MaterialCollection.Folktails.blueprint.json`
- `AssetBundles/MyHouse_win`

### Unity project mod

- `Assets/Mods/MyHouse/manifest.json`
- `Assets/Mods/MyHouse/Data/...`
- `Assets/Mods/MyHouse/AssetBundles/Resources/...`

## Route A Checklist

1. Start from `Example building`.
2. Export `.timbermesh` from Blender CLI.
3. Wire `TimbermeshSpec.Model` in the building Blueprint.
4. Register the building in `TemplateCollection`.
5. Add localization and icon.
6. Test placement in game.
7. If the look is still texture-dependent, switch to Route B.

## Route B Checklist

1. Export `.timbermesh` and extract the base texture from Blender CLI.
2. Create a Unity `Material`.
3. Store bundle assets under `AssetBundles/Resources/Materials/<BuildingName>/`.
4. Keep material and texture basenames distinct.
5. Add `MaterialCollection`.
6. Register the material with a normalized lower-case key such as `materials/myhouse/myhousebase`.
7. Build the AssetBundle with Unity CLI.
8. Fully restart Timberborn and re-test placement.

## Command Skeletons

### Blender CLI

```powershell
& "C:\Program Files\Blender Foundation\Blender 5.0\blender.exe" `
  --background `
  --python "D:\path\to\export_my_house.py"
```

### Unity CLI

```powershell
& "C:\Program Files\Unity\Hub\Editor\6000.4.0f1\Editor\Unity.exe" `
  -batchmode `
  -quit `
  -projectPath "D:\path\to\timberborn-modding-project" `
  -buildTarget StandaloneWindows64 `
  -executeMethod Timberborn.ModdingTools.ModBuilding.MyHouseCliBuild.BuildWindows `
  -logFile "D:\path\to\unity-my-house-build.log"
```

## Deliverables to Report

- Which route was used and why
- Exact files created or updated
- Commands run
- What was verified locally
- What still needs in-game confirmation
