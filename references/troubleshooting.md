# Troubleshooting

## "Material <name> not found in repository"

Likely causes:

- `MaterialCollection` is missing.
- The registered material key does not match the runtime-normalized key.
- The AssetBundle did not build or did not copy to the game mod folder.

Check:

- Built mod contains `MaterialCollections/MaterialCollection.<Faction>.blueprint.json`.
- Built mod contains `AssetBundles/<mod>_win`.
- `Materials#append` uses the normalized lower-case key, for example `materials/myhouse/myhousebase`.

## "Failed to load asset at ..."

Likely causes:

- The `MaterialCollection` path uses the wrong shape.
- The requested asset lives in the bundle under a different normalized key.
- A `.mat` and `.png` share the same basename and collide during provider normalization.

Check:

- Avoid full project-style paths such as `Assets/Mods/.../MyHouseBase.mat` in `MaterialCollection`.
- Keep `.mat` and `.png` basenames distinct.
- Rebuild the bundle after renaming either asset.

## Garbled or noisy textures after `.timbermesh` conversion

Likely causes:

- The source `GLB` is texture-baked and Route A was used anyway.
- Built-in material remapping was forced onto a texture-driven mesh.
- UV projection was changed in a way that does not fit the source model.

Response:

- Re-evaluate the route.
- If the original look matters, switch to Route B instead of over-tuning built-in material mapping.

## Unity says another instance is already using the project

Cause:

- A prior batch build or inspect command is still running.

Response:

- Wait for the existing Unity process to exit before starting another batch run.
- Confirm the current build log reached a success or shutdown line before retrying.

## The game still shows the old state

Cause:

- Timberborn held a stale material or asset repository in memory.

Response:

- Fully close Timberborn.
- Restart it before re-testing.

## Placement button exists but the preview is broken

Likely causes:

- The model path in `TimbermeshSpec.Model` is wrong.
- The custom material failed to load.
- The bundle exists but the material registration path is wrong.

Check:

- Building Blueprint model reference
- Built `.timbermesh` file existence
- Bundle existence
- MaterialCollection registration key
