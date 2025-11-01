# 倒入selenium的webdriver接口
from selenium import webdriver

# 1.打开Chrome浏览器
webdriver = webdriver.Chrome()
# 2.在浏览器地址栏输入百度的URL地址，并确认
time = url = 'https://www.baidu.com/'
