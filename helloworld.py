import scrapy

class HelloWorld(scrapy.Spider):

    name = 'helloworld'
        
    start_urls = ['http://www.gilenofilho.com.br']

    def parse(self, response):
        self.log('Hello World')
        self.log(response.body)