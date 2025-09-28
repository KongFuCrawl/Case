
from selenium import webdriver
import time
#创建一个driver对象
driver = webdriver.Chrome()

#打开一个网页
driver.get('https://www.baidu.com')
time.sleep(3)
#窗口最大化
driver.maximize_window()
time.sleep(3)
#刷新页面
driver.refresh()

print('地址：', driver.current_url)
print('标题：', driver.title)

#保存页面源码
with open('baidu.html', 'w',encoding='utf-8') as f:
    f.write(driver.page_source)

#当前页面截图
driver.save_screenshot('baidu.png')


# 关闭浏览器
time.sleep(3)
driver.quit()


