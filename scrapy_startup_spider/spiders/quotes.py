import scrapy
from scrapy_startup_spider.items import QuoteItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    meta_html = '//html/@lang'
    break_requests = False
    def start_requests(self):
        i = 0
        while True:
            if self.break_requests:
                break
            url_page = f'http://quotes.toscrape.com/page/{i+1}/' 
            i += 1
            yield scrapy.Request(url=url_page, callback=self.parse)

    def parse(self, response):
        quotes = response.css('div.quote')
        if bool(quotes):
            for quote_bloc in quotes:
                yield QuoteItem(text=quote_bloc.css('span.text::text').get(), 
                                author=quote_bloc.css('small.author::text').get(),
                                tags=quote_bloc.css('a.tag::text').getall())
            else:
                self.break_requests = True
                
                
                
