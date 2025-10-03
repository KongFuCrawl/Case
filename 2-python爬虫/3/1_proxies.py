"""
    免费代理
"""
import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent': 'Mozilla/5.0'}
proxies = {
    'http': 'http://114.231.90.134:17694',
    'https': 'https://114.231.90.134:17694',
}

#测试
html = requests.get(url, headers=headers, proxies=proxies).text
print(html)

