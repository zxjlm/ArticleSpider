# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LagouJobItemLoader,LagouJob


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/']                 #shi否有证书

    rules = (
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'zhaopin/.*'),  follow=True),
        Rule(LinkExtractor(allow=r'gongsi/\d+.hrml'),  follow=True),
    )

    def parse_job(self, response):
        #解析职位
        itemloader=LagouJobItemLoader(item=LagouJob,response=response)

        itemloader.add_css()

        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return itemloader.load_item()
