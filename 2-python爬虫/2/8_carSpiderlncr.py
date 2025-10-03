"""
    汽车之家二页数据抓取案例 - 利用redis实现增量爬虫
        1.一级页面提取数据：汽车详情页连接
        2.二级页面提取数据：具体汽车数据
        3.建立User-Agent池来应对反爬虫
            fake_useragent模块



增量爬虫思路：
    1,利用redis集合存储所有请求的指纹
    2,利用sadd（）的返回值来判断之前是否抓取过次请求

"""

import random
import re
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import redis
from hashlib import md5
import sys



class CarSpider:
    def __init__(self):
        self.url = 'https://www.che168.com/beijing/a0_0msdgscncgpi1ltocsp{}exx0/'
        # 连接redis
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def get_html(self, url):
        """获取网页内容"""
        headers = {'User-Agent': UserAgent().random}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.encoding = response.apparent_encoding
            print(f"📊 检测到的编码: {response.encoding}")
            return response.text
        except Exception as e:
            print(f"❌ 获取页面失败: {e}")
            return ""

    def parse_html(self, one_url):
        """解析列表页"""
        print(f"🌐 正在访问: {one_url}")
        html = self.get_html(one_url)

        if not html:
            print("❌ 页面内容为空")
            return

        # 保存HTML内容用于调试
        try:
            with open('debug_page.html', 'w', encoding='utf-8') as f:
                f.write(html)
            print("💾 页面已保存为 debug_page.html")
        except Exception as e:
            print(f"❌ 保存页面失败: {e}")

        # 显示页面标题
        title_match = re.search(r'<title>(.*?)</title>', html, re.S)
        if title_match:
            print(f"📄 页面标题: {title_match.group(1)}")

        # 使用BeautifulSoup解析
        try:
            soup = BeautifulSoup(html, 'html.parser')

            # 方法1: 查找cards-li类的元素
            car_items = soup.find_all('li', class_='cards-li')
            print(f"🍜 通过class找到 {len(car_items)} 个车辆项")

            car_links = []
            for item in car_items:
                link = item.find('a')
                if link and link.get('href'):
                    href = link['href']
                    car_links.append(href)
                    print(f"  找到链接: {href}")

            # 方法2: 如果没找到，尝试查找包含/dealer/的链接
            if not car_links:
                print("🔍 尝试查找/dealer/链接...")
                all_links = soup.find_all('a', href=True)
                for link in all_links:
                    href = link.get('href', '')
                    if '/dealer/' in href and href.endswith('.html'):
                        car_links.append(href)
                        print(f"  找到经销商链接: {href}")

            # 方法3: 查找其他可能的车辆链接
            if not car_links:
                print("🔍 尝试查找其他链接模式...")
                # 使用正则表达式查找可能的车辆链接
                link_patterns = [
                    r'href="(/dealer/.*?\.html)"',
                    r'href="(.*?\.html\?pvareaid=.*?)"',
                    r'class="carinfo".*?href="(.*?)"'
                ]

                for pattern in link_patterns:
                    matches = re.findall(pattern, html, re.S | re.I)
                    if matches:
                        car_links.extend(matches)
                        print(f"  正则找到 {len(matches)} 个链接")
                        break

            if not car_links:
                print("❌ 未找到任何车辆链接")
                # 显示页面开头内容用于调试
                print("HTML开头500字符:", html[:500])
                return

            print(f"✅ 总共找到 {len(car_links)} 个车辆链接")

            # 处理前3个链接进行测试
            for j, href in enumerate(car_links[:3]):
                if href.startswith('http'):
                    two_url = href
                else:
                    two_url = 'https://www.che168.com' + href
            finger = self.md5_url(url=two_url)
            #如果返回值为1：添加成功，说明之前没有抓取过次地址
            if self.r.sadd('car:spiders', finger) == 1:

                print(f"🚗 处理第 {j + 1} 个: {two_url}")
                self.get_car_info(two_url)
                time.sleep(random.uniform(1, 2))

            else:
                # 一旦发现第一个已经抓取过。说明后面的也一定抓取过了，此时会彻底退出
                sys.exit('更新完成，程序退出')


        except Exception as e:
            print(f"❌ 解析HTML失败: {e}")

    def md5_url(self, url):
        """功能函数3 - 生成指纹的函数"""
        s = md5()
        s.update(url.encode())
        return s.hexdigest()



    def get_car_info(self, two_url):
        """提取车辆详情信息"""
        print(f"📖 解析详情页: {two_url}")
        html = self.get_html(two_url)

        if not html:
            return

        try:
            # 简单提取信息
            title_match = re.search(r'<title>(.*?)</title>', html, re.S)
            price_match = re.search(r'class="price".*?([\d\.]+万)', html, re.S)

            title = title_match.group(1).strip() if title_match else '未知标题'
            price = price_match.group(1) if price_match else '价格未知'

            car_info = {
                '车型': title.split('|')[0] if '|' in title else title,
                '价格': price,
                '链接': two_url,
                '爬取时间': time.strftime('%Y-%m-%d %H:%M:%S')
            }

            self.car_list.append(car_info)
            print(f"✅ 提取: {car_info['车型']} - {car_info['价格']}")

        except Exception as e:
            print(f"❌ 解析详情页失败: {e}")

    def save_to_excel(self):
        """保存数据到Excel - 修正了encoding参数"""
        if self.car_list:
            df = pd.DataFrame(self.car_list)
            # 修正：去掉 encoding 参数
            df.to_excel('二手车数据.xlsx', index=False)
            print(f"💾 成功保存 {len(self.car_list)} 条数据")
        else:
            print("❌ 无数据可保存")

    def run(self):
        """运行爬虫"""
        print("🚗 开始爬取二手车之家数据...")

        # 测试第一页
        page_url = self.url.format(1)
        self.parse_html(page_url)

        self.save_to_excel()
        print("🎉 爬取完成！")


if __name__ == "__main__":
    spider = CarSpider()
    spider.run()