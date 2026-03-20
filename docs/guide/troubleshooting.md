# Troubleshooting

## JSON Patch Has No Visible Effect

Check:

- the patch file path matches the original game Blueprint path
- the mod was started from the correct content-mod template
- Timberborn was fully restarted after the change

## The Value Is Missing From Blueprint

This usually means the task is no longer a pure content mod.

If the value or behavior is not exposed in Blueprint, move toward a C# DLL mod or BepInEx and Harmony instead of inventing hidden JSON keys.

## Material Not Found In Repository

Check:

- `MaterialCollection` exists
- the bundle exists in the built mod folder
- the material key matches the normalized runtime key

## Failed To Load Asset

Common causes:

- wrong `MaterialCollection` path shape
- bundle asset resolved under a different normalized key
- `.mat` and `.png` share the same basename

## Garbled Visuals After `.timbermesh` Export

This usually means the asset belongs on Route B instead of Route A.

If the mesh is simple but the look depends on the image, do not keep forcing built-in material remaps.

## Old State Still Showing In Game

Fully restart Timberborn after custom material or AssetBundle changes.

## The User Wants A Settings Panel

That is a sign the task has moved beyond static JSON.

Switch to a C# DLL or UI mod when the user wants in-game toggles, notifications, or JSON generation from a save button.
