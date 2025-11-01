"""
    Ajax动态数据抓取 - 小米应用商店聊天社交分类下的应用信息

"""


import requests
import json
import time
import random
from fake_useragent import UserAgent

class xiaomiSpider:
    def __init__(self):
        self.url = 'https://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'

    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        response = requests.get(url, headers=headers).text
        # json.loads() : 把json格式的字符串转为python数据类型

        html = json.loads(response)
        # 开始数据解析提取
        self.parse_html(html)

    def parse_html(self, html):
        # 数据解析提取
        for one_app_dict in html['data']:
            item = {}
            item['name'] = one_app_dict['displayName']
            item['type'] = one_app_dict['level1CategoryName']
            item['link'] = one_app_dict['packageName']
            print(item)

    def run(self):
        for i in range(3):
            page_url = self.url.format(i)
            self.get_html(url=page_url)
            # 控制数据抓取频率
            time.sleep(random.randint(1, 3))

if __name__ == '__main__':
    spider = xiaomiSpider()
    spider.run()

















