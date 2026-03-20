---
layout: home

hero:
  name: Timberborn Modding Skill
  text: JSON patch から新規建物アセットまで Timberborn MOD を作る
  tagline: content mod、建物アセット、Unity AssetBundle、C# や BepInEx への分岐を案内する Codex スキルです。
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
  - title: 先に MOD 種別を決める
    details: JSON content mod、調整パック、新規建物アセット、code-driven mod のどれかを先に判断できます。
  - title: 建物アセットはルートAかルートB
    details: 新規建物アセットでは、built-in material で進めるか、AssetBundle が必要かを早めに決められます。
  - title: 実戦の落とし穴を回避
    details: MaterialCollection path、`.mat` と `.png` の basename 衝突、Blueprint に値が見えないケースまで整理しています。
---

## 進め方の 3 ステップ

1. まずは [はじめに](/ja/guide/getting-started) でトラック、出力先、使用ツールの前提をそろえます。
2. 次に [MOD 種別](/ja/guide/mod-types) を見て、JSON、建物アセット、DLL、advanced runtime patch のどれかを選びます。
3. その後に [ルート選定](/ja/guide/workflow-routes) と [トラブルシュート](/ja/guide/troubleshooting) を使って詰めます。

新規建物アセットの分岐を一枚で見たい場合は [ルート選定](/ja/guide/workflow-routes) を開いてください。新規建物アセットフローの SVG をそのまま掲載しています。
