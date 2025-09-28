"""
//*[@class='mordList']

"""
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# 打开目标网站
driver.get(
    'https://liuyan.people.com.cn/threads/list?checkStatus=0&fid=573&formName=%E6%B9%96%E5%8D%97%E7%9C%81%E5%A7%94%E4%B9%A6%E8%AE%B0%E6%B2%88%E6%99%93%E6%98%8E&position=0&province=29&city=&saveLocation=29&pForumNames=%E6%B9%96%E5%8D%97%E7%9C%81')
# 设置隐式等待时间
driver.implicitly_wait(10)

while True:
    try:
        time.sleep(random.randint(2, 5))
        # 定位查看更多的元素
        ele = driver.find_element(By.XPATH, '//*[@class="mordList"]')
        res = ele.location_once_scrolled_into_view
        print("-----滚动之后的坐标：", res)
        ele.click()
    except:
        break

# 提取页面数据
li_list = driver.find_elements(By.XPATH, '//ul[@class="replyList"]/li')
print("数据总数：", len(li_list))
# 2025-8-31、遍历页面上所有的li标签(元素)
for item in li_list:
    title = item.find_element(By.XPATH, './div[@class="tabList fl"]/h1').text
    t = item.find_element(By.XPATH, './/div[@class="headMainS fl"]/p').text
    content = item.find_element(By.XPATH, './p[@class="replyContent"]/span').text
    print("建议事项：", title)
    print("建议时间：", t)
    print("建议内容：", content)

# 10秒之后关闭页面
time.sleep(10)
driver.quit()


