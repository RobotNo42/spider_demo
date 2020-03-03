# -*- coding: utf-8 -*-
import os
from urllib import request
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class NewbeginPipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def open_spider(self, spider):
        print('爬虫开始')

    def process_item(self, item, spider):
        category = item['category']
        urls = item['urls']
        category_url = os.path.join(self.path, category)
        if not os.path.exists(category_url):
            os.mkdir(category_url)
        for url in urls:
            url_name = url.split('__')[-1]
            request.urlretrieve(url, os.path.join(category_url, url_name))
        return item

    def close_spider(self,spider):
        print('爬虫结束')
