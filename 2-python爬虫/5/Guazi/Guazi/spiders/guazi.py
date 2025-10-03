# Guazi/spiders/guazi.py

import scrapy
from ..items import GuaziItem


class GuaziSpider(scrapy.Spider):
    name = "guazi"
    allowed_domains = ["www.guazi.com"]
    start_urls = ["https://www.guazi.com/langfang/buy/o1/"]

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Referer': 'https://www.guazi.com/',
        }

        # 尝试多个可能的URL
        urls = [
            "https://www.guazi.com/langfang/buy/o1/",
            "https://www.guazi.com/langfang/buy/o1",
            "https://m.guazi.com/langfang/buy/o1/",  # 移动端
        ]

        for url in urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse, meta={'original_url': url})

    def parse(self, response):
        # 调试信息
        self.logger.info(f"请求URL: {response.meta.get('original_url')}")
        self.logger.info(f"实际URL: {response.url}")
        self.logger.info(f"状态码: {response.status}")

        # 检查页面标题
        title = response.xpath('//title/text()').get()
        self.logger.info(f"页面标题: {title}")

        # 保存响应内容用于分析
        filename = f"debug_{response.url.split('//')[1].replace('/', '_')}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        self.logger.info(f"已保存响应内容到: {filename}")

        # 尝试解析车辆列表
        li_list = response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        self.logger.info(f"找到 {len(li_list)} 个车辆列表项")

        if len(li_list) == 0:
            self.logger.warning("未找到车辆列表，可能被重定向或页面结构变化")
            # 尝试其他可能的选择器
            alternative_selectors = [
                '//div[contains(@class, "car-list")]//li',
                '//div[@class="list-wrap"]//li',
                '//ul[contains(@class, "list")]/li'
            ]
            for selector in alternative_selectors:
                items = response.xpath(selector)
                if len(items) > 0:
                    self.logger.info(f"使用选择器 '{selector}' 找到 {len(items)} 个元素")
                    break

        for li in li_list:
            item = GuaziItem()
            item['name'] = li.xpath('./a/h2/text()').get()
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').get()
            item['link'] = li.xpath('./a/@href').get()
            yield item
