import scrapy


class BaiduSpider(scrapy.Spider):
    #爬虫名:执行爬虫时使用：scrapy crawl 爬虫名
    name = "baidu"
    #允许爬取的域名：scrapy genspider baidu www.baidu.com
    allowed_domains = ["www.baidu.com"]
    # 起始的URL地址
    start_urls = ["https://www.baidu.com"]

    # 解析提取数据函数
    def parse(self, response):
        """解析提取数据 - 百度一下，你就知道"""
        item = {}
        #response.xpath()打印结果：{'title': [<Selector query='/html/head/title/text()' data='百度一下，你就知道'>]}
        #item['title'] = response.xpath('/html/head/title/text()')

        #.get()或者extract()打印结果是：{'title': '百度一下，你就知道'}
        #item['title'] = response.xpath('/html/head/title/text()').extract()

        #extract_first()打印结果是：{'title': '百度一下，你就知道'}
        item['title'] = response.xpath('/html/head/title/text()').extract_first()

        #打印不出结果错误语法格式
        #item['title'] = response.xpath('/html/head/title/text()').response.xpath()

        print(item)
