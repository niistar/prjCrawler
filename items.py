# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjetoTesteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nome = scrapy.Field()
    fg = scrapy.Field()
    fga = scrapy.Field()
    fg_pct = scrapy.Field()
    fg3 = scrapy.Field()
    fg3a = scrapy.Field()
    fg3_pct = scrapy.Field()
    ft = scrapy.Field()
    fta = scrapy.Field()
    ft_pct = scrapy.Field()
    orb = scrapy.Field()
    drb = scrapy.Field()
    trb = scrapy.Field()
    ast = scrapy.Field()
    stl = scrapy.Field()
    blk = scrapy.Field()
    tov = scrapy.Field()
    foul = scrapy.Field()
    points = scrapy.Field()

    pass
