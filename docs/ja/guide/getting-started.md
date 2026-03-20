# はじめに

## このスキルが向いている場面

次のような用途で使います。

- 既存 Blueprint JSON を patch して Timberborn の content mod を作る
- 複数の JSON 変更をまとめた調整パックを作る
- `GLB`、`FBX`、`OBJ` を Timberborn の配置可能な建物へ落とし込む
- C# DLL / UI MOD を組み立てたり調整したりする
- Timberborn built-in material と custom AssetBundle のどちらで進めるか判断する
- Blueprint で足りるか、BepInEx / Harmony まで必要かを判断する
- Blueprint、`TemplateCollection`、`MaterialCollection` を配線する
- preview 崩れ、material 未解決、bundle 読み込み失敗を切り分ける

## インストール

Codex の skills ディレクトリへ clone します。

```powershell
git clone https://github.com/Sunwood-ai-labs/timberborn-modding-skill.git "$HOME/.codex/skills/timberborn-modding"
```

## 呼び出し例

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

## 最初に集める情報

- どのトラックか
  - JSON content mod
  - JSON 調整パック
  - 新規建物アセット
  - C# DLL / UI MOD
  - advanced runtime patch
- 出力先 mod のパス
- 新規建物アセットなら元アセットのパス
- 新規建物アセットなら faction、category、footprint
- 建物アセットなら Timberborn 風に寄せるか、元の texture を維持するか
- code mod なら settings UI、JSON 生成、live な挙動変更のどれが必要か

## 最初の分岐

まずは [MOD 種別](/ja/guide/mod-types) を見てトラックを決め、その後に [ルート選定](/ja/guide/workflow-routes) へ進みます。
