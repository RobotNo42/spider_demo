# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from carhome.settings import IMAGES_STORE
import os


# 因为ImagesPipeline的下载位置是full/，而我们想要的不是这样，所以我们要自己写一个
class BMWImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 这个方法是在发送下载请求之前调用，其实这个方法本身就是去发送下载请求的，主要是让其他方法得到item的值
        request_objs = super(BMWImagesPipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        # 这个方法是图片在将要被存储的时候调用，来获取图片的存储路径
        path = super(BMWImagesPipeline, self).file_path(request, response, info)
        category = request.item.get('category')
        image_store = IMAGES_STORE
        category_path = os.path.join(image_store, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_name = path.replace("full/", "")
        image_path = os.path.join(category_path, image_name)
        return image_path
