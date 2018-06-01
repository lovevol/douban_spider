# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import requests


class DoubanSpiderPipeline(object):

    def process_item(self, item, spider):
        data = dict(item)
        requests.post(url='http://localhost:8000/books/', json=data)
        return item
