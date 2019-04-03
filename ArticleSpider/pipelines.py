# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from scrapy.exceptions import DropItem
import scrapy
import codecs
import json


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出
    def __init__(self):
        self.file = codecs.open('artcile.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


class JsonExpoterPipeline(object):
    # 调用scrapy提供的json exporter导出json文件
    def __init__(self):
        self.file = open("articalexpo.json", "wb")
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'zxj6131ming', 'artical_spider', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into article_spider(title,datetime,praise_num)
            value (%s,%s,%s)
        """
        self.cursor.execute(insert_sql, (item['title'], item['datetime'], item['praise_num']))
        self.conn.commit()


class ArticleImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['img_url']:
            print(image_url)
            yield scrapy.Request(image_url)

    # def item_completed(self, results, item, info):
    #     image_paths = [x["path"] for ok, x in results if ok]
    #     if not image_paths:
    #         raise DropItem("Item contains no image")
    #     item['image_paths'] = image_paths
    #     return item
