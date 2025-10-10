"""
内置生成器 zip
"""
# lst1 = [1, 2, 3, 4, 5,]
# lst2 = [1, 2, 3, 4, 5, 6, ]
# lst3 = [1, 2, 3, 4, 5, 6, 7, ]
# lst4 = [1, 2, 3, 4, 5, 6, 7, 8, ]
# list_zipped = list (zip(lst1, lst2, lst3, lst4))
#
#
# print(list_zipped)




"""
把2个列表合并成一个字典
"""
# list1 = ["name", "age", "sex"]
# list2 = ["xiaoyi", "18", "男"]
#
# # print(dict(zip(list1, list2)))
#
#
#
#
#
#
# # 解包
# tpll, tpl2 = zip(*zip(list1, list2))
# print(tpll, tpl2)








"""
矩阵转置
2行3列   3行2列
"""
# list_map = [
#     [1, 2,3],
#     [4, 5,6]
# ]
#
#
# list_new = [list(item) for item in list(zip(*list_map))]
# print(list_new)






"""
内置生成器 enumerate
"""
list1 = ["xiaoyi", "女", 18]

for item in list1:
    print(item)

for i, val in enumerate (list1):
    print(i, val)








