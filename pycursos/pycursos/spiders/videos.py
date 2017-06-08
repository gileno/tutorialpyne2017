# -*- coding: utf-8 -*-
import scrapy


class VideosSpider(scrapy.Spider):
    name = 'videos'
    allowed_domains = ['www.pycursos.com']
    start_urls = ['http://www.pycursos.com/videos/']

    def parse(self, response):
        pass
