# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from test1_scrapy.items import Test1ScrapyItem

class Meesi2Spider(CrawlSpider):
    name = 'meesi2'
    allowed_domains = ['messilessblog.com']
    start_urls = ['http://messilessblog.com/']

    rules = (
        Rule(LinkExtractor(allow=r'http://messilessblog.com/page/\d/'), follow=True),
        Rule(LinkExtractor(allow=r'.+/\d{4}/\d{2}/\d{2}/.+'), callback="parse_item", follow=False)

    )

    def parse_item(self, response):
        title = response.xpath("//*[@id='posts']/article/div/header/h1/text()").get()
        create_time = response.xpath("//*[@id='posts']/article/div/header/div/span[1]/time/text()").get().strip()
        item = Test1ScrapyItem(title=title, create_time=create_time)
        yield item
