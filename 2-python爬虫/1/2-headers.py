from wsgiref import headers

import requests
url = 'https://httpbin.org/get'
headers={
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
}
html = requests.get(url=url,headers=headers).text

print(html)