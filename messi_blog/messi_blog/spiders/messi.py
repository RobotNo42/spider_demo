# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from messi_blog.items import MessiBlogItem


class MessiSpider(CrawlSpider):
    name = 'messi'
    allowed_domains = ['robotno42.github.io']
    start_urls = ['https://robotno42.github.io']

    rules = (
        Rule(LinkExtractor(allow=r'https://robotno42.github.io/page/\d/'), follow=True),
        Rule(LinkExtractor(allow=r'.+/\d{4}/\d{2}/\d{2}/.+'), callback="parse_item", follow=False)

    )

    def parse_item(self, response):
        title = response.xpath("//*[@id='posts']/article/div/header/h1/text()").get()
        create_time = response.xpath("//*[@id='posts']/article/div/header/div/span[1]/time/text()").get().strip()
        item = MessiBlogItem(title=title, create_time=create_time)
        yield item

