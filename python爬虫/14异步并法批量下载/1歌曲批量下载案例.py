"""
https://www.myfreemp3.com.cn/

"""
import requests
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

res = requests.post(url,data=params,headers=headers)

print(res.json())
