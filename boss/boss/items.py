# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    # define the fields for your item here like:
    job_name = scrapy.Field()
    salary = scrapy.Field()
    working_address = scrapy.Field()
    working_age = scrapy.Field()
    education = scrapy.Field()
    detail = scrapy.Field()
