# リポジトリ構成

## 全体構成

```text
.
├── SKILL.md
├── assets/
├── docs/
├── references/
└── scripts/
```

## 各ディレクトリの役割

### `assets/`

実装を始めるための雛形:

- Blender CLI export テンプレート
- building Blueprint テンプレート
- material collection テンプレート
- template collection テンプレート

### `references/`

Codex が必要時に読む詳細資料:

- MOD 種別の分岐
- 標準ワークフロー
- トラブルシュート

### `scripts/`

CI とローカル検証に使う補助スクリプト。

### `docs/`

VitePress で公開する人向けドキュメント。

## `references` と `docs` を分ける理由

- `references/` は Codex 実行時の判断材料向け
- `docs/` は GitHub と Pages で読む人向け
