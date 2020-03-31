# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MessiBlogItem(scrapy.Item):
    title = scrapy.Field()
    create_time = scrapy.Field()
