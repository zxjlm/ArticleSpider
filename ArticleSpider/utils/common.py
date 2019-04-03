# -*- coding:utf-8 -*-
import hashlib

__author__ = 'harumonia'

def get_md5(url):
    if isinstance(url,str):
        url=url.encode("utf-8")
    m=hashlib.md5()
    m.update(url)
    return m.hexdigest()

if __name__ == '__main__':
    url="jobbole.com"
    url1=get_md5(url.encode("utf-8"))
    print(url1)