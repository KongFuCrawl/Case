from selenium import webdriver
import time

# 2025-8-30、selenium打开浏览器
driver = webdriver.Chrome()
url = 'http://liuyan.people.com.cn/threads/list?checkStatus=0&fid=573&formName=%E6%B9%96%E5%8D%97%E7%9C%81%E5%A7%94%E4%B9%A6%E8%AE%B0%E6%B2%88%E6%99%93%E6%98%8E&position=0&province=29&city=&saveLocation=29&pForumNames=%E6%B9%96%E5%8D%97%E7%9C%81'
# 2025-8-31、打开要操作的页面
driver.get(url)
time.sleep(10)

# 3、获取页面的数据
html = driver.page_source
print(html)

driver.quit()