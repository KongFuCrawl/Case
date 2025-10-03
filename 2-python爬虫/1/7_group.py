"""
正则表达式分组示例

"""

import re

html = 'A B C D'
pattern = re.compile(r'\w+\s+\w+',re.S)
r_list = pattern.findall(html)
print(r_list)
#结果 ：['A B', 'C D']

pattern = re.compile(r'(\w+)\s+\w+',re.S)
r_list = pattern.findall(html)
print(r_list)
#结果：['A', 'C']

pattern = re.compile(r'(\w+)\s+(\w+)',re.S)
r_list = pattern.findall(html)
print(r_list)
#结果：[('A', 'B'), ('C', 'D')]



