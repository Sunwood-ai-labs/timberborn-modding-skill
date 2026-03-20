# Workflow

## Step 1: Choose the Mod Track

### Track 1: JSON Content Mod

Use this when:

- the user wants to change existing Blueprint values
- the job is still data-driven
- no new model, UI, or runtime patch is needed

Main flow:

1. Start from `Empty`.
2. Find the exact target Blueprint path.
3. Patch only the keys that need changing.
4. Restart Timberborn and confirm the mod is enabled.

Typical editable specs:

- `GoodCarrierSpec.BaseLiftingCapacity`
- `WalkerSpeedManagerSpec.BaseWalkingSpeed`
- `StockpileSpec.MaxCapacity`
- `BuildingSpec.BuildingCost`
- `BuildingSpec.ScienceCost`
- `WorkplaceSpec.MaxWorkers`

### Track 2: JSON Adjustment Pack

Use this when:

- the user wants many related JSON changes
- consistent naming and generation matter
- the mod is still data-driven and should remain easy to diff

Main flow:

1. Start from `Empty`.
2. Gather every target Blueprint path first.
3. Generate or organize the patches coherently.
4. Verify that each output path matches a real game Blueprint path.

### Track 3: Building Asset

Use this when:

- the user wants a new placeable building
- the mod needs `.timbermesh`, icon, localization, or `TemplateCollection`
- a custom material might be required

Choose Route A or Route B inside this track.

#### Route A

- Use Timberborn built-in materials.
- Skip Unity AssetBundles.
- Prefer this when geometry and material assignment can carry the look.

Typical signs:

- The model is already split into meaningful surfaces such as wood, plaster, and roof pieces.
- The desired result is "Timberborn-style" rather than "match the original render exactly."

#### Route B

- Preserve custom textures.
- Add a Unity `Material`.
- Build an AssetBundle.

Typical signs:

- The source `GLB` is texture-baked.
- The mesh is simple but the look depends on the image.
- Route A produced garbled or noisy visuals.

### Track 4: C# DLL or UI Mod

Use this when:

- the user wants an in-game settings panel
- JSON should be generated or toggled from UI
- a static data patch is no longer enough

Main flow:

1. Inspect the existing code-mod project structure.
2. Add the needed starter, services, and UI layers.
3. Decide whether the mod writes JSON, changes live behavior, or both.
4. Verify build output and the game load path.

### Track 5: BepInEx or Harmony Runtime Patch

Use this when:

- the requested behavior is not visible in Blueprint or normal mod APIs
- a runtime patch is required
- the user is asking for hidden range or logic changes

Main flow:

1. Prove that the data or hook is not exposed in content or normal code mods.
2. Inspect the target game type or method carefully.
3. Patch only the minimum behavior required.
4. Document the higher risk and verification burden.

## Standard Inputs to Gather

- Mod track
- Source asset path
- Target mod path
- Unity project path if Route B is likely
- Faction, category, footprint, and desired display name
- Whether the user wants the original look or a Timberborn-style reinterpretation

## Standard File Layout

### Built mod

Minimum:

- `manifest.json`
- one or more `*.blueprint.json` patches for JSON content mods
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

## Track Checklists

### JSON Content Mod Checklist

1. Start from `Empty`.
2. Patch only the target keys.
3. Keep the original game Blueprint path.
4. Restart Timberborn and verify the change.

### JSON Adjustment Pack Checklist

1. Group the target Blueprints before editing.
2. Keep each patch small and path-accurate.
3. Generate repeated patches when the pack is large.
4. Verify that every generated file is still under the correct game path.

### Building Asset Route A Checklist

1. Start from `Example building`.
2. Export `.timbermesh` from Blender CLI.
3. Wire `TimbermeshSpec.Model` in the building Blueprint.
4. Register the building in `TemplateCollection`.
5. Add localization and icon.
6. Test placement in game.
7. If the look is still texture-dependent, switch to Route B.

### Building Asset Route B Checklist

1. Export `.timbermesh` and extract the base texture from Blender CLI.
2. Create a Unity `Material`.
3. Store bundle assets under `AssetBundles/Resources/Materials/<BuildingName>/`.
4. Keep material and texture basenames distinct.
5. Add `MaterialCollection`.
6. Register the material with a normalized lower-case key such as `materials/myhouse/myhousebase`.
7. Build the AssetBundle with Unity CLI.
8. Fully restart Timberborn and re-test placement.

### C# DLL or UI Mod Checklist

1. Confirm that JSON alone is not enough.
2. Inspect the project file and references.
3. Add or update the starter, services, and UI components.
4. Verify the build output and load path.
5. Be explicit about what needs in-game confirmation.

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

- Which mod track was used and why
- If the building asset track was used, which route was used and why
- Exact files created or updated
- Commands run
- What was verified locally
- What still needs in-game confirmation
