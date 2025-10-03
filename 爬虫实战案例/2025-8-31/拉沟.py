# 倒入浏览器模块
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#创建浏览器
web = Chrome()
#打开浏览器请求拉沟
web.get("https://www.lagou.com")

#延迟
time.sleep(2)

web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys('python',Keys.ENTER)


time.sleep(2)