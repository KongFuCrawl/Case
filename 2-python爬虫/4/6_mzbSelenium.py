"""
    selenium切换句柄
"""
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class MzbSelenium:
    def __init__(self):
        self.url = 'https://www.mca.gov.cn/n156/n186/c1662004999980004260/content.html'
        self.driver = webdriver.Chrome()
        self.driver.get(url=self.url)
        time.sleep(3)  # 等待页面加载

    def get_html(self):
        try:
            # 点击链接
            self.driver.find_element(By.XPATH, '//*[@id="zoom"]/p[1]/a').click()
            time.sleep(5)  # 增加等待时间

            # 检查窗口句柄数量
            all_handles = self.driver.window_handles
            print(f"当前窗口句柄数量: {len(all_handles)}")

            if len(all_handles) > 1:
                # 切换到新窗口
                self.driver.switch_to.window(all_handles[1])
                print("成功切换到新窗口")
                # 解析提取数据
                self.parse_html()
            else:
                print("没有打开新窗口，在当前页面解析")
                self.parse_html()

        except Exception as e:
            print(f"错误: {e}")

    def parse_html(self):
        """解析提取函数"""
        try:
            tr_list = self.driver.find_elements(By.XPATH, '//tr[@height="19"]')
            print(f"找到 {len(tr_list)} 行数据")
            for tr in tr_list:
                print(tr.text)
        except Exception as e:
            print(f"解析错误: {e}")

    def run(self):
        self.get_html()

    def __del__(self):
        """析构函数，确保浏览器关闭"""
        if hasattr(self, 'driver'):
            self.driver.quit()


if __name__ == '__main__':
    spider = MzbSelenium()
    spider.run()

    
