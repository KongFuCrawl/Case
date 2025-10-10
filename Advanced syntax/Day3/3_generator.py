"""
生成器 是组织代码的一中方式 是一种特殊的迭代器（惰性求值）是一种能够动态的提供数据的可迭代对象
惰性求职：不是一次加载所有数据到内存，而是按需动态生成
"""

# 函数中包含 yield 关键字 就是生成器函数  返回生成器（可迭代对象）
def my_range(stop):
    start = 0
    while start < stop:
        yield start
        start += 1

print(my_range(3)) # <generator object my_range at 0x72eedf545c00>


for i in my_range(5):
    print(i)










