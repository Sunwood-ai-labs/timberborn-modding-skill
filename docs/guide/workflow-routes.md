# Workflow Routes

## Route A: Built-in Timberborn Materials

Use Route A when:

- Timberborn-style materials are acceptable
- the mesh can look correct without custom textures
- the project should avoid Unity unless necessary

Main flow:

1. Start from `Example building`
2. Export `.timbermesh` from Blender CLI
3. Wire the building Blueprint
4. Register the building in `TemplateCollection`
5. Test placement in game

## Route B: Custom Textures with AssetBundles

Use Route B when:

- the source `GLB` is texture-baked
- the original look matters
- Route A already produced broken or noisy visuals

Main flow:

1. Export `.timbermesh` and extract the texture from Blender CLI
2. Create a Unity `Material`
3. Place bundle assets under `AssetBundles/Resources/...`
4. Add `MaterialCollection`
5. Build the bundle with Unity CLI
6. Fully restart Timberborn and retest

## Key Guardrails

- Do not assume `.timbermesh` preserves the original texture look by itself
- Keep `.mat` and `.png` basenames distinct
- Prefer lower-case normalized keys in `MaterialCollection`
- Restart Timberborn after material-side changes
