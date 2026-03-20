# はじめに

## このスキルが向いている作業

次のような作業で使います。

- `GLB`、`FBX`、`OBJ` を Timberborn の配置可能な建物へ落とし込む
- Timberborn built-in material と custom AssetBundle のどちらで行くか判断する
- Blueprint、`TemplateCollection`、`MaterialCollection` を配線する
- preview 破損、material 未解決、bundle 読み込み失敗を切り分ける

## インストール

Codex の skills ディレクトリへ clone します。

```powershell
git clone https://github.com/Sunwood-ai-labs/timberborn-modding-skill.git "$HOME/.codex/skills/timberborn-modding"
```

## 呼び出し例

```text
Use $timberborn-modding to turn my GLB into a Timberborn building mod.
```

```text
Use $timberborn-modding and keep the original GLB texture with the Unity AssetBundle route.
```

## 最初に集める情報

- 元アセットのパス
- 出力先 mod のパス
- faction、category、footprint
- Timberborn 風に寄せるか、元の texture を維持するか

## 最初の分岐

入力がそろったら、すぐに [ルート選定](/ja/guide/workflow-routes) へ進みます。
