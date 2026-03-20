# Getting Started

## What This Skill Is For

Use this skill when Codex needs to:

- turn a `GLB`, `FBX`, or `OBJ` into a placeable Timberborn building
- choose between built-in Timberborn materials and custom textured AssetBundles
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
Use $timberborn-modding to turn my GLB into a Timberborn building mod.
```

```text
Use $timberborn-modding and keep the original GLB texture with the Unity AssetBundle route.
```

## Required Inputs

Codex should gather these before editing:

- source asset path
- target mod path
- faction, category, and footprint
- whether the user wants a Timberborn-style reinterpretation or the original textured look

## First Decision

Move to [Workflow Routes](/guide/workflow-routes) immediately after gathering the inputs.
