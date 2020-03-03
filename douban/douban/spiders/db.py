# -*- coding: utf-8 -*-
import scrapy
# 更改豆瓣个性签名


class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def start_requests(self):
        url = 'https://accounts.douban.com/j/mobile/login/basic'
        data = {
            'name': '18368723168',
            'password': '946971',
            'remember': 'true',
        }
        request = scrapy.FormRequest(url, formdata=data, callback=self.parse_page)
        yield request

    def parse_page(self, response):
        url = 'https://www.douban.com/people/157823813/'
        request = scrapy.Request(url=url, callback=self.page,)
        yield request

    def page(self, response):
        ck = response.xpath("//*[@id='edit_signature']/form/div/input[@name='ck']/@value").get()
        formdata = {
            'ck': ck,
            'signature': 'wo am ill'
        }
        yield scrapy.FormRequest(url='https://www.douban.com/j/people/157823813/edit_signature', formdata=formdata)