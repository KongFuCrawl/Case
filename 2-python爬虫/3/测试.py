import requests
import time
import random
import hashlib
import base64
from Crypto.Cipher import AES
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def selenium_translate(word):
    """使用Selenium模拟真实浏览器操作"""
    driver = webdriver.Chrome()  # 需要安装ChromeDriver
    try:
        driver.get("https://fanyi.youdao.com/")

        # 等待页面加载
        wait = WebDriverWait(driver, 10)

        # 找到输入框
        input_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea")))
        input_box.clear()
        input_box.send_keys(word)

        # 等待翻译结果
        time.sleep(3)

        # 获取翻译结果
        result_element = driver.find_element(By.CSS_SELECTOR, ".targetText")
        translation = result_element.text

        return translation

    except Exception as e:
        print(f"Selenium翻译失败: {e}")
        return None
    finally:
        driver.quit()


# 测试
print(selenium_translate("你好"))
class YoudaoTranslator:
    def __init__(self):
        self.post_url = 'https://dict.youdao.com/webtranslate'
        self.headers = {
            "Host": "dict.youdao.com",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://fanyi.youdao.com",
            "Connection": "keep-alive",
            "Referer": "https://fanyi.youdao.com/",
            "Cookie": "OUTFOX_SEARCH_USER_ID=1204419532@123.13.67.120; OUTFOX_SEARCH_USER_ID_NCOO=1812469373.2692113; YOUDAO_MOBILE_ACCESS_TYPE=1; __adroll_fpc=b3a3bb7e55a2ce65fb7b7686e3725eba-1760252400700; DICT_DOCTRANS_SESSION_ID=Y2EwMDkxN2QtN2Q5Mi00ZGZlLWJmYWEtNmVlNzgwOTRlODI5; _uetsid=0db1c7c0a73811f0be61f3a3f0f14684; _uetvid=0db1b140a73811f0941a8fcdfcea7a9f",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site"
        }

    def get_ts_salt_sign(self, word):
        """生成时间戳、salt和签名"""
        ts = str(int(time.time() * 1000))
        salt = ts + str(random.randint(0, 9))

        # 签名算法
        string = "fanyideskweb" + word + salt + "mmbP%A-r6U3Nw(n]BjuEu"
        sign = hashlib.md5(string.encode()).hexdigest()
        return ts, salt, sign

    def decrypt_response(self, encrypted_text):
        """解密有道翻译响应"""
        try:
            key_str = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
            iv_str = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"

            key = hashlib.md5(key_str.encode()).digest()
            iv = hashlib.md5(iv_str.encode()).digest()

            # Base64解码
            encrypted_text = encrypted_text.replace('-', '+').replace('_', '/')
            pad_len = len(encrypted_text) % 4
            if pad_len:
                encrypted_text += '=' * (4 - pad_len)

            encrypted_data = base64.b64decode(encrypted_text)

            # 确保长度正确
            if len(encrypted_data) % 16 != 0:
                encrypted_data += b'\x00' * (16 - len(encrypted_data) % 16)

            # AES解密
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(encrypted_data)

            # 去除填充
            try:
                pad_len = decrypted[-1]
                if 1 <= pad_len <= 16:
                    decrypted = decrypted[:-pad_len]
            except:
                pass

            # 直接解码
            result = decrypted.decode('utf-8')
            return result

        except Exception as e:
            print(f"解密失败: {e}")
            return None

    def translate(self, word, from_lang="auto", to_lang="auto"):
        """翻译单词"""
        ts, salt, sign = self.get_ts_salt_sign(word)

        data = {
            "i": word,
            "from": from_lang,
            "to": to_lang,
            "useTerm": "false",
            "domain": "0",
            "dictResult": "true",
            "keyid": "webfanyi",
            "sign": sign,
            "client": "fanyideskweb",
            "product": "webfanyi",
            "appVersion": "1.0.0",
            "vendor": "web",
            "pointParam": "client,mysticTime,product",
            "mysticTime": ts,
            "keyfrom": "fanyi.web",
            "mid": "1",
            "screen": "1",
            "model": "1",
            "network": "wifi",
            "abtest": "0",
            "yduuid": "abcdefg",
        }

        try:
            print(f"\n=== 翻译: {word} ===")
            print(f"签名: {sign}")
            print(f"时间戳: {ts}")

            response = requests.post(self.post_url, data=data, headers=self.headers, timeout=10)
            print(f"状态码: {response.status_code}")
            print(f"响应长度: {len(response.text)}")

            if response.status_code == 200:
                # 解密响应
                decrypted = self.decrypt_response(response.text)

                if decrypted:
                    print("解密成功!")
                    print(f"原始解密: {decrypted}")

                    # 解析JSON
                    try:
                        data = json.loads(decrypted)
                        if data.get("code") == 0 and "translateResult" in data:
                            translate_result = data["translateResult"]
                            if translate_result and len(translate_result) > 0:
                                first_result = translate_result[0]
                                if isinstance(first_result, list) and len(first_result) > 0:
                                    first_result = first_result[0]

                                return {
                                    "success": True,
                                    "src": first_result.get("src", ""),
                                    "tgt": first_result.get("tgt", ""),
                                    "type": data.get("type", ""),
                                    "raw_data": data
                                }

                        return {"success": False, "error": "未找到翻译结果", "raw_data": data}

                    except json.JSONDecodeError as e:
                        return {"success": False, "error": f"JSON解析失败: {e}", "raw_text": decrypted}
                else:
                    return {"success": False, "error": "解密失败"}
            else:
                return {"success": False, "error": f"请求失败: {response.status_code}", "response": response.text}

        except Exception as e:
            return {"success": False, "error": str(e)}


def main():
    translator = YoudaoTranslator()

    # 测试多种翻译
    test_cases = [
        ("hello", "auto", "auto"),
        ("老虎", "auto", "auto"),
        ("world", "auto", "auto"),
        ("苹果", "zh-CHS", "en"),
        ("你好", "zh-CHS", "en")
    ]

    for word, from_lang, to_lang in test_cases:
        result = translator.translate(word, from_lang, to_lang)
        print("\n" + "=" * 60)
        if result["success"]:
            print(f"✅ 翻译成功!")
            print(f"原文: {result['src']}")
            print(f"结果: {result['tgt']}")
            print(f"类型: {result['type']}")
        else:
            print(f"❌ 翻译失败: {result['error']}")
        print("=" * 60)
        time.sleep(2)  # 添加延迟避免请求过快


if __name__ == '__main__':
    main()