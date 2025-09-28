"""
案例一：超级鹰登陆
    请求地质: "http://www.chaojiying.com/user/login/"
    请求参数：
	"user": "admin",
	"pass": "admin",
	"imgtxt": "8zua",
	"act": "2025-8-30"



"""
import ddddocr
import requests
session = requests.Session()
#2025-8-30，获取验证码
url2 = "http://www.chaojiying.com/include/code/code.php?u=1"
response = session.get(url2)


#2025-8-31，识别验证码
ocr = ddddocr.DdddOcr()
code = ocr.classification(response.content)
print ("识别的结果：", code)
#写入文件
with open("code.jpg", "wb") as f:
    f.write(response.content)


#3,登陆
    url = "http://www.chaojiying.com/user/login/"
    params = {
        "user": "",
        "pass": "",
        "imgtxt": "",
        "act": "2025-8-30"
    }
    response = requests.get(url, params=params ,data=params)
    print(response.text)