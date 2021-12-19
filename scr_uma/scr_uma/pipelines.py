# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import psycopg2
from dotenv import load_dotenv
from scr_uma.items import Horse, Race
import scrapy

class ScrUmaPipeline:
    def open_spider(self, spider):
        load_dotenv()
        url = os.getenv('POSTGRESQL_URL')
        self.conn = psycopg2.connect(url)

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item: scrapy.Item, spider):
        """
        Pipeline にデータが渡される時に実行される
        item に spider から渡された item がセットされる
        """
        print(6)
        if item is Horse:
            print(7)
            sql= "INSERT INTO races \
                (race_id, res_num, start_num, hose_num, hose_name, sex, age, wei_ca, rid_name, time, pop, odds, hose_wei, wei_change) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;"
            curs = self.conn.cursor()
            curs.execute(sql, (item['race_id'], item['res_num'], item['start_num'], item['hose_num'], item['hose_name'], item['sex'], item['age'], 
                item['wei_ca'], item['rid_name'], item['time'], item['pop'], item['odds'], item['hose_wei'], item['wei_change']))
            self.conn.commit()
            print(8)
            return item
        
        if item is Race:
            sql= "INSERT INTO inf \
                (race_id, , clock, field, distance, r_or_l, weather, count, place, day, regulation) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;"
                
            curs = self.conn.cursor()
            curs.execute(sql, (item['race_id'], item['clock'], item['field'], item['distance'], item['r_or_l'], item['weather'], item['count'], 
                item['place'], item['day'], item['regulation']))
            self.conn.commit()
            return item