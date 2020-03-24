# -*- coding: utf-8 -*-
import scrapy


class QsSpider(scrapy.Spider):
    name = 'qs'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']

    def parse(self, response):
        pass
