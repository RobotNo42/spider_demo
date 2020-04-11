# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss.items import BossItem


class BsSpider(CrawlSpider):
    name = 'bs'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101210100/?query=python&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+\?query=python&page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'.+job_detail/.+\.html'), callback='parse_boss', follow=False)
    )

    def parse_boss(self, response):
        job_name = response.xpath("//div[@class='job-banner']//div[@class='name']/h1/text()").get().strip()
        company = response.xpath("//div[@class='detail-content']/div[4]//div[@class='name']/text()").get().strip()
        salary = response.xpath("//div[@class='job-banner']//div[@class='name']/span/text()").get().strip()
        working_address = response.xpath("//div[@class='job-banner']//div[@class='info-primary']/p//text()").getall()[0]
        working_age = response.xpath("//div[@class='job-banner']//div[@class='info-primary']/p//text()").getall()[1]
        education = response.xpath("//div[@class='job-banner']//div[@class='info-primary']/p//text()").getall()[2]
        detail = response.xpath("//div[@class='job-box']//div[@class='job-detail']//div[@class='text']/text()").get()
        item = BossItem(job_name=job_name, company=company, salary=salary, working_address=working_address,
                        working_age=working_age, education=education, detail=detail)
        print(item)
        yield item
