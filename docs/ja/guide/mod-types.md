# MOD 種別

## 先にトラックを決める

このスキルは、新規建物アセットだけでなく、JSON 調整 MOD や C# DLL MOD も扱います。最初にどのトラックで進めるかを決めるのが重要です。

## JSON content mod

既存 Blueprint の値だけを変えるときに向いています。

例:

- 積載量
- 移動速度
- 倉庫容量
- 建築コスト
- 研究コスト
- 労働者数
- レシピ値

おすすめの土台:

- `Empty`

## JSON 調整パック

複数の Blueprint patch をまとめて配るバランス調整向けです。

例:

- 複数ファイルの再調整パック
- 一括生成する JSON patch
- 多数の建物やキャラクターへ同系統の数値変更を入れる場合

おすすめの土台:

- `Empty`

## 新規建物アセット

新しい配置物を追加したいときに向いています。

例:

- 新しい Blueprint
- `.timbermesh`
- アイコンと localization
- `TemplateCollection`

おすすめの土台:

- `Example building`

このトラックの中で:

- ルートA は Timberborn built-in material を使う
- ルートB は custom texture を Unity と AssetBundle で持ち込む

## C# DLL / UI MOD

ゲーム内設定、UI、コード駆動の挙動が必要なときに向いています。

例:

- 設定パネル
- UI からの JSON 生成
- 通知やボタン
- static data だけでは表現しづらい処理

## BepInEx / Harmony runtime patch

Blueprint や通常の mod API では届かない機能にだけ使います。

例:

- hidden な活動範囲ロジック
- 通常の content data に出てこない挙動
- method 単位の runtime patch

## おすすめの学習順

1. JSON content mod
2. JSON 調整パック
3. 新規建物アセット
4. C# DLL / UI MOD
5. BepInEx / Harmony runtime patch
