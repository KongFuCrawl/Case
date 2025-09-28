"""
反向输出所有元素 2种方法
"""
from xmlrpc.server import list_public_methods

# list_movie = ["封神", "娃哈哈", "图图", "749","闪耀","南真不备战"]
# for item in list_movie[::-1]:
#     print(item)
#
# for i in range(-1, -len(list_movie)-1, -1):
#     print(list_movie[i])
#
# for i in range(len(list_movie) -1 , -1, -1):
#     print(list_movie[i])




# print([i ** 2 for i in range (1, 21) if i % 2 == 0])




list1 = [[1, 2, 3 ], [4, 5, 6], [7, 8, 9]]
list_new = []
for item in list1:
    for sub_item in item:
        list_new.append(sub_item)

print(list_new)


# 列表推导式
print([sub_item for item in list1 for sub_item in item])


