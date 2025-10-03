# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # define the fields for your item here like:
    # 汽车名称 ， 价格 ， 连接
    name = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()

# 相当于你定义了一个字典，值给了key，没有给Value
# {'name':'', 'price':'', 'link':''}

