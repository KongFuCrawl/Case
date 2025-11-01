import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名，执行爬虫时使用：scrapy crawl 爬虫名
    name = "baidu"
    # 允许爬去的域名：scrapy grnspider baidu www.baidu.com
    allowed_domains = ["www.baidu.com"]
    # 起始的URL地址
    start_urls = ["https://www.baidu.com"]

    # 解析提取数据的函数
    def parse(self, response):
        """解析提取数据"""
        item = {}

        item['title'] = response.xpath('/html/head/title/text()').get()
        print(item)
