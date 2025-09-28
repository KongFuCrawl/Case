import time
import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# 打开目标网站
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# 设置隐式等待时间
driver.implicitly_wait(10)

#切换到iframe中
driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="iframeResult"]'))
#创建一个鼠标操作对象
ac = ActionChains(driver)
#将鼠标移动到某个元素上（请拖拽我）
ac.move_to_element(driver.find_element(By.XPATH, '//*[@id="draggable"]'))
#按下鼠标左键
ac.click_and_hold()
ac.move_to_element(driver.find_element(By.XPATH, '//*[@id="droppable"]'))
#释放鼠标
ac.release()
#执行动作
ac.perform()

time.sleep(5)
driver.quit()



