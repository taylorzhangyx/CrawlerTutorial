# -*- coding: utf-8 -*-
import scrapy


class ElecronicsSpider(scrapy.Spider):
    name = 'elecronics1'
    allowed_domains = ['www.olx.com.pk']
    start_urls = ['http://www.olx.com.pk/']

    def parse(self, response):
        pass
