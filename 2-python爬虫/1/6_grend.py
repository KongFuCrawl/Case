"""
    他贪婪匹配和非贪婪匹配演示

"""

import re

html = '''
<div><p>人无远虑。必有近忧</p></div>
<div><p>人无进忧。必有远虑</p></div>>
'''
#贪婪匹配
#pattern = re.compile('<div><p>.*</p></div>', re.S)

#非贪婪匹配
#pattern = re.compile('<div><p>.*?</p></div>', re.S)

#正则表达式的分组<div><p>(.*?)</p></div>
pattern = re.compile('<div><p>(.*?)</p></div>', re.S)
r_list = pattern.findall(html)
print(r_list)