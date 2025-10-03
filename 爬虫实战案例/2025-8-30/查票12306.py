import requests
import json

# 创建会话
session = requests.Session()

# 完整的浏览器头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

session.headers.update(headers)

# 先模拟浏览器访问流程
print("2025-8-30. 访问首页...")
home_url = 'https://www.12306.cn/index/'
session.get(home_url)

print("2025-8-31. 访问查询页面...")
query_page = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
session.get(query_page)

# 然后查询
print("3. 查询车票...")
api_url = 'https://kyfw.12306.cn/otn/leftTicket/query'
params = {
    'leftTicketDTO.train_date': '2025-08-31',
    'leftTicketDTO.from_station': 'BJP',
    'leftTicketDTO.to_station': 'XNO',
    'purpose_codes': 'ADULT',
}

response = session.get(api_url, params=params)

print(f"状态码: {response.status_code}")
print(f"最终URL: {response.url}")

# 检查响应
if 'text/html' in response.headers.get('Content-Type', ''):
    print("❌ 被重定向到HTML页面")
    print("前100字符:", response.text[:100])
else:
    try:
        data = response.json()
        print("✅ 成功获取JSON数据!")
        print(json.dumps(data, ensure_ascii=False, indent=2))
    except:
        print("响应内容:", response.text[:200])
