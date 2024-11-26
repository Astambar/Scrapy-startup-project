# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuoteItem(scrapy.Item):
    # define the fields for your item here like:
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class TitleItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()

class NavItem(scrapy.Item):
    # define the fields for your item here like:
    nav = scrapy.Field()