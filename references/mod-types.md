# Mod Types

## Track 1: JSON Content Mod

Use this when:

- the task is changing existing Blueprint values
- the user wants balance tweaks such as cost, speed, capacity, workers, or recipe numbers
- no new model, UI, or runtime hook is needed

Typical fit:

- `GoodCarrierSpec.BaseLiftingCapacity`
- `WalkerSpeedManagerSpec.BaseWalkingSpeed`
- `StockpileSpec.MaxCapacity`
- `BuildingSpec.BuildingCost`
- `BuildingSpec.ScienceCost`
- `WorkplaceSpec.MaxWorkers`

Recommended base:

- `Empty` mod template

## Track 2: JSON Adjustment Pack

Use this when:

- the user wants many Blueprint tweaks bundled together
- the work should be generated or kept consistent across many files
- the project is still data-driven and does not need in-game UI

Recommended base:

- `Empty` mod template plus a repeatable generation script if the patch set is large

## Track 3: New Building Asset

Use this when:

- the user wants a new placeable building
- the job needs a Blueprint, icon, localization, and `TemplateCollection`
- a new `.timbermesh` or custom material is involved

Recommended base:

- `Example building`

Inside this track:

- Route A uses Timberborn built-in materials and avoids Unity when possible
- Route B preserves the original textured look with Unity and AssetBundles

## Track 4: C# DLL or UI Mod

Use this when:

- the user wants in-game configuration UI
- the mod should save settings or generate JSON from a control panel
- normal static Blueprint patches are not enough

Typical signs:

- the change needs `IModStarter`, `Configurator`, `ILoadableSingleton`, or UI layout code
- the user wants a settings panel, buttons, or notifications

## Track 5: BepInEx or Harmony Runtime Patch

Use this when:

- the target value is not visible in Blueprint or normal mod APIs
- the job requires patching game logic rather than just supplying content
- the requested behavior looks like activity range, hidden logic, or runtime-only systems

Guardrail:

- escalate here only after checking whether Blueprint or standard code-mod APIs already expose the feature

## Recommended Learning Order

1. Start with a single JSON content mod.
2. Expand to a JSON adjustment pack.
3. Move to a new building asset with Route A or Route B.
4. Add a C# DLL or UI mod when the job needs in-game controls.
5. Use BepInEx or Harmony only for advanced cases.

## Fast Decision Rule

- Existing values only: JSON content mod
- Many related value patches: JSON adjustment pack
- New building or new visuals: building asset
- In-game panel or generated settings: C# DLL or UI mod
- No visible Blueprint or API hook: BepInEx or Harmony
