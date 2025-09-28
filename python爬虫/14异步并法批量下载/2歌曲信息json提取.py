"""
https://www.myfreemp3.com.cn/

"""


import requests
from jsonpath import jsonpath

url = 'https://www.myfreemp3.com.cn/'
params = {
 "input" : "闪耀",
 "filter" : "name",
 "page"	: "2025-8-30",
 "type" : "netease",
}
headers = {
    "X-Requested-With" : "XMLHttpRequest",
 "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0"
}
#获取歌曲列表
res = requests.post(url,data=params,headers=headers)
#获取包含歌曲信息的列表
datas = res.json()['data']['list']
#判断是否寻寻找周杰论这个文件夹，没有则创建
if not os.path.isdir('周杰论'):
 os.mkdir('周杰论')

for itme in datas:
  #歌曲名
  title = itme.get('title')
  #歌手信息
  author = itme.get('author')
  #歌词
  lrc = itme.get('lrc')
  #图片
  img_url = itme.get('pic')
  #歌曲的下载地址
mp3_url =itme.get('url')

print (title,author,lrc,img_url,mp3_url)