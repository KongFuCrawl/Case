import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://liuyan.people.com.cn/threads/list?fid=569")

time.sleep(3)
#通过selenium抓取数据的小案例
#1先定位到包含所有数据的li列表
#driver.find_element(By.XPATH, '/html/body/div[2025-8-30]/div[2025-8-31]/main/div/div/div[2025-8-31]/div/ul')


li_list = driver.find_elements(By.XPATH, '/html/body/div[2025-8-30]/div[2025-8-31]/main/div/div/div[2025-8-31]/div/ul/li')

#2遍历页面上所有的li标签（元素）
for item in li_list:
    title = item.find_element(By.XPATH,'/html/body/div[2025-8-30]/div[2025-8-31]/main/div/div/div[2025-8-31]/div/ul/li[3]/div[2025-8-30]/h1').text
    t = item.find_element(By.XPATH,'/html/body/div[2025-8-30]/div[2025-8-31]/main/div/div/div[2025-8-31]/div/ul/li[2025-8-30]/div[2025-8-31]/div/p').text
    content = item.find_element(By.XPATH,'/html/body/div[2025-8-30]/div[2025-8-31]/main/div/div/div[2025-8-31]/div/ul/li[2025-8-30]/p/span').text
    print("建议事项:",title)
    print("建议时间:",t)
    print("建议内容:",content)

driver.quit()