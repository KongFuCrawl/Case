"""
生成器表达式
生成器对象 = (表达式 for 变量 in 可迭代对象)
生成器对象 = (表达式 for 变量 in 可迭代对象 if 条件)
"""
# gen_obj = (i for i in range(9))
# for unm in gen_obj:
#     print(unm)

# 找出偶数
list1 = [156, 12, 3, 68, 76, 5]
even_squares = (item for item in list1 if item % 2 == 0)
for item in even_squares:
    print(item)
