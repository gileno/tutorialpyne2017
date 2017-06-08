# -*- coding: utf-8 -*-
import scrapy


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
        title = response.xpath("//title/text()").extract_first()
        yield {
            'title': title
        }
