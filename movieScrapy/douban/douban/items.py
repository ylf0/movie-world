# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Demo1Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class douban(Item):
    order = Field()
    title = Field()
    info = Field()
    star = Field()
    votes = Field()
    quote = Field()
    poster_url = Field()