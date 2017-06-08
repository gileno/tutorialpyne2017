# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

from courses.items import Course


class UdacitySpider(scrapy.Spider):
    name = 'udacity'
    allowed_domains = ['www.udacity.com']
    start_urls = ['http://www.udacity.com/courses/all']

    def parse(self, response):
        courses = response.xpath(
            "//div[contains(@class,'course-list')]//h3/a"
        )
        for course in courses:
            url = course.xpath("./@href").extract_first()
            url = 'http://www.udacity.com' + url
            yield scrapy.Request(
                url=url, callback=self.parse_detail
            )
    
    def parse_detail(self, response):
        item_loader = ItemLoader(Course(), response)
        item_loader.default_output_processor = TakeFirst()
        item_loader.add_xpath('title', '//title/text()')
        yield item_loader.load_item()