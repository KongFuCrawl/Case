from selenium import webdriver
from selenium.webdriver.common.by import By
import time
"""# 1.打开Chrime浏览器"""
driver = webdriver.Chrome()
# 2.输入百度的URL地址，进入百度首页
driver.get('https://www.baidu.com/')
# 等待三秒
time.sleep(3)
# 3. 找到搜索框节点，并发送文本 - 胡歌
driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('胡歌')
# 等待三秒
time.sleep(3)
# 4. 找到百度一下按钮，并进行模拟点击
driver.find_element(By.XPATH,'//*[@id="su"]').click()
# 等待三秒
time.sleep(3)



