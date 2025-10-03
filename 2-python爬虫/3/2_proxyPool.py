"""
    抓取快代理免费代理高匿名代理，并测试。建立自己的代理IP池

"""

import requests
from lxml import etree
from fake_useragent import UserAgent
import time
import threading
from queue import Queue


class ProxyPool:
    def __init__(self):
        self.url = 'https://www.kuaidaili.com/free/inha/{}/'  # 添加了页码占位符和路径
        self.test_url = 'http://httpbin.org/get'
        self.available_proxies = []
        self.lock = threading.Lock()

    def get_proxy(self, url):
        headers = {'User-Agent': UserAgent().random}
        try:
            html = requests.get(url, headers=headers, timeout=10).text
            # 解析提取代理ip
            p = etree.HTML(html)
            # tr_list: [<element tr at xxx>,....]
            tr_list = p.xpath('//tr')
            ip_port_list = []

            for tr in tr_list[1:]:  # 从1开始跳过表头
                ip_list = tr.xpath('./td[1]/text()')
                ip = ip_list[0].strip() if ip_list else None
                port_list = tr.xpath('./td[2]/text()')
                port = port_list[0].strip() if port_list else None

                if ip and port:
                    ip_port_list.append((ip, port))

            return ip_port_list
        except Exception as e:
            print(f"获取代理失败: {e}")
            return []

    def test_proxy(self, ip, port):
        # 测试一个代理ip是否可用
        proxies = {
            'http': f'http://{ip}:{port}',
            'https': f'https://{ip}:{port}',
        }

        try:
            resp = requests.get(url=self.test_url, proxies=proxies, timeout=5)
            if resp.status_code == 200:
                print(f"\033[92m{ip}:{port} 可用\033[0m")
                with self.lock:
                    self.available_proxies.append(f"{ip}:{port}")
            else:
                print(f"\033[91m{ip}:{port} 不可用 - 状态码: {resp.status_code}\033[0m")
        except Exception as e:
            print(f"\033[91m{ip}:{port} 不可用 - 错误: {e}\033[0m")

    def worker(self, proxy_queue):
        """工作线程函数"""
        while True:
            item = proxy_queue.get()
            if item is None:  # 终止信号
                break
            ip, port = item
            self.test_proxy(ip, port)
            proxy_queue.task_done()

    def run(self):
        # 创建队列和线程
        proxy_queue = Queue()
        threads = []

        # 启动工作线程
        for _ in range(10):  # 10个线程并发测试
            t = threading.Thread(target=self.worker, args=(proxy_queue,))
            t.start()
            threads.append(t)

        # 获取代理IP并加入队列
        for pg in range(1, 200):  # 只获取前10页，避免请求过多
            page_url = self.url.format(pg)
            print(f"正在获取第{pg}页代理...")

            ip_port_list = self.get_proxy(page_url)
            for ip, port in ip_port_list:
                proxy_queue.put((ip, port))

            # 添加延迟，避免请求过快被封IP
            time.sleep(1)

        # 等待所有任务完成
        proxy_queue.join()

        # 停止工作线程
        for _ in range(10):
            proxy_queue.put(None)
        for t in threads:
            t.join()

        # 输出结果
        print(f"\n检测完成！找到 {len(self.available_proxies)} 个可用代理")
        if self.available_proxies:
            print("可用代理列表:")
            for proxy in self.available_proxies:
                print(proxy)


if __name__ == "__main__":
    proxy_pool = ProxyPool()
    proxy_pool.run()
