# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    datetime = scrapy.Field()
    praise_num = scrapy.Field()
    content = scrapy.Field()
    img_url=scrapy.Field()
    url_object_id=scrapy.Field()