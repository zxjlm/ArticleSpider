# -*- coding:utf-8 -*-
__author__ = 'harumonia'

import requests

import cookiejar as cookielib

import re


def zhihulogin(account,pwd):
    if re.match("1\d{10}",account):
        print("shoujihaomadenglu")
        url_post='https://www.zhihu.com/signin'
    req=requests.get()