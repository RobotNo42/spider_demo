# -*- coding: utf-8 -*-
import scrapy


class HaoSpider(scrapy.Spider):
    name = 'hao'
    allowed_domains = ['henhenlu.com']
    start_urls = ['http://henhenlu.com/']

    def parse(self, response):
        pass
