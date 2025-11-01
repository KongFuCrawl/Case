# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    rating = scrapy.Field()
    image = scrapy.Field()




