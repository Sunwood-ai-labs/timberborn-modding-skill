# Troubleshooting

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
