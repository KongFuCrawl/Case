import scrapy
# noinspection PyUnresolvedReferences
from Douban.items import DoubanItem  # 使用绝对导入


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = [f'https://movie.douban.com/top250?start={i}' for i in range(0, 250, 25)]

    def parse(self, response):
        movies = response.css('.grid_view li')
        for movie in movies:
            item = DoubanItem()

            item['name'] = movie.css('.title::text').get()
            item['link'] = movie.css('.hd a::attr(href)').get()
            item['rating'] = movie.css('.rating_num::text').get()
            item['image'] = movie.css('.pic img::attr(src)').get()




            yield item

