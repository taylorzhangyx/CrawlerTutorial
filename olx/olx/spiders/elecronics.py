# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from olx.items import OlxItem
class ElectronicsSpider(CrawlSpider):
    name = "electronics"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = [
        'https://sfbay.craigslist.org/d/furniture/search/fua'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.next',)),
             callback="parse_item",
             follow=False),)

    def parse_item(self, response):
        print('Processing..' + response.url)
        itemlinks = response.css('.result-title::attr(href)').getall()
        for item in itemlinks:
            yield scrapy.Request(item, callback=self.processItem)

    def processItem(self, response):
        title = response.xpath('//span[@id="titletextonly"]/text()').get()
        price = response.xpath('//span[@class="price"]/text()').get()
        item = OlxItem()
        item['title'] = title
        item['price'] = price
        yield item
