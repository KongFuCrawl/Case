"""
https://www.myfreemp3.com.cn/

"""


import requests

import os

class MP3Spider:

    url = 'https://www.myfreemp3.com.cn/'

headers = {
    "X-Requested-With" : "XMLHttpRequest",
 "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0"
}

def get_music_list(self, name, page):

        params = {
            "input": "namw",
            "filter": "name",
            "page": "page",
            "type": "netease",
        }
        #获取歌曲列表
        res = requests.post(self.url,data=params, headers=self.header)
        #获取包含歌曲信息的列表
        datas = res.json()['data']['list']
        #判断是否寻寻找周杰论这个文件夹，没有则创建
        if not os.path.isdir(name):
         os.mkdir(name)

        self.paser_data( name,datas)

        def paser_data(self , name,datas):
            """解析返回数据"""



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

        #在歌手文件夹下面创建一个和歌曲同名的文件夹
        file_path ='{}/{}'.format(name,title)
        if not os.path.isdir(file_path):
            os.mkdir(file_path)
        else:
            print("该歌曲已经下载了")
        #保存歌词为文件



if __name__ == '__main__':
    mp3 = MP3Spider()
    mp3.get_music_list('蔡依林', 1)

