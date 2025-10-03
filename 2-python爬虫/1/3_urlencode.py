import requests
from urllib import parse

#1：拼接URl地址
keyword = input('请输入关键字：')
params = parse.urlencode({'q': keyword})
url = 'http://www.baidu.com/s?{}'.format(params)
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}
#2: 发送请求获取响应
html = requests.get(url=url, headers=headers).text


#3：保存文件到本地
filename = '{}.html'.format(keyword)

with open(filename, 'w',encoding='utf_8') as f:
    f.write(html)