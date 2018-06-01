""" 
douban.py
Copyright 2011-2018 Qunhe Tech, all rights reserved.
Qunhe PROPRIETARY/CONFIDENTIAL, any form of usage is subject to approval.

@Author: tianming
@created: 6/1/18
"""
import scrapy
from scrapy import Request

from douban_spider.items import DouBanBookItem
URL_SET = set()

class DouBanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["www.douban.com"]
    start_urls = [
        "https://book.douban.com/tag/算法/"
    ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = "https://book.douban.com/tag/算法/"
        yield Request(url, headers=self.headers)

    def parse(self, response):
        for book in response.xpath('//ul[@class = "subject-list"]/li[@class="subject-item"]'):
            item = DouBanBookItem()
            name1 = book.xpath('.//div[@class="info"]/h2/a/text()').extract_first(default='').rstrip('\n').lstrip('\n').strip()
            name2 = book.xpath('.//div[@class="info"]/h2/a/span/text()').extract_first(default='').rstrip('\n').lstrip('\n').strip()
            item['name'] = name1 + name2
            item['pub'] = book.xpath('.//div[@class="info"]/div[@class="pub"]/text()').extract_first(default='').rstrip('\n').lstrip('\n').strip()
            item['star'] = book.xpath('.//div[@class="info"]/div[@class="star clearfix"]/span[@class="rating_nums"]/text()').\
                extract_first(default=0)
            item['desc'] = book.xpath('.//div[@class="info"]/p/text()').extract_first(default='').rstrip('\n').lstrip('\n').strip()
            item['category'] = response.xpath('//div[@id="content"]/h1/text()').extract_first(default='')
            yield item

        for url in response.xpath('//div[@class="paginator"]/a/@href').extract():
            if url is not None:
                url = 'https://book.douban.com' + url
                if url not in URL_SET:
                    URL_SET.add(url)
                    yield Request(url, callback=self.parse, dont_filter=True, headers=self.headers)


