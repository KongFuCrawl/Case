"""
    使用selenium抓取京东商城 爬虫书 商品的数据
    所抓数据：
        1.产品名称
        2.产品价格
        3.评价数量
        4.产品商家
    知识点：
        1.浏览器对象driver执行JS脚本，execute_script('')
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JdSpider:
    def __init__(self):
        self.url = 'https://search.jd.com/'
        self.driver = webdriver.Chrome()
        self.driver.get(url=self.url)

        time.sleep(3)
    def get_html(self):
        """找到搜索框，发送搜索关键字，点击搜索，进入到商品页"""
        self.driver.find_element(By.XPATH, '//*[@id="keyword"]').send_keys('爬虫书')
        self.driver.find_element(By.XPATH, '/html/body/div[2]/form/input[4]').click()
        time.sleep(3)
    def parse_html(self):
        """解析提取1页的完整数据"""
        # 执行Js脚本，让所有商品数据完全加载出来之后在杂抓取
        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)'
        )
        # 给页面加载预留时间
        time.sleep(3)
        div_list = self.driver.find_elements(By.XPATH, '//*[@id="searchCenter"]/div/div/div[2]/div')
        for div in div_list:
            print(div.text)
            print('*' * 50)

    def run(self):
        self.get_html()
        self.parse_html()


if __name__ == '__main__':
    spider = JdSpider()
    spider.run()












