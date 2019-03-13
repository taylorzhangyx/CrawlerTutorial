# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class ElectronicsSpider(CrawlSpider):
    name = "electronics"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = [
        'https://sfbay.craigslist.org/d/furniture/search/fua'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.next',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)
        itemsTitle = response.css('.result-title::text').getall()
        for item in itemsTitle:
            yield scrapy.Request(item, callback = self.processItem)
