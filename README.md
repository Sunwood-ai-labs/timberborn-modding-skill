<div align="center">
  <img src="./docs/public/skillmark.svg" width="128" alt="">
  <h1>Timberborn Modding Skill</h1>
  <p><strong>Codex skill for Timberborn mod creation across JSON balance patches, new building assets, and UI-driven code mods.</strong></p>
  <p>Guide Codex through content-mod track selection, Blender CLI <code>.timbermesh</code> export, Blueprint wiring, Unity AssetBundle material workflows, and when to escalate to C# or BepInEx.</p>
</div>

<div align="center">
  <a href="https://github.com/Sunwood-ai-labs/timberborn-modding-skill/actions/workflows/validate.yml"><img src="https://github.com/Sunwood-ai-labs/timberborn-modding-skill/actions/workflows/validate.yml/badge.svg" alt="Validate"></a>
  <a href="https://github.com/Sunwood-ai-labs/timberborn-modding-skill/actions/workflows/docs.yml"><img src="https://github.com/Sunwood-ai-labs/timberborn-modding-skill/actions/workflows/docs.yml/badge.svg" alt="Docs"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/github/license/Sunwood-ai-labs/timberborn-modding-skill" alt="License"></a>
  <a href="https://sunwood-ai-labs.github.io/timberborn-modding-skill/"><img src="https://img.shields.io/badge/docs-GitHub%20Pages-2f855a" alt="Docs site"></a>
</div>

<div align="center">
  <a href="./README.md"><strong>English</strong></a>
  <span> | </span>
  <a href="./README.ja.md"><strong>日本語</strong></a>
</div>

## ✨ Overview

`timberborn-modding` is a Codex skill for choosing the right Timberborn mod track before implementation gets messy.

It now covers the full ladder:

- JSON content mods for patching existing Blueprint values
- JSON adjustment packs for larger rebalance bundles
- New building assets with Route A or Route B
- C# DLL and UI mods when in-game controls are needed
- BepInEx or Harmony escalation when Blueprint and normal APIs are not enough

The skill bundles practical references, reusable templates, and guardrails based on real Timberborn modding workflows.

## 🚀 Quick Start

1. Install the skill into your Codex skills directory.

```powershell
git clone https://github.com/Sunwood-ai-labs/timberborn-modding-skill.git "$HOME/.codex/skills/timberborn-modding"
```

2. Ask Codex to use it.

```text
Use $timberborn-modding to make a Timberborn JSON content mod that lowers building science cost.
```

```text
Use $timberborn-modding and preserve the original GLB texture with the Unity AssetBundle path.
```

```text
Use $timberborn-modding to scaffold a Timberborn C# mod with a small in-game settings panel.
```

## 🧭 Mod Tracks

| Track | Use it when | Main tools |
| --- | --- | --- |
| JSON content mod | Existing Blueprint values are enough | `Empty`, `*.blueprint.json` |
| JSON adjustment pack | Many related value patches belong together | `Empty`, generated or organized JSON |
| New building asset: Route A | Timberborn-style built-in materials are enough | Blender CLI, `.timbermesh`, Blueprint |
| New building asset: Route B | The original textured look must survive | Blender CLI, `.timbermesh`, Unity CLI, AssetBundle |
| C# DLL or UI mod | In-game controls or code-driven behavior are needed | C#, Timberborn assemblies, optional JSON generation |
| BepInEx or Harmony | The feature is not exposed in Blueprint or normal APIs | Runtime patching |

The key rule is simple: choose the mod track first, then choose Route A or Route B only inside the new building asset track.

## 🗺️ New Building Asset Flow

Use this diagram when the task is a new placeable building and you want the full route split at a glance.

![New building asset flow](./assets/new-building-asset-flow.en.drawio.png)

- Guide page: [Workflow Routes](./docs/guide/workflow-routes.md)
- View SVG: [new-building-asset-flow.en.drawio.svg](./assets/new-building-asset-flow.en.drawio.svg)
- Edit source: [new-building-asset-flow.en.drawio](./assets/new-building-asset-flow.en.drawio)

## 📦 Bundled Resources

- [SKILL.md](./SKILL.md): trigger description and operating instructions for Codex
- [mod types reference](./references/mod-types.md): choose between JSON, asset, DLL, and advanced runtime tracks
- [workflow reference](./references/workflow.md): route split, commands, and deliverables
- [troubleshooting reference](./references/troubleshooting.md): common Timberborn asset failures
- [Route A example](./references/example-route-a.md): minimal built-in material scenario
- [Route B example](./references/example-route-b.md): custom texture and AssetBundle scenario
- [Blender export template](./assets/export_glb_to_timbermesh_template.py): starter script for `GLB -> .timbermesh`
- [building Blueprint template](./assets/building_blueprint.template.json): minimal building skeleton
- [material collection template](./assets/material_collection.template.json): custom material registration starter
- [template collection template](./assets/template_collection_buildings.template.json): building registration starter

## 🛠️ What The Skill Guards Against

- Choosing a new building asset workflow when a simple JSON content mod would do
- Treating a hidden runtime behavior as if it were a visible Blueprint value
- Assuming `.timbermesh` alone preserves the original GLB texture look
- Choosing the wrong route for texture-baked assets
- Registering `MaterialCollection` with a path shape that Timberborn cannot resolve
- Reusing the same basename for `.mat` and `.png` files
- Forgetting to fully restart Timberborn after bundle-side material changes

## 🗂️ Repository Layout

```text
.
├── SKILL.md
├── README.md
├── README.ja.md
├── assets/
├── docs/
├── references/
└── scripts/
```

## 🌐 Documentation

- Live docs: [sunwood-ai-labs.github.io/timberborn-modding-skill](https://sunwood-ai-labs.github.io/timberborn-modding-skill/)
- Mod Types: [Mod Types](https://sunwood-ai-labs.github.io/timberborn-modding-skill/guide/mod-types)
- Getting Started: [Getting Started](https://sunwood-ai-labs.github.io/timberborn-modding-skill/guide/getting-started)
- Troubleshooting: [Troubleshooting Guide](https://sunwood-ai-labs.github.io/timberborn-modding-skill/guide/troubleshooting)

## ✅ Validation

Validate the skill structure:

```powershell
uv run --with pyyaml python scripts/validate_skill.py .
```

Build the docs locally:

```powershell
Set-Location docs
npm ci
npm run docs:build
```

## 🤝 Contributing

Pull requests and issue reports are welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md) for validation expectations and [SECURITY.md](./SECURITY.md) for sensitive disclosures.

## 📄 License

Released under the [MIT License](./LICENSE).
