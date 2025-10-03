"""
    猫眼电影top100数据抓取 - 存入 CSV文件
    思路：
        1. 在 __init__中创建相关连对象
        2. 在 save_html() 中把抓取的数据处理为字典，然后存入mongodb数据库
"""

import random
import re
import time
import pymongo
import requests


class MAoyanSpider:
    def __init__(self):
        self.url = 'https://www.maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

        # 创建 MongoDB 连接 - 修正后的代码
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['filmdb']
        self.collection = self.db['filmset']

        # 删除这行，MongoDB 没有 cursor() 方法
        # self.cursor = self.db.cursor()

    def create_table(self):
        """MongoDB 不需要创建表，但可以创建索引"""
        try:
            # 创建索引（MongoDB 的等价操作）
            self.collection.create_index([("title", pymongo.TEXT)])
            self.collection.create_index([("star", 1)])
            self.collection.create_index([("time", 1)])
            print("✅ MongoDB 集合和索引已就绪")
        except Exception as e:
            print(f"❌ 创建索引失败: {e}")

    def get_html(self, url):
        """获取响应内容"""
        try:
            print(f"🌐 正在请求: {url}")
            response = requests.get(url, headers=self.headers, timeout=10)
            print(f"📊 响应状态码: {response.status_code}")

            if response.status_code == 200:
                response.encoding = 'utf-8'
                html = response.text
                # 保存HTML内容到文件用于调试
                with open(f'maoyan_page_{url.split("=")[-1]}.html', 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"💾 页面内容已保存，长度: {len(html)} 字符")
                self.parse_html(html)
            else:
                print(f"❌ 请求失败，状态码: {response.status_code}")

        except Exception as e:
            print(f"❌ 请求失败: {e}")

    def parse_html(self, html):
        """解析提取函数"""
        print("🔍 开始解析HTML...")

        # 正则表达式模式
        pattern = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'

        try:
            regex = re.compile(pattern, re.S)
            r_list = regex.findall(html)

            if r_list:
                print(f"✅ 找到 {len(r_list)} 条电影数据")
                self.save_html(r_list)
            else:
                print("❌ 没有找到电影数据，请检查正则表达式")
                # 打印部分HTML内容用于调试
                print("📋 HTML片段:", html[:1000])

        except Exception as e:
            print(f"❌ 解析失败: {e}")

    def save_html(self, r_list):
        """保存数据到 MongoDB"""
        try:
            for r in r_list:
                item = {
                    'title': r[0].strip(),
                    'star': r[1].strip(),
                    'releasetime': r[2].strip(),
                    'crawl_time': time.strftime('%Y-%m-%d %H:%M:%S')
                }

                # 插入数据到 MongoDB
                result = self.collection.insert_one(item)
                print(f"✅ 保存成功: {item['title']} (ID: {result.inserted_id})")

        except Exception as e:
            print(f"❌ 保存失败: {e}")

    def run(self):
        """运行爬虫"""
        print("🚀 开始爬取猫眼电影数据...")
        self.create_table()

        # 爬取多页数据
        for offset in range(0, 100, 10):  # 0, 10, 20, ..., 90
            url = self.url.format(offset)
            self.get_html(url)
            time.sleep(random.uniform(1, 3))  # 随机延迟，避免被封

        print("🎉 爬取完成！")

        # 显示爬取的数据统计
        count = self.collection.count_documents({})
        print(f"📊 总共爬取 {count} 条电影数据")


# 运行爬虫
if __name__ == '__main__':
    spider = MAoyanSpider()
    spider.run()


