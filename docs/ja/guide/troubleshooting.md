# トラブルシュート

## JSON patch が効かない

確認すること:

- patch ファイルの path が元の game Blueprint path と一致しているか
- content mod として正しいテンプレートから始めているか
- 変更後に Timberborn を完全再起動したか

## Blueprint に値が見つからない

この場合は、純粋な content mod の範囲を超えている可能性が高いです。

値や挙動が Blueprint に露出していないなら、hidden な JSON key を推測するのではなく、C# DLL MOD や BepInEx / Harmony への移行を検討します。

## Material が Repository に見つからない

確認すること:

- `MaterialCollection` があるか
- built mod 側に bundle があるか
- material key が runtime の正規化 key と一致しているか

## Failed to load asset が出る

よくある原因:

- `MaterialCollection` の path 形式が違う
- bundle 内の正規化 key と参照がずれている
- `.mat` と `.png` が同じ basename になっている

## `.timbermesh` 化後に見た目がガビガビになる

この場合は、ルートAではなくルートBに進むべきケースが多いです。

メッシュが単純で、見た目の情報が画像に強く依存しているなら、built-in material への無理な置き換えは避けます。

## ゲーム内で古い状態のまま見える

custom material や AssetBundle を更新したら、Timberborn を完全終了してから再起動してください。

## ゲーム内設定パネルが欲しい

これは static JSON だけでは足りないサインです。

ゲーム内トグル、通知、Save ボタンからの JSON 生成が必要なら、C# DLL / UI MOD へ進みます。
