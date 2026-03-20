# Example Route B

Use this example when the source asset depends on its original texture and the look must survive in game.

## Scenario

- Source asset: a texture-baked `GLB` with most visual detail painted into the image
- Goal: preserve the original textured look
- Tools: Blender CLI, `.timbermesh`, Unity `Material`, `MaterialCollection`, AssetBundle

## Recommended Output

- one finished `.timbermesh`
- extracted texture PNG
- one Unity `Material`
- one `MaterialCollection` entry using a normalized lower-case key
- one built `AssetBundle`

## Why Route B Fits

- the mesh is simple but the image carries the detail
- built-in material remapping is likely to look garbled
- a custom material path gives the most reliable visual result
