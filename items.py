# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class CsItem(scrapy.Item):
    CId = scrapy.Field()
    CName = scrapy.Field()
    NPrice = scrapy.Field()  #最新价
    UpDown = scrapy.Field()  #涨跌
    Range = scrapy.Field()   #涨跌幅
    Volume = scrapy.Field()  #成交量
    Transaction = scrapy.Field() #成交额
    CloseY = scrapy.Field()  #昨收
    OpenT = scrapy.Field()   #今开
    HPrice  = scrapy.Field()  #最高价
    LPrice  = scrapy.Field()  #最低价
    PE  = scrapy.Field()   #市盈率
    Value = scrapy.Field() #市值


