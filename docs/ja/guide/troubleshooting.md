# トラブルシュート

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
