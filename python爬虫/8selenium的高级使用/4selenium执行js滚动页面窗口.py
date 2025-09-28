"""
js滚动窗口


"""

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# 打开目标网站
driver.get(
    'https://liuyan.people.com.cn/threads/list?checkStatus=0&fid=573&formName=%E6%B9%96%E5%8D%97%E7%9C%81%E5%A7%94%E4%B9%A6%E8%AE%B0%E6%B2%88%E6%99%93%E6%98%8E&position=0&province=29&city=&saveLocation=29&pForumNames=%E6%B9%96%E5%8D%97%E7%9C%81')
# 设置隐式等待时间
driver.implicitly_wait(10)

for i in range(5):
    time.sleep(1)
    js = 'window.scrollBy(0,{})'.format(random.randint(100, 300))
    #通过driver执行js代码
    driver.execute_script(js)

time.sleep(5)
driver.quit()
