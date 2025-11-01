"""
    selenium操作鼠标
"""


#  导入元素定位器（支持ID、XPATH、CSS_SELECTOR等）
from selenium.webdriver.common.by import By
# 导入Selenium核心模块，用于浏览器自动化控制
from selenium import webdriver
# 导入鼠标事件类
from selenium.webdriver import ActionChains
# 时间模块
import time


# 1.打开浏览器，输入百度地址
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://www.baidu.com/')

# 2.找到右上角设置节点，把鼠标移动过去
set_nodes = driver.find_elements(By.XPATH, '//*[@id="s-usersetting-top"]')
time.sleep(3)

# 3.移动鼠标
ActionChains(driver).move_to_element(set_nodes[0]).perform()
time.sleep(3)
#  谨记三不走
# 1. 实例化
# 2.指定行为
# 3.执行行为



