# -*- coding:utf-8 -*-
__author__ = 'harumonia'

import requests
from scrapy import Selector


def get_id():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}

    for i in range(1, 3):
        req = requests.get("https://www.xicidaili.com/nn/{0}".format(i), headers=headers)

        # print(req.text)
        sel = Selector(text=req.text)

        raw = (sel.css('#ip_list tr'))
        for ip_raw in raw[1:]:
            tdcss = ip_raw.css('td')
            ip = tdcss[1].css('::text').extract()[0]
            port = tdcss[2].css('::text').extract()[0]
            print("{0}:{1}".format(ip, port))


if __name__ == '__main__':
    get_id()
