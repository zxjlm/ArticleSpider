# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join



class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    datetime = scrapy.Field()
    praise_num = scrapy.Field()
    content = scrapy.Field()
    img_url = scrapy.Field()
    url_object_id = scrapy.Field()


class LagouJobItemLoader(ItemLoader):
    default_output_processor = TakeFirst()



class LagouJob(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    salary = scrapy.Field()
    job_city = scrapy.Field()
    work_years = scrapy.Field()
    degree_need = scrapy.Field()
    job_type = scrapy.Field()
    publish_time = scrapy.Field()
    job_advantage = scrapy.Field()
    job_desc = scrapy.Field()
    job_addr = scrapy.Field()
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    tags = scrapy.Field()
    crawl_time = scrapy.Field()
