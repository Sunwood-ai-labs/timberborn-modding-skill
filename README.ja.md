<div align="center">
  <img src="./docs/public/skillmark.svg" width="128" alt="">
  <h1>Timberborn Modding Skill</h1>
  <p><strong>JSON 調整 MOD、新規建物アセット、UI 付き code mod まで扱う Timberborn 向け Codex スキルです。</strong></p>
  <p>content mod の分岐、Blender CLI による <code>.timbermesh</code> 化、Blueprint 配線、Unity AssetBundle material、C# や BepInEx への段階的な移行まで案内します。</p>
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

`timberborn-modding` は、Timberborn MOD 制作で「どのトラックで進めるべきか」を最初に正しく選ぶための Codex スキルです。

次の流れをまとめて扱えます。

- JSON content mod で既存 Blueprint 値を patch する
- JSON 調整パックで多数の数値変更をまとめる
- 新規建物アセットで ルートA / ルートB を選ぶ
- C# DLL / UI MOD でゲーム内設定や code-driven な挙動を足す
- Blueprint や通常 API で足りない場合に BepInEx / Harmony へ進む

`MaterialCollection`、`.mat` と `.png` の basename 衝突、Blueprint に値が見えないケース、再起動前提の確認ポイントまで含めて再利用できる形でまとめています。

## 🚀 クイックスタート

1. Codex の skills ディレクトリへ clone します。

```powershell
git clone https://github.com/Sunwood-ai-labs/timberborn-modding-skill.git "$HOME/.codex/skills/timberborn-modding"
```

2. Codex にスキル利用を指示します。

```text
Use $timberborn-modding to make a Timberborn JSON content mod that lowers building science cost.
```

```text
Use $timberborn-modding and preserve the original GLB texture with the Unity AssetBundle path.
```

```text
Use $timberborn-modding to scaffold a Timberborn C# mod with a small in-game settings panel.
```

## 🧭 MOD トラック

| トラック | 向いているケース | 主なツール |
| --- | --- | --- |
| JSON content mod | 既存 Blueprint の値変更だけで足りる | `Empty`、`*.blueprint.json` |
| JSON 調整パック | 多数の数値変更をまとめたい | `Empty`、生成または整理した JSON |
| 新規建物アセット: ルートA | Timberborn 風の built-in material で十分 | Blender CLI、`.timbermesh`、Blueprint |
| 新規建物アセット: ルートB | 元の texture を保ちたい | Blender CLI、`.timbermesh`、Unity CLI、AssetBundle |
| C# DLL / UI MOD | ゲーム内設定や code-driven な挙動が必要 | C#、Timberborn assemblies、必要に応じて JSON 生成 |
| BepInEx / Harmony | Blueprint や通常 API では届かない | runtime patch |

大事なのは、最初に MOD トラックを決めることです。そのうえで、新規建物アセットの中だけで ルートA / ルートB を選びます。

## 🗺️ 新規建物アセットフロー

新しい配置物を作るときに、ルートA / ルートB の分岐を含めた全体像を一目で確認したい場合はこの図を使います。

![新規建物アセットフロー](./assets/new-building-asset-flow.drawio.png)

- ガイドページ: [ルート選定](./docs/ja/guide/workflow-routes.md)
- SVG を開く: [new-building-asset-flow.drawio.svg](./assets/new-building-asset-flow.drawio.svg)
- 元ファイルを編集: [new-building-asset-flow.drawio](./assets/new-building-asset-flow.drawio)

## 📦 同梱リソース

- [SKILL.md](./SKILL.md): Codex 向けのスキル定義
- [mod types reference](./references/mod-types.md): JSON、建物アセット、DLL、advanced runtime patch の分岐
- [workflow reference](./references/workflow.md): 標準フローと分岐
- [troubleshooting reference](./references/troubleshooting.md): よくある失敗の切り分け
- [Route A example](./references/example-route-a.md): built-in material 前提の最小例
- [Route B example](./references/example-route-b.md): custom texture と AssetBundle の最小例
- [Blender export template](./assets/export_glb_to_timbermesh_template.py): `GLB -> .timbermesh` 用の雛形スクリプト
- [building Blueprint template](./assets/building_blueprint.template.json): 建物 Blueprint の最小テンプレート
- [material collection template](./assets/material_collection.template.json): custom material 登録テンプレート
- [template collection template](./assets/template_collection_buildings.template.json): 建物一覧登録テンプレート

## 🛠️ このスキルが防ぐ失敗

- 単純な JSON content mod で済むのに、いきなり新規建物アセットへ進んでしまう
- hidden な runtime 挙動を Blueprint 値だと思い込む
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
- MOD 種別: [MOD 種別](https://sunwood-ai-labs.github.io/timberborn-modding-skill/ja/guide/mod-types)
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
