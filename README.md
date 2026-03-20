<div align="center">
  <img src="./docs/public/skillmark.svg" width="128" alt="">
  <h1>Timberborn Modding Skill</h1>
  <p><strong>Codex skill for turning GLB assets into placeable Timberborn buildings.</strong></p>
  <p>Guide Codex through route selection, Blender CLI <code>.timbermesh</code> export, Blueprint wiring, and Unity AssetBundle material workflows.</p>
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

`timberborn-modding` is a Codex skill focused on one job: taking Timberborn building ideas from source assets to a working in-game mod.

It helps Codex choose the right path early:

- Route A: use Timberborn built-in materials and ship fast with `Blender + .timbermesh + Blueprint`
- Route B: preserve custom textures with `Blender + .timbermesh + Unity + AssetBundle`

The skill bundles practical references, reusable templates, and guardrails based on a real end-to-end Timberborn building workflow.

## 🚀 Quick Start

1. Install the skill into your Codex skills directory.

```powershell
git clone https://github.com/Sunwood-ai-labs/timberborn-modding-skill.git "$HOME/.codex/skills/timberborn-modding"
```

2. Ask Codex to use it.

```text
Use $timberborn-modding to turn my GLB into a Timberborn building mod.
```

3. For a custom textured asset, be explicit.

```text
Use $timberborn-modding and preserve the original GLB texture with the Unity AssetBundle path.
```

## 🧭 Route Selection

| Route | Use it when | Main tools |
| --- | --- | --- |
| Route A | Timberborn-style built-in materials are enough | Blender CLI, `.timbermesh`, Blueprint |
| Route B | The original textured look must survive | Blender CLI, `.timbermesh`, Unity CLI, AssetBundle |

The key rule is simple: if the source mesh is texture-baked and visual detail mostly lives in the image, move to Route B early instead of over-tuning material remaps.

## 📦 Bundled Resources

- [SKILL.md](./SKILL.md): trigger description and operating instructions for Codex
- [workflow reference](./references/workflow.md): route split, commands, and deliverables
- [troubleshooting reference](./references/troubleshooting.md): common Timberborn asset failures
- [Route A example](./references/example-route-a.md): minimal built-in material scenario
- [Route B example](./references/example-route-b.md): custom texture and AssetBundle scenario
- [Blender export template](./assets/export_glb_to_timbermesh_template.py): starter script for `GLB -> .timbermesh`
- [building Blueprint template](./assets/building_blueprint.template.json): minimal building skeleton
- [material collection template](./assets/material_collection.template.json): custom material registration starter
- [template collection template](./assets/template_collection_buildings.template.json): building registration starter

## 🛠️ What The Skill Guards Against

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
- Start here: [Getting Started](https://sunwood-ai-labs.github.io/timberborn-modding-skill/guide/getting-started)
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
