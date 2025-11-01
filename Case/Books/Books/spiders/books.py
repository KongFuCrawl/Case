import scrapy
from ..items import BooksItem

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    i = 1
    start_urls = ["http://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        li_list = response.xpath('//ol[@class="row"]/li')
        for li in li_list:
            # 给items.py中的BooksItem类做实例化
            item = BooksItem()
            # 书名
            item['name'] = li.xpath('.//h3/a/text()').get()
            # 价格
            item['price'] = li.xpath('.//div[@class="product_price"]/p/text()').get()

            # 在parse方法中添加链接提取
            item['link'] = response.urljoin(li.xpath('.//h3/a/@href').get())

            # 把抓取的数据提交给管道文件处理: yield item
            yield item

        # 生成下一页的地址，去交给调度器入队列
        if self.i < 50:
            self.i += 1
            print(f'====准备爬去第{self.i}页=====')
            url = 'http://books.toscrape.com/catalogue/page-{}.html'.format(self.i)
            # 把url交给调度器入队列
            yield scrapy.Request(url=url, callback=self.parse)

        else:
            print('===所有页面爬去完成！=====')

