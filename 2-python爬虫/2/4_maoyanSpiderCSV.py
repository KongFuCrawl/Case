

"""
猫眼电影top100数据抓取 - 存入 CSV文件
"""
import requests
import re
import time
import random
import csv
import os


class MAoyanSpider:
    def __init__(self):
        self.url = 'https://www.maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        }
        self.csv_file = 'maoyan_movies.csv'
        self.init_csv()

    def init_csv(self):
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', encoding='utf-8-sig', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['排名', '电影名称', '主演', '上映时间', '评分'])
            print("CSV文件已初始化")

    def get_html(self, url):
        try:
            print(f"正在请求: {url}")
            response = requests.get(url, headers=self.headers, timeout=15)
            print(f"响应状态码: {response.status_code}")

            if response.status_code == 200:
                response.encoding = 'utf-8'
                html = response.text

                # 保存HTML用于分析
                with open('maoyan_debug.html', 'w', encoding='utf-8') as f:
                    f.write(html)
                print("HTML已保存到 maoyan_debug.html")

                self.parse_html(html)
            else:
                print(f"请求失败")

        except Exception as e:
            print(f"请求失败: {e}")

    def parse_html(self, html):
        """解析HTML内容"""
        print("开始解析HTML...")

        # 尝试多种可能的选择器
        patterns = [
            # 可能的新模式
            r'<div class="movie-item".*?<p class="name"><a.*?>(.*?)</a>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>',
            r'<div class="board-item".*?<p class="name"><a.*?>(.*?)</a>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>',
            r'<p class="name">.*?>(.*?)</a>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>',
            # 简单匹配
            r'<p class="name">.*?>(.*?)</a>',
            r'<p class="star">(.*?)</p>',
            r'<p class="releasetime">(.*?)</p>'
        ]

        all_data = []
        for i, pattern in enumerate(patterns[:3]):  # 只尝试前3个完整模式
            try:
                matches = re.findall(pattern, html, re.S | re.I)
                if matches:
                    print(f"模式{i + 1}找到 {len(matches)} 条数据")
                    for match in matches:
                        if len(match) == 3:
                            all_data.append(match)
                            print(f"  找到: {match[0]}")
                    break
            except Exception as e:
                continue

        if all_data:
            self.save_to_csv(all_data)
        else:
            print("未找到数据，尝试提取部分信息...")
            self.extract_partial_data(html)

    def extract_partial_data(self, html):
        """提取部分数据"""
        titles = re.findall(r'<p class="name">.*?>(.*?)</a>', html, re.S)
        stars = re.findall(r'<p class="star">(.*?)</p>', html, re.S)
        times = re.findall(r'<p class="releasetime">(.*?)</p>', html, re.S)

        print(f"找到 {len(titles)} 个标题, {len(stars)} 个主演信息, {len(times)} 个时间信息")

        # 取最小长度，确保数据对应
        min_len = min(len(titles), len(stars), len(times))
        if min_len > 0:
            combined_data = []
            for i in range(min_len):
                combined_data.append((titles[i].strip(), stars[i].strip(), times[i].strip()))

            self.save_to_csv(combined_data)
        else:
            print("数据不完整，无法匹配")

    def save_to_csv(self, r_list):
        if not r_list:
            return

        try:
            with open(self.csv_file, 'a', encoding='utf-8-sig', newline='') as f:
                writer = csv.writer(f)

                for i, r in enumerate(r_list):
                    if len(r) >= 3:
                        title = r[0].strip()
                        star = r[1].strip().replace('主演：', '').replace('&nbsp;', ' ').strip()
                        releasetime = r[2].strip().replace('上映时间：', '').strip()

                        writer.writerow([i + 1, title, star, releasetime, ''])
                        print(f"保存: {title}")

                print(f"成功保存 {len(r_list)} 条数据")

        except Exception as e:
            print(f"保存失败: {e}")

    def run(self):
        try:
            for offset in range(0, 91, 10):
                page_url = self.url.format(offset)
                print(f"\n=== 正在抓取第 {offset // 10 + 1} 页 ===")
                self.get_html(page_url)
                time.sleep(random.uniform(2, 4))
        except Exception as e:
            print(f"错误: {e}")
        finally:
            print(f"数据已保存到: {os.path.abspath(self.csv_file)}")


if __name__ == '__main__':
    spider = MAoyanSpider()
    spider.run()
