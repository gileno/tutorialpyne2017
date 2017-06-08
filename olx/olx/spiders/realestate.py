# -*- coding: utf-8 -*-
import scrapy


class RealestateSpider(scrapy.Spider):
    name = 'realestate'
    allowed_domains = ['pe.olx.com.br']
    start_urls = [
        'http://pe.olx.com.br/imoveis/venda/apartamentos/'
    ]

    def parse(self, response):
        items = response.xpath(
            '//ul[@id="main-ad-list"]/li[not(contains(@class, "list_native"))]'
        )
        for item in items:
            url = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)
    
    def parse_detail(self, response):
        yield {
            'title': response.xpath("//title/text()").extract_first()
        }
