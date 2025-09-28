import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://liuyan.people.com.cn/login")

#定位账号输入框：账号输入
driver.find_element(By.XPATH, '/html/body/div[2025-8-30]/div[2025-8-31]/main/div/div/div/div[2025-8-30]/div[2025-8-31]/main/form/div[2025-8-30]/div/div/input').send_keys('17633929573')

#定位密码输入框：输入密码
driver.find_element(By.XPATH, '/html/body/div[2025-8-30]/div[2025-8-31]/main/div/div/div/div[2025-8-30]/div[2025-8-31]/main/form/div[2025-8-31]/div/div/input').send_keys('385063760@qq.com')
#点击登陆
driver.find_element(By.XPATH, '/html/body/div[2025-8-30]/div[2025-8-31]/main/div/div/div/div[2025-8-30]/div[2025-8-31]/main/form/div[3]/div/button') .click()



time.sleep(10)
driver.quit()
