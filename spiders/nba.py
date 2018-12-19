# -*- coding: utf-8 -*-
import scrapy

from projeto_teste.items import ProjetoTesteItem


class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ["https://www.basketball-reference.com/"]
    # start_urls = ["https://www.basketball-reference.com/friv/dailyleaders.fcgi?month=12&day=18&year=2018"]

    def __init__(self, month, day, year):
        self.start_urls=["https://www.basketball-reference.com/friv/dailyleaders.fcgi?month=%s&day=%s&year=%s" % (month, day, year)]

    def parse(self, response):
        for resp in response.xpath('//tr'):
            item = ProjetoTesteItem()
            if len(resp.xpath('td[@data-stat="player"]/a/text()').extract()) > 0:
                item['nome'] = resp.xpath('td[@data-stat="player"]/a/text()').extract()
                item['fg'] = resp.xpath('td[@data-stat="fg"]/text()').extract()
                item['fga'] = resp.xpath('td[@data-stat="fga"]/text()').extract()
                item['fg_pct'] = resp.xpath('td[@data-stat="fg_pct"]/text()').extract()
                item['fg3'] = resp.xpath('td[@data-stat="fg3"]/text()').extract()
                item['fg3a'] = resp.xpath('td[@data-stat="fg3a"]/text()').extract()
                item['fg3_pct'] = resp.xpath('td[@data-stat="fg3_pct"]/text()').extract()
                item['ft'] = resp.xpath('td[@data-stat="ft"]/text()').extract()
                item['fta'] = resp.xpath('td[@data-stat="fta"]/text()').extract()
                item['ft_pct'] = resp.xpath('td[@data-stat="ft_pct"]/text()').extract()
                item['orb'] = resp.xpath('td[@data-stat="orb"]/text()').extract()
                item['drb'] = resp.xpath('td[@data-stat="drb"]/text()').extract()
                item['trb'] = resp.xpath('td[@data-stat="trb"]/text()').extract()
                item['ast'] = resp.xpath('td[@data-stat="ast"]/text()').extract()
                item['stl'] = resp.xpath('td[@data-stat="stl"]/text()').extract()
                item['blk'] = resp.xpath('td[@data-stat="blk"]/text()').extract()
                item['tov'] = resp.xpath('td[@data-stat="tov"]/text()').extract()
                item['foul'] = resp.xpath('td[@data-stat="pf"]/text()').extract()
                item['points'] = resp.xpath('td[@data-stat="pts"]/text()').extract()


            yield item

        # for item in response.xpath('//tr'):
        #     a = item.xpath('td[@data-stat="pts"]/text()').extract()

        #     print (a)

            
        #pass
