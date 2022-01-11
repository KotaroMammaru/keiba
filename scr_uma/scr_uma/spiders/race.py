from scr_uma.items import Horse
from scr_uma.items import Race
import scrapy
from scr_uma.spiders.url_list import urls_list


class RaceSpider(scrapy.Spider):
    name = 'race'
    allowed_domains = ['race.netkeiba.com']
    urls = urls_list

    # sample_list = ['202109040805']
    # start_urls = ['https://race.netkeiba.com/race/result.html?race_id=' + p for p in sample_list]

    start_urls = ['https://race.netkeiba.com/race/result.html?race_id=' + p for p in urls]
    count = -1

    def parse(self, response):
        print("url取得\n\n")
        self.count = self.count + 1
        # id = url_list.urls_list[self.count]
        id = self.urls[self.count]
        raceId = int(id[2:4] + id[6:12])

        data = response.css('#page > div.RaceColumn01 > div > div.RaceMainColumn > div.RaceList_NameBox > div.RaceList_Item02 > div.RaceData01')

        clock = data.css('::text').get()
        if clock == None:
            print(2)
            print(str(raceId) + 'のレースはありません。')
            return
        
        clock = ment_clock(clock)

        field_and_distance = data.css('span:nth-child(1)::text').get().strip(' ')
        print(field_and_distance)
        field = ment_f_d(field_and_distance, 0)
        distance = ment_f_d(field_and_distance, 1)
        # print(data.split('('))
        r_or_l_and_wea = data.get().split('(')[1].split('<')[0].split('/ 天候:')
        r_or_l = ment_r_l(r_or_l_and_wea[0])
        weather = r_or_l_and_wea[1]

        data2 = response.css('#page > div.RaceColumn01 > div > div.RaceMainColumn > div.RaceList_NameBox > div.RaceList_Item02 > div.RaceData02')
        count = data2.css('span:nth-child(1)::text').get()
        count = ment_count(count)
        place = data2.css('span:nth-child(2)::text').get()
        day = data2.css('span:nth-child(3)::text').get()
        day = ment_day(day)
        regulation = data2.css('span:nth-child(4)::text').get()

        yield Race(
            race_id = raceId,
            clock = clock,
            field = field,
            distance = distance,
            r_or_l = r_or_l,
            weather = weather,
            count = count,
            place = place,
            day = day,
            regulation = regulation
        )


        for race in response.xpath('//*[@id="All_Result_Table"]/tbody/tr'):
            resNum = race.xpath('td[1]/div/text()').get()
            startNum = race.xpath('td[2]/div/text()').get()
            hoseNum = race.xpath('td[3]/div/text()').get()
            hoseName = race.xpath('td[4]/span/a/text()').get()
            sexAge = race.xpath('td[5]/div/span/text()').get()
            weiCa = race.xpath('td[6]/div/span/text()').get()
            ridName = race.xpath('td[7]/a/text()').get()
            time = race.xpath('td[8]/span/text()').get()
            pop = race.xpath('td[10]/span/text()').get()
            odds = race.xpath('td[11]/span/text()').get()
            hoseWei = race.xpath('td[15]/text()').get()
            weiChange = race.xpath('td[15]/small/text()').get()

            print(5)
            
            
            yield Horse(
                race_id = raceId,
                res_num = ment_res_num(resNum),
                start_num = ment_start_num(startNum),
                hose_num = ment_hose_num(hoseNum),
                hose_name = hoseName,
                sex = ment_sex_age(sexAge, 0),
                age = ment_sex_age(sexAge, 1),
                wei_ca = ment_wei_ca(weiCa),
                rid_name = ment_rid_name(ridName),
                time = ment_time(time),
                pop = ment_pop(pop),
                odds = float(odds),
                hose_wei = ment_hose_wei(hoseWei),
                wei_change = ment_wei_change(weiChange)
            )

def ment_clock(clock):
    clock = clock.replace('\n', '').split(':')[0]
    return int(clock)
def ment_f_d(f_d, num):
    field = f_d[0]
    distance = f_d.strip(f_d[0]).strip('m')

    if field == '芝':
        field = 0
    else:
        field = 1

    if num == 0:
        return field
    
    else:
        return int(distance)

def ment_r_l(r_l):
    r_l = r_l[0]
    if r_l == '右':
        r_l = 0
    else:
        r_l = 1
    
    return r_l

def ment_count(count):
    count = count.strip('回')
    return int(count)

def ment_day(day):
    day = day.strip('日目')
    return int(day)

def ment_res_num(num):
    if num is str:
        num = int(num)
    return num

def ment_start_num(num):
    return int(num)

def ment_hose_num(num):
    return int(num)

def ment_sex_age(sexAge, num):
    sexAge = sexAge.replace("\n", "")
    sex = sexAge[0]

    if sex == '牡':
        sex = 0
    else:
        sex = 1
    
    age = int(sexAge[1])

    if num == 0:
        return sex

    return age

def ment_wei_ca(wei):
    return float(wei)

def ment_rid_name(name):
    return name.replace(" ", "")

def ment_time(min):
    pre_sec = min.split(':')
    sec = float(pre_sec[0])*60 + float(pre_sec[1])

    return sec

def ment_pop(num):
    if num == None:
        num = 15
    else:
        num = int(num)
    
    return num

def ment_hose_wei(weight):
    return int(weight.replace(" ", ""))

def ment_wei_change(prechange):
    prechange = prechange.replace('(', '')
    change = prechange.replace(')', '')

    return int(change)



