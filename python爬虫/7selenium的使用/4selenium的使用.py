from selenium import webdriver
import time

from selenium.webdriver.common.by import By

#创建一个driver对象
driver = webdriver.Chrome()

#打开一个网页
driver.get("http://www.baidu.com")

#ele = driver.find_element(By.XPATH, '//*[@id="chat-textarea"]')
ele = driver.find_element(By.ID, "chat-textarea")


ele.send_keys("人大代表")
time.sleep(1)
#清空输入框
ele.clear()

time.sleep(5)
driver.quit()
