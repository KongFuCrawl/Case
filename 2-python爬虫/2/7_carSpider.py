"""
    汽车之家
        1.一级页面提取数据：汽车详情页连接
        2.二级页面提取数据：具体汽车数据

"""

import random
import re

import requests
import time


class CarSpider:
    def __init__(self):
        self.url = 'https://www.che168.com/beijing/a/a0_0msdgscncgpi1ltocsp{''}4exx0/?pvareaid=102179#currengpostion'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0'}

    def get_html(self, url):
        """功能函数1 - 获取html"""
        html = requests.get(url=url, headers=self.headers).content.decode('gb2312')

        return html

    @staticmethod
    def re_func(regex, html):
        """功能函数2 - 正则解析函数"""
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)

        return r_list

    def parse_html(self, one_url):
        """程序逻辑函数"""
        one_html = self.get_html(one_url)
        one_regex = '<li class="cards-li list-photo-li".*?<a href="(.*?)"'
        # href_list: ['/declear/xxx',','',...]
        href_list = self.re_func(one_regex, one_html)
        for href in href_list:
            two_url = 'https://www.che168.com' + href
            # 提取一辆汽车的具体信息
            self.get_car_info(two_url)
            # 控制抓取频率，每抓取一辆汽车随机休眠0-1秒钟
            time.sleep(random.uniform(1, 3))

    def get_car_info(self, two_url):
        """提取一辆汽车的具体信息"""
        two_html = self.get_html(two_url)
        two_regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<h4>.*?</h4>.*?<p>(.*?)</p>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">¥(.*?)<b>'
        # r_list:[('悦动'，'7.01万公里','2019年08月','自动 / 1.6L','北京'),'3.28万']
        self.re_func(regex=two_regex, html=two_html)

    def run(self):
        for o in range(1, 3):
         page_url = self.url.format(o)
         self.parse_html(one_url=page_url)


if __name__ == "__main__":
    spider = CarSpider()
    spider.run()
