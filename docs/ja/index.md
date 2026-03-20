---
layout: home

hero:
  name: Timberborn Modding Skill
  text: GLB アセットを Timberborn の配置可能な建物 MOD にする
  tagline: ルート選定、Blender CLI による timbermesh 化、Blueprint 配線、Unity AssetBundle material ワークフローを案内する Codex スキルです。
  image:
    src: /skillmark.svg
    alt: ""
  actions:
    - theme: brand
      text: はじめに
      link: /ja/guide/getting-started
    - theme: alt
      text: トラブルシュート
      link: /ja/guide/troubleshooting

features:
  - title: 先にルートを決める
    details: Timberborn built-in material で行くか、custom AssetBundle で行くかを早めに判断できます。
  - title: すぐ使えるテンプレート
    details: Blender export、建物 Blueprint、material 登録、TemplateCollection 配線の雛形を同梱しています。
  - title: 実戦の落とし穴を回避
    details: MaterialCollection path、`.mat` と `.png` の basename 衝突、再起動前提の確認ポイントまで整理しています。
---

## 進め方の 3 ステップ

1. まずは [はじめに](/ja/guide/getting-started) で Blender、Unity、リポジトリ構成の前提をそろえます。
2. 次に [ルート選定](/ja/guide/workflow-routes) を見て、built-in material で進めるか、AssetBundle が必要かを判断します。
3. 作業中は [トラブルシュート](/ja/guide/troubleshooting) を開いておき、MaterialCollection や basename 衝突をすぐ切り分けます。
