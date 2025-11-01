import scrapy
from ..items import BooksItem

class BooksSpider(scrapy.Spider):
    name = "books2"
    allowed_domains = ["books.toscrape.com"]

    # 1.删掉start_urls变量
    # 2. 重写start_requests()方法
    def start_requests(self):
        """一次性生成所有要抓取的URL地址，一次性交给调度器入队列"""
        for i in range(1, 5):
            url = 'http://books.toscrape.com/catalogue/page-{}.html'.format(i)
            # 交给调度器入队列，并指定解析函数
            yield scrapy.Request(url=url, callback=self.parse)


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



