"""
使用生成器思想找出列表中的偶数
"""
# def find_even(lst):
#     for item in lst:
#         if item % 2 == 0:
#             yield item
#
# list1 = [156, 12, 3, 68, 76, 5]
# for item in find_even(list1):
#     print(item)




"""
使用生成器表达式找出列表中的整数 2种方法
"""
# list1 = ["C++", 12.3, True, 8, 0]
# gen_obj1 = (item for item in list1 if type(item) == int)
# gen_obj2 = (item for item in list1 if isinstance(item, int))
#
# for item1 in gen_obj1:
#     print(item1)
#
#
#
# # print(list(gen_obj2))
# print(tuple(gen_obj2))






list_nums = [1, 2, 3]
list_letters = ["a", "b", "c"]

pairs = ((num, letter) for num in list_nums for letter in list_letters)
for item in pairs:
    print(item)






