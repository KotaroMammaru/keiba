# keiba

## 概要
Scrapyを使用して「ネット競馬」から各レース情報を引っ張る。それをPostgreSQLに保存する。

1．https://nar.netkeiba.com/race/result.html?race_id=202254010901&rf=race_list の各馬ごとのデータを得る。

2．それをそのまま、postgreSQLにぶち込む（ここまですべてScrapy）

3．write_json.pyで保存していたデータをJSON形式でLocalに引っ張る

以降、AIを開発しようとしたが、データが少なすぎて断念。

## 環境
python 3.0

HerokuのpostgreSQLサーバー

このDBは容量が1万行であるため、今回のテーブル構造ではすぐキャパオーバーであった。
### 必須ライブラリ
scrapy, os, psycopg2, dotenv, json
### 手順
```
git clone https://github.com/KotaroMammaru/keiba.git
```
write_json.py と同じ階層に.emvを作成し、
```
POSTGRESQL_URL = '自分のpostgreSQLURL'
```
を記入
```
cd scr_uma

scrapy crawl race
```
でスクレイピング実行
```
cd ..
```
でさっきのディレクトリに戻り、
```
python write_json.py
```
でJSON形式データを得られる。
