"""
猫眼电影top100数据抓取
"""

# <div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>
# <div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>(.*?)<p class="releasetime">(.*?)</p>


"""
猫眼电影top100数据抓取 - 存入mysql
"""
import random
import re
import time

import pymysql
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

        # 数据库连接
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            database='mydb',
            charset='utf8mb4',
            port=3306
        )
        self.cursor = self.db.cursor()

        # 创建适合爬虫数据的表
        self.create_table()

    def create_table(self):
        """创建匹配爬虫数据的数据表"""
        create_sql = """CREATE TABLE IF NOT EXISTS maoyan_movies ( 
            id INT AUTO_INCREMENT PRIMARY KEY, 
            title VARCHAR ( 100 ),
            star VARCHAR ( 100 ),
            releasetime VARCHAR ( 100 )
            )"""
       
        try:
            self.cursor.execute(create_sql)
            self.db.commit()
            print("爬虫数据表已就绪")
        except Exception as e:
            print(f"创建表失败: {e}")

    def get_html(self, url):
        """获取响应内容"""
        try:
            print(f"正在请求: {url}")
            response = requests.get(url, headers=self.headers, timeout=10)
            print(f"响应状态码: {response.status_code}")

            if response.status_code == 200:
                response.encoding = 'utf-8'
                html = response.text
                # 保存HTML内容到文件用于调试
                with open(f'maoyan_page_{url.split("=")[-1]}.html', 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"页面内容已保存，长度: {len(html)} 字符")
                self.parse_html(html)
            else:
                print(f"请求失败，状态码: {response.status_code}")

        except Exception as e:
            print(f"请求失败: {e}")

    def parse_html(self, html):
        """解析提取函数"""
        print("开始解析HTML...")

        # 尝试不同的正则表达式模式
        patterns = [
            '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>',
            '<div class="movie-item-info".*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>',
            'title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        ]

        for i, pattern in enumerate(patterns):
            try:
                regex = re.compile(pattern, re.S)
                r_list = regex.findall(html)
                if r_list:
                    print(f"模式{i + 1}找到 {len(r_list)} 条数据")
                    self.save_html(r_list)
                    return
            except Exception as e:
                print(f"模式{i + 1}解析失败: {e}")

        print("所有解析模式都失败，请检查网页结构")
        # 打印部分HTML内容用于调试
        print("HTML片段:", html[:500])

    def save_html(self, r_list):
        """具体数据处理的函数"""
        if not r_list:
            print("没有数据需要保存")
            return

        print(f"准备保存 {len(r_list)} 条数据")
        ins = 'INSERT INTO maoyan_movies (title, star, releasetime) VALUES (%s, %s, %s)'

        success_count = 0
        for r in r_list:
            li = [
                r[0].strip(),
                r[1].strip(),
                r[2].strip(),
            ]
            print(f"处理数据: {li}")
            try:
                self.cursor.execute(ins, li)
                self.db.commit()
                success_count += 1
                print(f"插入成功: {li}")
            except Exception as e:
                print(f"插入数据失败: {e}")
                self.db.rollback()

        print(f"数据保存完成，成功: {success_count}/{len(r_list)}")

    def run(self):
        """程序入口函数"""
        try:
            for offset in range(0, 91, 10):
                page_url = self.url.format(offset)
                print(f"\n=== 正在抓取第 {offset // 10 + 1} 页 ===")
                self.get_html(page_url)
                time.sleep(random.uniform(2, 5))  # 增加等待时间
        except Exception as e:
            print(f"爬取过程中出错: {e}")
        finally:
            self.close_db()

    def close_db(self):
        """安全关闭数据库连接"""
        try:
            if self.cursor:
                self.cursor.close()
            if self.db:
                self.db.close()
                print("数据库连接已关闭")
        except Exception as e:
            print(f"关闭数据库时出错: {e}")


# 运行爬虫
if __name__ == '__main__':
    spider = MAoyanSpider()
    spider.run()
