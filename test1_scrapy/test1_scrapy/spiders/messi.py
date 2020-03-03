# -*- coding: utf-8 -*-
import scrapy
from test1_scrapy.items import Test1ScrapyItem


class MessiSpider(scrapy.Spider):
    name = 'messi'
    allowed_domains = ['messilessblog.com']
    start_urls = ['http://messilessblog.com/']
    base_url = "http://messilessblog.com"

    def parse(self, response):
        articles = response.xpath("//article[@class='post post-type-normal']")
        for article in articles:
            title = article.xpath(".//a[@class='post-title-link']//text()").get()
            item = Test1ScrapyItem(title=title)
            # 取得标题
            yield item
        next_url = response.xpath("//*[@id='content']/nav/a[last()]/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_url+next_url, callback=self.parse)
