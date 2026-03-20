# Getting Started

## What This Skill Is For

Use this skill when Codex needs to:

- patch existing Blueprint JSON and build Timberborn content mods
- bundle many JSON changes into a balance pack
- turn a `GLB`, `FBX`, or `OBJ` into a placeable Timberborn building
- scaffold or debug a C# DLL or UI mod
- choose between built-in Timberborn materials and custom textured AssetBundles
- decide when Blueprint is enough and when BepInEx or Harmony is required
- wire Blueprints, `TemplateCollection`, and `MaterialCollection`
- troubleshoot broken preview models, missing materials, or bundle loading errors

## Install

Clone the repository into your Codex skills directory.

```powershell
git clone https://github.com/Sunwood-ai-labs/timberborn-modding-skill.git "$HOME/.codex/skills/timberborn-modding"
```

## Invoke

Typical prompts:

```text
Use $timberborn-modding to make a Timberborn JSON content mod that lowers building science cost.
```

```text
Use $timberborn-modding to turn my GLB into a Timberborn building mod.
```

```text
Use $timberborn-modding and keep the original GLB texture with the Unity AssetBundle route.
```

```text
Use $timberborn-modding to scaffold a Timberborn C# mod with a small in-game settings panel.
```

## Required Inputs

Codex should gather these before editing:

- mod track: JSON content mod, adjustment pack, building asset, DLL or UI mod, or advanced runtime patch
- target mod path
- source asset path if a new building asset is involved
- faction, category, and footprint if a new building asset is involved
- whether the user wants a Timberborn-style reinterpretation or the original textured look for building assets
- whether the user wants settings UI, generated JSON, or live code behavior for code mods

## First Decision

Move to [Mod Types](/guide/mod-types) first, then continue to [Workflow Routes](/guide/workflow-routes).
