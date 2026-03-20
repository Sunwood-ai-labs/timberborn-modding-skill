# ルート選定

## ルートA: Timberborn built-in material を使う

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

## ルートB: custom texture を AssetBundle で持ち込む

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

## 重要ガードレール

- `.timbermesh` だけで元 texture がそのまま出ると思わない
- `.mat` と `.png` の basename を分ける
- `MaterialCollection` は lower-case の正規化 key を優先する
- material 側を更新したらゲーム再起動で確認する
