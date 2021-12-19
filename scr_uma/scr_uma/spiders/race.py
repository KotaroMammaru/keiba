from scr_uma.items import Horse
import scrapy
# from url_list


class RaceSpider(scrapy.Spider):
    name = 'race'
    allowed_domains = ['race.netkeiba.com']

    sample_list = ['202109040805']
    start_urls = ['https://race.netkeiba.com/race/result.html?race_id=' + p for p in sample_list]

    # start_urls = ['https://race.netkeiba.com/race/result.html?race_id=' + p for p in url_list.urls_list]
    count = -1

    def parse(self, response):
        print(1)
        self.count = self.count + 1
        # id = url_list.urls_list[self.count]
        id = self.sample_list[self.count]
        raceId = id[2:4] + id[6:12]

        data = response.xpath('//*[@id="page"]/div[2]/div/div[1]/div[3]/div[2]')
        
        time = data.xpath('text()[1]').extract()
        if time == []:
            print(2)
            print(raceId + 'のレースはありません。')
            return
            
        fi_dis = data.xpath('span[1]').extract()
        # data_2 = data.xpath('div.RaceData02::text').get()
        print(3)
        print(time)
        print(fi_dis)
        print(4)

        for race in response.xpath('//*[@id="All_Result_Table"]/tbody/tr'):
            resNum = race.xpath('td[1]/div/text()').get()
            print(resNum)
            startNum = race.xpath('td[2]/div/text()').get()
            print(startNum)
            hoseNum = race.xpath('td[3]/div/text()').get()
            print(hoseNum)
            hoseName = race.xpath('td[4]/span/a/text()').get()
            print(hoseName)
            sexAge = race.xpath('td[5]/div/span/text()').get()
            print(sexAge)
            weiCa = race.xpath('td[6]/div/span/text()').get()
            print(weiCa)
            ridName = race.xpath('td[7]/a/text()').get()
            print(ridName)
            time = race.xpath('td[8]/span/text()').get()
            print(time)
            pop = race.xpath('td[10]/span/text()').get()
            print(pop)
            odds = race.xpath('td[11]/span/text()').get()
            print(odds)
            hoseWei = race.xpath('td[15]/text()').get()
            print(hoseWei)
            weiChange = race.xpath('td[15]/small/text()').get()
            print(weiChange)

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

def ment_res_num(num):
    if num is str:
        num = int(num)
    return num

def ment_start_num(num):
    return int(num)

def ment_hose_num(num):
    return int(num)

def ment_sex_age(sexAge, num):
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



