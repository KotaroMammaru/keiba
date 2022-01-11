import json
import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv


load_dotenv()
url = os.getenv('POSTGRESQL_URL')
conn = psycopg2.connect(url)

cur = conn.cursor()

sql = 'SELECT race_id FROM inf WHERE distance > 2000'
cur.execute(sql)

rows = cur.fetchall()

id_sen = '('

for id in rows:
    id_sen = id_sen + str(id[0]) + ','

id_sen = id_sen[0:len(id_sen)-1] + ') ORDER BY race_id ASC, res_num ASC;'

sql = 'SELECT * FROM races WHERE race_id IN ' + id_sen

cur = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)

cur.execute(sql)
rows = cur.fetchall()

print(rows)
print('********** JSONファイルを書き出す **********')

# 辞書オブジェクト(dictionary)を生成
dict_res = []
for row in rows:
    dict_res.append(row._asdict())
# 辞書オブジェクトをstr型で取得して出力
print(json.dumps(dict_res, ensure_ascii=False, indent=2))

# 辞書オブジェクトをJSONファイルへ出力
with open('mydata.json', mode='wt', encoding='utf-8') as file:
    print(3)
    json.dump(dict_res, file, ensure_ascii=False, indent=2)

conn.close()