# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from carhome.items import CarhomeItem

class BmSpider(CrawlSpider):
    name = 'bm'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/65.+'), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        category = response.xpath("//div[@class='uibox']/div[@class='uibox-title']/text()").get()
        detail_urls = response.xpath("//div[@class='uibox']/div[@class='uibox-con carpic-list03 border-b-solid']/ul/li//img/@src").getall()
        image_urls = list(map(lambda x: response.urljoin(x.replace('240x180_0_q95_c42_', '1024x0_1_q95_')), detail_urls))
        items = CarhomeItem(category=category, image_urls=image_urls)
        yield items
