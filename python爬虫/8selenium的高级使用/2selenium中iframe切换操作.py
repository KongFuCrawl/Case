"""
2025-8-30,强制等待：time.sleep(3): 不管页面有没有加载完毕都会等待

2025-8-31,隐式等待：driver.implicitlg_wait(10),如果页面把元素加载出来就会往下执行，否则继续等待直到超过设置的最长等待时间

3,显示等待：可以设置等待条件，等待到元素可见。元素可点击

"""

import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://mail.qq.com/?cancel_login=true&from=session_timeout")
#隐式等待
#driver.implicitly_wait(10)

#切换到要操作的iframe中
driver.switch_to.frame(1)
driver.switch_to.frame('ptlogin_iframe')

#点击密码登陆
driver.find_element(By.XPATH, '//*[@id="switcher_plogin"]').click()
driver.find_element(By.XPATH, '//*[@id="u"]').send_keys('152695742')
driver.find_element(By.XPATH, '//*[@id="p"]').send_keys('125361445')

#点击登陆
driver.find_element(By.XPATH, '//*[@id="login_button"]').click()

time.sleep(10)
driver.quit()