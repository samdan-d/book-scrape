import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes';

    def start_requests(self):
        urls = [
            
        ]