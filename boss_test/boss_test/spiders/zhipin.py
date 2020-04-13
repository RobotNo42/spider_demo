# -*- coding: utf-8 -*-
import scrapy


class ZhipinSpider(scrapy.Spider):
    name = 'zhipin'
    allowed_domains = ['zhipin.com']
    start_urls = ['http://zhipin.com/']

    def parse(self, response):
        pass
