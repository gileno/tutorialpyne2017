# -*- coding: utf-8 -*-
import scrapy


class RealestateSpider(scrapy.Spider):
    name = 'realestate'
    allowed_domains = ['ma.olx.com.br']
    start_urls = [
        'http://ma.olx.com.br/imoveis/venda/apartamentos/'
    ]

    def parse(self, response):
        divs = response.xpath(
            "//div[@id='main-ad-list']"
        )
        divs = divs.xpath(
            ".//a[contains(@class,'OLXad-list-link')]"
        )
        for link in divs:
            yield scrapy.Request(
                url=link.xpath("./@href").extract_first(),
                callback=self.parse_detail
            )
    
    def parse_detail(self, response):
        yield {
            'title': response.xpath("//title/text()").extract_first()
        }
