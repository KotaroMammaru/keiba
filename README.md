# keiba

<h1>概要</h1>
<p>Scrapyを使用して「ネット競馬」から各レース情報を引っ張る。それをPostgreSQLに保存する。</p>
<p>https://nar.netkeiba.com/race/result.html?race_id=202254010901&rf=race_list の各馬ごとのデータを得る。</p>
<p>write_json.pyで保存していたデータをJSON形式でLocalに引っ張る</p>
<h1>環境</h1>
<p>python 3.0</p>
<h1>必須ライブラリ</h1>
<p>scrapy, os, psycopg2, dotenv, json</p>
<h1>手順</h1>
<p>　git clone https://github.com/KotaroMammaru/keiba.git　</p>
<p>write_json.py と同じ階層に.emvを作成し、　POSTGRESQL_URL = '自分のpostgreSQLURL'　を記入</p>
<p>cd scr_uma</p>
<p>scrapy crawl race　でスクレイピング実行</p>
<p>cd ..　でさっきのディレクトリに戻り、　python write_json.py　でJSON形式データを得られる</p>
