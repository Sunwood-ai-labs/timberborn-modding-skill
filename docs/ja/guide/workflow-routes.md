# ルート選定

## トラック1: JSON content mod

向いているケース:

- 既存 Blueprint の値変更が目的
- content-only で済ませたい
- 新しいモデルや UI は不要

主な流れ:

1. `Empty` から始める
2. 必要な key だけ patch する
3. 元の Blueprint path を保つ
4. ゲーム再起動後に確認する

## トラック2: JSON 調整パック

向いているケース:

- 複数の Blueprint patch をまとめたい
- data-driven のまま進めたい
- 一括生成や整理が必要

主な流れ:

1. `Empty` から始める
2. 対象 Blueprint path を先にそろえる
3. patch をまとめて生成または整理する
4. 出力 path を全部確認する

## トラック3: 新規建物アセット

向いているケース:

- 新しい配置物を追加したい
- `.timbermesh`、アイコン、localization、`TemplateCollection` が必要

### ルートA: Timberborn built-in material を使う

向いているケース:

- Timberborn 風の見た目で十分
- custom texture がなくても成立する
- Unity を極力使いたくない

主な流れ:

1. `Example building` を土台にする
2. Blender CLI で `.timbermesh` を出す
3. 建物 Blueprint を配線する
4. `TemplateCollection` に登録する
5. ゲーム内で配置確認する

### ルートB: custom texture を AssetBundle で持ち込む

向いているケース:

- 元 `GLB` が texture-baked 型
- 元の見た目を保ちたい
- ルートAでノイズや破綻が出た

主な流れ:

1. Blender CLI で `.timbermesh` と texture を出す
2. Unity で `Material` を作る
3. `AssetBundles/Resources/...` に置く
4. `MaterialCollection` を追加する
5. Unity CLI で bundle を build する
6. Timberborn を完全再起動して再確認する

## トラック4: C# DLL / UI MOD

向いているケース:

- ゲーム内設定パネルが必要
- UI から JSON を生成したい
- code-driven の挙動が必要

主な流れ:

1. project と references を確認する
2. starter、service、UI layer を追加する
3. 次回起動用 JSON を書くのか、live に挙動変更するのかを決める
4. DLL の build と読み込み path を確認する

## トラック5: BepInEx / Harmony runtime patch

向いているケース:

- Blueprint や通常の mod API では届かない
- hidden な runtime logic を触る必要がある

主な流れ:

1. Blueprint と通常 code mod で足りないことを確認する
2. 対象 type や method を慎重に調べる
3. 最小限の patch だけを入れる
4. 検証負荷が高いことを明記する

## 重要ガードレール

- JSON 系は `Empty`、新規建物は `Example building` から始める
- `.timbermesh` だけで元 texture がそのまま出ると思わない
- `.mat` と `.png` の basename を分ける
- `MaterialCollection` は lower-case の正規化 key を優先する
- Blueprint に値が見えないなら C# や BepInEx へ進む前提で考える
- material 側、JSON 側、DLL 側を更新したらゲーム再起動で確認する
