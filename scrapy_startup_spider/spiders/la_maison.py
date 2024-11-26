import scrapy
from scrapy_startup_spider.items import QuoteItem, TitleItem, NavItem

class LaMaisonPageListSpider(scrapy.Spider):
    name = "la_maison"
    start_urls = ["https://www.lamaison.fr/bricolage/outillage/outil-electroportatif.html"]  # URL initiale

    def parse(self, response):
        
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse_product
        )
        
    
    def parse_product(self, response):
        product_main = response.css('main')
        product_main_column = product_main.css('div.columns div.column.main')
        product_wrapper = product_main_column.css('div.products.wrapper.grid.products-grid')
        
        # product_info = product_grid.css('div[data-container="product-grid"]')[0]
        # product_link = product_info.css('a.product.photo::attr(href)')
        product_title = None
        product_brand = None
        product_price = None
        
        yield {
            'product_title' : product_title
        }