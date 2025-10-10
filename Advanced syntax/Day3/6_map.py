"""
高阶函数
1.如果一个函数返回一个函数
2,如果一个函数能够接受一个函数作为参数
"""

#map(函数，可迭代对象)

def calc(item):
    return item * 2


list1 = [1, 2, 3, 4, 5]
print(list(map(lambda item: item * 2, list1)))



