# Mod Types

## Pick the Track Before You Edit

This skill supports more than new building assets. The first job is choosing the right Timberborn mod track.

## JSON Content Mod

Use this when you are changing existing Blueprint values only.

Good fit:

- carry capacity
- walking speed
- storage capacity
- building cost
- science cost
- worker counts
- recipe values

Recommended base:

- `Empty`

## JSON Adjustment Pack

Use this when the mod bundles many Blueprint patches into one balance pack.

Good fit:

- multi-file rebalance packs
- generated JSON patches
- consistent data changes across many buildings or characters

Recommended base:

- `Empty`, with a repeatable generation script if needed

## New Building Asset

Use this when the user wants a new placeable structure.

Good fit:

- new Blueprint
- `.timbermesh`
- icon and localization
- `TemplateCollection`

Recommended base:

- `Example building`

Inside this track:

- Route A keeps Timberborn built-in materials
- Route B preserves custom textures with Unity and AssetBundles

## C# DLL or UI Mod

Use this when the user wants in-game controls, generated settings, or code-driven behavior.

Good fit:

- settings panel
- JSON generation from UI
- notifications and buttons
- logic that is no longer comfortable as static data

## BepInEx or Harmony Runtime Patch

Use this only when the feature is not exposed in Blueprint or normal mod APIs.

Good fit:

- hidden activity-range logic
- behavior not represented in normal content data
- method-level runtime changes

## Recommended Order

1. JSON content mod
2. JSON adjustment pack
3. New building asset
4. C# DLL or UI mod
5. BepInEx or Harmony runtime patch
