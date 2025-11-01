from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1.打开浏览器并进入登陆页
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')
driver.maximize_window()
time.sleep(3)

# 2. 切换到iframe子页面：因为selenium默认支持id 或者 name 两个属性的切换
driver.switch_to.frame( 'ptlogin_iframe')


# 3. 账号 + 密码 + 登陆按钮
driver.find_element(By.ID, 'u').send_keys('385063760')
driver.find_element(By.ID, 'p').send_keys('zbc199994')
driver.find_element(By.ID, 'login_button').click()
time.sleep(3)

