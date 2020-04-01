# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from carhome.items import CarhomeItem

class BmSpider(CrawlSpider):
    name = 'bm'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/135.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/135.+'), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        category = response.xpath("//div[@class='uibox']/div[@class='uibox-title']").get()
        detail_urls = response.xpath("/html/body/div[2]/div/div[2]/div[7]/div/div[2]/div[2]/ul/li/a/img/@src").getall()
        detail_urls = list(map(lambda x: x.replace("240x180", "1024x0"), detail_urls))
        image_urls = list(map(lambda x: response.urljoin(x), detail_urls))
        items = CarhomeItem(category=category, image_urls=image_urls)
        yield items
