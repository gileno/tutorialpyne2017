# -*- coding: utf-8 -*-
import scrapy


class VideosSpider(scrapy.Spider):
    name = 'videos'
    allowed_domains = ['www.pycursos.com']
    start_urls = ['http://www.pycursos.com/videos/']

    def parse(self, response):
        categories = response.css('.sidebar-widget .list-group-item')
        for category in categories:
            href = category.xpath('.//@href').extract_first()
            url = 'https://www.pycursos.com' + href
            yield scrapy.Request(
                url=url, callback=self.parse_category
            )
    
    def parse_category(self, response):
        links = response.xpath(
            "//div[contains(@class, 'news-item')]//a[contains(@class, 'btn')]"
        )
        for link in links:
            href = link.xpath('.//@href').extract_first()
            url = 'https://www.pycursos.com' + href
            yield scrapy.Request(
                url=url, callback=self.parse_video,
                meta={'category': response.xpath('/html/body/div[3]/div/div/div[1]/h2').extract_first()}
            )

    def parse_video(self, response):
        yield {
            'title': response.xpath('//title/text()').extract_first(),
            'category': response.meta['category']
        }
