"""
高阶函数

filter(函数，可迭代对象)
"""

# list1 = [1, 2, 3, 4, 5]
# print(list(filter(lambda item: not item % 2, list1)))






"""
找出字符串包含 "ap" 字符串的元素
"""
words = ["APPLE", "cherry", "cotapir", "apart"]

print(list(filter(lambda words: "ap" in words.lower(), words)))







