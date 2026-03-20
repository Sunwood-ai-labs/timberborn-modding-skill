<div align="center">
  <img src="./docs/public/skillmark.svg" width="128" alt="">
  <h1>Timberborn Modding Skill</h1>
  <p><strong>GLB アセットを Timberborn の配置可能な建物 MOD に落とし込むための Codex スキルです。</strong></p>
  <p>ルート選定、Blender CLI による <code>.timbermesh</code> 化、Blueprint 配線、Unity AssetBundle material ワークフローまでを案内します。</p>
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

## ✨ 概要

`timberborn-modding` は、Timberborn の建物 MOD 制作に特化した Codex スキルです。

特に次の分岐を早めに正しく判断できるようにします。

- ルートA: Timberborn 既存 material を使い、`Blender + .timbermesh + Blueprint` で軽く進める
- ルートB: custom texture を維持し、`Blender + .timbermesh + Unity + AssetBundle` で仕上げる

実戦でハマりやすい `MaterialCollection`、`.mat` と `.png` の basename 衝突、再起動前提の確認ポイントまで含めて再利用できる形でまとめています。

## 🚀 クイックスタート

1. Codex の skills ディレクトリへ clone します。

```powershell
git clone https://github.com/Sunwood-ai-labs/timberborn-modding-skill.git "$HOME/.codex/skills/timberborn-modding"
```

2. Codex にスキル利用を指示します。

```text
Use $timberborn-modding to turn my GLB into a Timberborn building mod.
```

3. custom texture を維持したい場合は明示します。

```text
Use $timberborn-modding and preserve the original GLB texture with the Unity AssetBundle path.
```

## 🧭 ルート選定

| ルート | 向いているケース | 主なツール |
| --- | --- | --- |
| ルートA | Timberborn 風の built-in material で十分 | Blender CLI、`.timbermesh`、Blueprint |
| ルートB | 元の texture を保ちたい | Blender CLI、`.timbermesh`、Unity CLI、AssetBundle |

大事なのは、texture-baked 型の `GLB` を無理にルートAで押し切らないことです。見た目の情報が画像側に強くあるなら、早めにルートBへ切り替えたほうが安定します。

## 📦 同梱リソース

- [SKILL.md](./SKILL.md): Codex 向けのスキル定義
- [workflow reference](./references/workflow.md): 標準フローと分岐
- [troubleshooting reference](./references/troubleshooting.md): よくある失敗の切り分け
- [Route A example](./references/example-route-a.md): built-in material 前提の最小例
- [Route B example](./references/example-route-b.md): custom texture と AssetBundle の最小例
- [Blender export template](./assets/export_glb_to_timbermesh_template.py): `GLB -> .timbermesh` 用の雛形スクリプト
- [building Blueprint template](./assets/building_blueprint.template.json): 建物 Blueprint の最小テンプレート
- [material collection template](./assets/material_collection.template.json): custom material 登録テンプレート
- [template collection template](./assets/template_collection_buildings.template.json): 建物一覧登録テンプレート

## 🛠️ このスキルが防ぐ失敗

- `.timbermesh` 化だけで元の GLB texture がそのまま出ると思い込む
- texture-baked 型アセットでルート選択を誤る
- `MaterialCollection` に Timberborn が解決できない path を書く
- `.mat` と `.png` に同じ basename を使ってしまう
- bundle 側更新後に Timberborn の完全再起動を省く

## 🗂️ リポジトリ構成

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

## 🌐 ドキュメント

- 公開 docs: [sunwood-ai-labs.github.io/timberborn-modding-skill](https://sunwood-ai-labs.github.io/timberborn-modding-skill/)
- 導入: [はじめに](https://sunwood-ai-labs.github.io/timberborn-modding-skill/ja/guide/getting-started)
- トラブルシュート: [トラブルシュート](https://sunwood-ai-labs.github.io/timberborn-modding-skill/ja/guide/troubleshooting)

## ✅ 検証

スキル構造の検証:

```powershell
uv run --with pyyaml python scripts/validate_skill.py .
```

docs のローカル build:

```powershell
Set-Location docs
npm ci
npm run docs:build
```

## 🤝 コントリビュート

Pull Request と issue は歓迎です。検証手順は [CONTRIBUTING.md](./CONTRIBUTING.md)、機微な報告は [SECURITY.md](./SECURITY.md) を確認してください。

## 📄 ライセンス

[MIT License](./LICENSE) で公開しています。
