# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BsSpider(CrawlSpider):
    name = 'bs'
    allowed_domains = ['zhipin.com/hangzhou']
    start_urls = ['https://www.zhipin.com/c101210100/?query=python&page=1&ka=page-1']

    rules = (
        Rule(LinkExtractor(allow=r'.+query=python&page=\d+&ka=page-\d+'), follow=True),
        Rule(LinkExtractor(allow=r'.+ka=search_list_jname_\d+blank&lid=nlp.+'), callback='parse_boss', follow=False)
    )

    def parse_boss(self, response):

        item = {}

        yield item
