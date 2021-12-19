# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Horse(scrapy.Item):
    race_id = scrapy.Field()
    res_num = scrapy.Field()
    start_num = scrapy.Field()
    hose_num = scrapy.Field()
    hose_name = scrapy.Field()
    sex = scrapy.Field()
    age = scrapy.Field()
    wei_ca = scrapy.Field()
    rid_name = scrapy.Field()
    time = scrapy.Field()
    pop = scrapy.Field()
    odds = scrapy.Field()
    hose_wei = scrapy.Field()
    wei_change = scrapy.Field()

class Race(scrapy.Item):
    race_id = scrapy.Field()
    clock = scrapy.Field()
    field = scrapy.Field()
    distance = scrapy.Field()
    r_or_l = scrapy.Field()
    weather = scrapy.Field()
    count = scrapy.Field()
    place = scrapy.Field()
    day = scrapy.Field()
    regulation = scrapy.Field()
