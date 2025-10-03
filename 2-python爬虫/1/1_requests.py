#引入requests模块
import requests
from bs4 import BeautifulSoup

#get()获取到的为响应对象
resp = requests.get(url='https://www.jd.com/')

#text:获取响应的内容 - 字符串
html1 = resp.text
print(html1)

#content: 获取响应的内容 - 字符串
html = resp.content
print(html)

# status_code:获取http响应码
code = resp.status_code
print(code)

#url:获取返回实际数据的URL地址
url = resp.url
print(url)

