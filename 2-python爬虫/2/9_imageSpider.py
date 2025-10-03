"""
    抓取图片到本地
    思路：
        一定要找到图片的真实完整的URL地址

"""


import requests
from fake_useragent import UserAgent

url = 'https://img1.baidu.com/it/u=1544750289,3500125996&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=677'
headers = {'User-Agent':UserAgent().random }

 # 一定使用content属性，因为图片是以二进制的方式存储的
r = requests.get(url, headers=headers).content

# 保存图片到本地
with open('boye.jpg', 'wb') as f:
    f.write(r)


