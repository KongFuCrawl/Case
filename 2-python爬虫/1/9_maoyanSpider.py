"""
猫眼电影top100数据抓取
"""
# <div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>
# <div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>(.*?)<p class="releasetime">(.*?)</p>


"""
猫眼电影top100数据抓取
"""
import requests
import re
import time
import random


class MAoyanSpider:
    def __init__(self):
        self.url = 'https://www.maoyan.com/board/4?ffset={}'
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0'}

    def get_html(self, url):
        """获取响应内容"""
        html = requests.get(url, headers=self.headers).content.decode('utf-8')
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析提取函数"""
        regex = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        pattern = re.compile(regex, re.S)

        r_list = pattern.findall(html)
        #直接调用数据处理函数
        self.save_html(r_list)

    def save_html(self, r_list):
        """具体数据处理的函数"""
        item = {}
        for r in r_list:
            item['name'] = r[0].strip()
            item['star'] = r[1].strip()
            item['time'] = r[2].strip()
            print(item)


    def run(self):
        #程序入口函数
        for offset in range(0, 91, 10):
            page_url = self.url.format(offset)
            self.get_html(page_url)
            #控制数据抓取的频率 uniform生成指定范围的浮点数
            time.sleep(random.uniform(0, 1))

if __name__ == '__main__':
    spider = MAoyanSpider()
    spider.run()