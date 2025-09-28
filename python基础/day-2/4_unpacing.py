"""
元组解包
"""
#注意力获取元素，一次赋值给左侧变量，变量个数和元素个数一致，否则报错
# tuple = (1, 2, 3, 4, 5)
# a, b, c, d,  = tuple
# print(a, b, c, d, ) ValueError: too many values to unpack (expected 4)


# tu = (1, 2, 3, 4, 5)
# a, b, c, d, e = tu
# print(a, b, c, d, e) #1 2 3 4 5


# *号解包 长度不确定的时候 把多余的元素收集起来，放到列表中
tu = (1, 2, 3, 4, 5)
a, *b = tu
print(a, b) #1 [2, 3, 4, 5]

# a, *b, *c = tu
# print(a, b, c)  # SyntaxError: multiple starred expressions in assignment


a, *b, c = tu
print(a, b, c) #1 [2, 3, 4] 5

a, b, *c = tu
print(a, b, c) #1 2 [3, 4, 5]


*a, b, c = tu
print(a, b, c) #[1, 2, 3] 4 5


