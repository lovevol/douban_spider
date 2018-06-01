# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DouBanBookItem(scrapy.Item):
    name = scrapy.Field()
    pub = scrapy.Field()
    star = scrapy.Field()
    desc = scrapy.Field()
    category = scrapy.Field()
