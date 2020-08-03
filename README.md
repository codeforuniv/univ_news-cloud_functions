## 主タスク
<スプレッドシート>
- https://docs.google.com/spreadsheets/d/1yra4f5-MeGzrRkp8QNdxsAQVxvqpcBQw0gi32g8ow-0/edit?usp=sharing
- 大学候補と完了リストを更新していく
- 目標は100大学

<ページ>
- [x] トップページ
- [x] コロナ関連ページ
- [ ] 研究ページ

## 参考資料

- https://cloud.google.com/source-repositories/docs/integrating-with-cloud-build?hl=ja
- https://qiita.com/mitonattou919/items/1dd4c2e74f5023b337cc

1. Github で Cloud Functions にあげたい関数を入れたリポジトリを作る

   - ローカル開発するときに環境を合わせたいので、ルートに環境用のファイルを入れて関数のファイルは/src の中に入れる

2. Github のリポジトリと Cloud Source Repositories をミラーリングする

   - Github の master に push すると Cloud Source Repositories に反映される

3. Cloud Source Repositories の変更をトリガーとして Cloud Functions をデプロイする

   - ルートの cloudbuild.yaml を編集することで、リポジトリに変更があったときに何をするのかを記述する
   - http ではなくトピック指定にすれば後述の Scheduler から定期実行してくれる
   - functions のデプロイのための yaml
     - https://cloud.google.com/cloud-build/docs/deploying-builds/deploy-functions?hl=ja

4. Cloud Scheduler からトピックを実行する
