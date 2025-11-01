"""
    使用selenium+Chrome来抓取猫眼电影top100数据
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 设置无界面模式
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无界面模式
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 1.打开浏览器（无痕模式）
driver = webdriver.Chrome(options=chrome_options)

# 2.输入URL地址
driver.get('https://movie.douban.com/top250')


def get_one_page():
    # 3. li_list:匹配所有电影信息的li节点对象列表
    li_list = driver.find_elements(By.XPATH, '//*[@id="content"]/div/div[1]/ol/li')

    # 4.for循环一次遍历,提取每个电影的信息
    for li in li_list:
        # 正确的字段提取方式
        item = {}

        # 电影标题
        title_elem = li.find_element(By.CLASS_NAME, 'title')
        item['name'] = title_elem.text.strip()

        # 评分
        rating_elem = li.find_element(By.CLASS_NAME, 'rating_num')
        item['rating'] = rating_elem.text.strip()

        # 引用语
        try:
            quote_elem = li.find_element(By.CLASS_NAME, 'quote')
            item['quote'] = quote_elem.text.strip()
        except:
            item['quote'] = ''

        # 其他信息（导演、演员、年份等）
        info_elem = li.find_element(By.CLASS_NAME, 'bd')
        item['info'] = info_elem.text.strip()

        # 图片URL
        img_elem = li.find_element(By.TAG_NAME, 'img')
        item['image'] = img_elem.get_attribute('src')

        print(item)

    return len(li_list)  # 返回本页电影数量


# 正确的翻页逻辑
page_num = 1
while True:
    print(f"\n=== 第{page_num}页 ===")
    movie_count = get_one_page()

    if movie_count == 0:
        print("没有更多电影了")
        break

    # 尝试翻页
    try:
        next_btn = driver.find_element(By.XPATH, '//span[@class="next"]/a')
        next_btn.click()
        page_num += 1
        time.sleep(2)  # 等待页面加载
    except:
        print("已经是最后一页")
        break

# 关闭浏览器
driver.quit()












