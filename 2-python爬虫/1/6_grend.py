"""
    贪婪匹配和非贪婪匹配
"""

import re

html = '''
<div><p>明日复明日明日和日期多</p></div>
<div><p>美国联邦政府“停摆”11日进入第11天，对公众的影响日益显现。总统特朗普表示，他已命令国防</p></div>

'''
# 贪婪匹配（默认）.*
# pattern = re.compile('<div><p>.*</p></div>', re.S)
# r_list = pattern.findall(html)
# print(r_list)

# 非贪婪匹配 .*?
# pattern = re.compile('<div><p>.*?</p></div>', re.S)
# r_list = pattern.findall(html)
# print(r_list)



# 非贪婪匹配 (.*?)
pattern = re.compile('<div><p>(.*?)</p></div>', re.S)
r_list = pattern.findall(html)
print(r_list)





