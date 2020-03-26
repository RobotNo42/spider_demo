# -*- coding: utf-8 -*-
import scrapy
from blog_spider.items import BlogSpiderItem


class MessiSpider(scrapy.Spider):
    name = 'messi'
    allowed_domains = ['messiless.club']
    start_urls = ['http://messiless.club/']

    def parse(self, response):

