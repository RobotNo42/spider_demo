# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def start_requests(self):
        url = 'https://accounts.douban.com/j/mobile/login/basic'
        data = {
            'name': '18368723168',
            'password': '946971',
            'remember': 'true',
        }
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_page)

    def parse_page(self, response):
        url = 'https://www.douban.com/people/157823813/'
        yield scrapy.Request(url=url, callback=self.page)

    def page(self, response):
        url = 'https://www.douban.com/j/people/157823813/edit_signature'
        data = {
            'ck': '8vd1',
            'signature': '今天就是我'
        }
        yield scrapy.FormRequest(url=url, formdata=data)
