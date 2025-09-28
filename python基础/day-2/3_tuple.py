"""
元组 (数据结构) （可迭代对象）
    由一系列变量组成的不可变序列容器
        不可变：一旦创建，不允许在添加，删除，修改元素

"""
# #1.创建
# he = (1, 2, 3)
# # 如果元组只有1个元组，必须有逗号
# tu = ("剧情")
# tuple1 = "tutu",
# print(tuple1)
# print(he)
# print(type(he))
# print(type(tu))
#
#
# #2.索引和切片
# print(he[0])
# print(he[::-1])
#
#
# #3.遍历
# for item in he:
#     print(item)
#
#
#
# #4.常用的函数
# tuple2 = (1, 2, 3, 4)
# print(len(tuple2))
# print(max(tuple2))
# print(min(tuple2))
# print(sum(tuple2))


tuple_day = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

month = int(input("请输入月份："))
day = int(input("请输入日："))

# print(tuple_day[:month - 1])

days = sum(tuple_day[:month - 1]) + day
print(days)



