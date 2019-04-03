# -*- coding: utf-8 -*-
import re

import scrapy
from ArticleSpider.items import ArticlespiderItem
from scrapy.http import Request

from ArticleSpider.utils.common import get_md5


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    # allowed_domains = ['books.toscrape.com']
    # start_urls = ['http://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg']

    def parse(self, response):

        res_raw = response.css("#archive .floated-thumb")

        for foo in res_raw:
            url = foo.css(".archive-title::attr(href)").extract_first("")
            img_url = foo.css(".post-thumb img::attr(src)").extract_first("")
            yield Request(url=url, meta={"img_url": img_url}, callback=self.parse_details)

    def parse_details(self, response):
        news = ArticlespiderItem()

        img_url = response.meta.get("img_url", "")
        title = response.css(".entry-header h1::text").extract_first("")
        datetime = response.css(".entry-meta-hide-on-mobile::text").extract_first("").replace(" ·", "").strip()
        praise_num_str = response.css("#114676votetotal::text").extract_first("")
        if praise_num_str:
            praise_num = int(praise_num_str)
        else:
            praise_num = 0
        content = response.css(".entry p::text").extract()[0]

        news['title'] = title
        news['datetime'] = datetime
        news['praise_num'] = praise_num
        news['content'] = content
        news['img_url'] = [img_url]
        news['url_object_id'] = get_md5(img_url)

        yield news
