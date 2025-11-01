"""
    使用selenium模拟登陆豆瓣网
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 1,打开浏览器，输入地址到登陆页
driver = webdriver.Chrome()
driver.get("https://www.douban.com/")
driver.maximize_window()

time.sleep(2)

# 2. 先切换iframe
frame_node = driver.find_element(By.XPATH, '//*[@id="anony-reg-new"]/div/div[1]/iframe')
driver.switch_to.frame(frame_node)
time.sleep(2)

# 3. 登陆密码，用户名，密码，登陆按钮
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/ul[1]/li[2]').click()
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('1562236310')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('15348545')
time.sleep(2)
# 注意：查找节点时，如果属性值中包含空格，则必须使用 . 来代替，否则会无法找到该节点
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
time.sleep(5)




















