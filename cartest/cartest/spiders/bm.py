# -*- coding: utf-8 -*-
import scrapy
from urllib import request

class BmSpider(scrapy.Spider):
    name = 'bm'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['http://car.autohome.com.cn/']
    first_urls = 'https://car3.autoimg.cn/cardfs/product/g2/M07/54/1E/1024x0_1_q95_autohomecar__ChsEmlzuM72AEHIfAAi_GkUdbYE147.jpg'

    def parse(self, response):
        request.urlretrieve(self.first_urls, 'hahah.jpg')
