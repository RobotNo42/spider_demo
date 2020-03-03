# -*- coding: utf-8 -*-
import scrapy
from newbegin.items import NewbeginItem
from scrapy.pipelines.images import ImagesPipeline


class BmSpider(scrapy.Spider):
    name = 'bm'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/135.html']

    def parse(self, response):
        uiboxs = response.xpath("//div[@class='uibox']")[1:]
        for box in uiboxs:
            category = box.xpath("./div[@class='uibox-title']/a/text()").get()
            urls = box.xpath(".//ul/li/a/img/@src").getall()
            urls = list(map(lambda x: response.urljoin(x), urls))
            yield NewbeginItem(category=category, image_urls=urls)


class BMImagesPipeline(ImagesPipeline):
    pass
