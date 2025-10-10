"""
高阶函数
sorted(可迭代对象,key=函数，reverse=bool)
"""

list1 = [11, 22, 33, 43, 51, 6, 7]
print(sorted(list1))
print(sorted(list1, reverse=True))

people = [
    {"name": "Chris", "age": 20},
    {"name": "C", "age": 28},
    {"name": "Chr", "age": 22},
    {"name": "Ch", "age": 25},
]
# sorted基于 Timsort算法
print(sorted(people, key=lambda people: people["age"]))





