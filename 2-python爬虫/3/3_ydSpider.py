"""
    抓取有到翻译的翻译结果
    1, F12抓包，页面中翻译单词
    2, 分析Form表单数据变化
    3, 寻找加密的Js文件，并分析加密算法
    4, 用python实现对应的加密算法
    5, 处理headers，data为字典，发送请求进行数据抓取
"""
import requests
import time
import random
from hashlib import md5

class YdSpider:
    def __init__(self):
        # Post_url: 一定要是F12抓到的地址
        self.post_url = 'https://dict.youdao.com/webtranslate'
        self.headers = {
            "Host": "dict.youdao.com",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "330",
            "Origin": "https://fanyi.youdao.com",
            "Connection": "keep-alive",
            "Referer": "https://fanyi.youdao.com/",
            "Cookie": "OUTFOX_SEARCH_USER_ID=1204419532@123.13.67.120; OUTFOX_SEARCH_USER_ID_NCOO=1812469373.2692113; YOUDAO_MOBILE_ACCESS_TYPE=1; __adroll_fpc=b3a3bb7e55a2ce65fb7b7686e3725eba-1760252400700; _uetsid=0db1c7c0a73811f0be61f3a3f0f14684; _uetvid=0db1b140a73811f0941a8fcdfcea7a9f; DICT_DOCTRANS_SESSION_ID=NDYwYTg2MWYtODE2ZS00ZGIyLTgxNzItYTkwMTM2ZmMxOWU5",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
        }

    def get_ts_salt_sing(self, word):
        # ts salt
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))
        # sign
        string = "fanyideskweb" + word + salt + "mmbP%A-r6U3Nw(n]BjuEu"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()

        return ts, salt, sign

    def attack_yd(self, word):
        # 获取 ts salt sign
        ts, salt, sign = self.get_ts_salt_sing(word)
        date = {
            "i": word,
            "from": "en",
            "to": "en",
            "useTerm": "'false'",
            "domain": "'0'",
            "dictResult": "'true'",
            "keyid": "webfanyi",
            "sign": sign,
            "client": "fanyideskweb",
            "product": "webfanyi",
            "appVersion": "1.0.0",
            "vendor": "web",
            "pointParam": "client,mysticTime,product",
            "mysticTime": "'1760344108935'",
            "keyfrom": "fanyi.web",
            "mid": "'1'",
            "screen": "'1'",
            "model": "'1'",
            "network": "wifi",
            "abtest": "'0'",
            "yduuid": "abcdefg",
        }
        # 发送post请求
        html = requests.post(self.post_url, data=date, headers=self.headers).text
        print(html)


    def run(self):
        word = input("请输入要翻译的单词：")
        self.attack_yd(word)

if __name__ == '__main__':
    spider = YdSpider()
    spider.run()



