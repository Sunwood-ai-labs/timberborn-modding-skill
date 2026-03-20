# Workflow Routes

## Track 1: JSON Content Mod

Use this when:

- the task is an existing Blueprint value change
- the mod should stay content-only
- no new model or UI is required

Main flow:

1. Start from `Empty`.
2. Patch only the keys you need.
3. Keep the original Blueprint path.
4. Restart the game and verify the change.

## Track 2: JSON Adjustment Pack

Use this when:

- many Blueprint patches belong together
- the mod should stay data-driven
- a repeatable generation flow would help

Main flow:

1. Start from `Empty`.
2. Gather the target Blueprint paths up front.
3. Generate or organize the patches coherently.
4. Verify every output path before shipping.

## Track 3: New Building Asset

Use this when:

- the user wants a new placeable building
- `.timbermesh`, icon, localization, or `TemplateCollection` are involved

### Route A: Built-in Timberborn Materials

Use Route A when:

- Timberborn-style materials are acceptable
- the mesh can look correct without custom textures
- the project should avoid Unity unless necessary

Main flow:

1. Start from `Example building`.
2. Export `.timbermesh` from Blender CLI.
3. Wire the building Blueprint.
4. Register the building in `TemplateCollection`.
5. Test placement in game.

### Route B: Custom Textures with AssetBundles

Use Route B when:

- the source `GLB` is texture-baked
- the original look matters
- Route A already produced broken or noisy visuals

Main flow:

1. Export `.timbermesh` and extract the texture from Blender CLI.
2. Create a Unity `Material`.
3. Place bundle assets under `AssetBundles/Resources/...`.
4. Add `MaterialCollection`.
5. Build the bundle with Unity CLI.
6. Fully restart Timberborn and retest.

## Track 4: C# DLL or UI Mod

Use this when:

- the user wants an in-game settings panel
- JSON should be generated from UI
- code-driven behavior is required

Main flow:

1. Inspect the existing project and references.
2. Add the needed starter, services, and UI layers.
3. Decide whether the mod writes JSON for next launch, changes behavior live, or both.
4. Build and verify the DLL load path.

## Track 5: BepInEx or Harmony Runtime Patch

Use this when:

- the value or behavior is not exposed in Blueprint or normal mod APIs
- the request targets hidden or runtime-only logic

Main flow:

1. Prove that Blueprint and normal code-mod APIs are insufficient.
2. Inspect the target game type or method carefully.
3. Patch only the smallest necessary surface.
4. Document the higher verification burden.

## Key Guardrails

- Start from `Empty` for JSON work and `Example building` for new structures.
- Do not assume `.timbermesh` preserves the original texture look by itself.
- Keep `.mat` and `.png` basenames distinct.
- Prefer lower-case normalized keys in `MaterialCollection`.
- If a value is not visible in Blueprint, be ready to move to C# or BepInEx.
- Restart Timberborn after material-side, JSON, or DLL changes.
