# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class DoubanSpiderPipeline(object):

    def process_item(self, item, spider):
        with open('data_1.json', 'a') as f:
            json.dump(dict(item), f, ensure_ascii=False)
            f.write(',\n')
        return item
