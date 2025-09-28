"""
1:定义
    由一系列键值对组成的可变散列容器
        三列：对键进行哈希运算，确定在内存中的存储位置，每条数据存储无先后顺序
        键必须唯一不可变，值没有限制


2：创建
    字典名 = {键1：值1, 键2：值2}
    字典名 = dict(可迭代对象)


"""
from decorator import append
from django.db.models.expressions import result

# dict_movie = {"name": "749局",
#               "type": "科比",
#               "index":999696,
#               "p": "图图",
#             }
#
# print(dict_movie) #{'name': '749局', 'type': '科比', 'index': 999696, 'p': '图图'}
#
#
# #  访问，字典名[键]
# print(dict_movie["type"]) #科比
# print(dict_movie["p"]) #图图
#
#
# # 字典名[键] = 值  字典的键不存在，则是添加 ，键存在则是修改
# # 新增
# dict_movie["city"] = "中国"
# print(dict_movie)  #{'name': '749局', 'type': '科比', 'index': 999696, 'p': '图图', 'city': '中国'}
#
# #修改
# dict_movie["name"] = "人在囧途"
# print(dict_movie)  #{'name': '人在囧途', 'type': '科比', 'index': 999696, 'p': '图图', 'city': '中国'}
#
# #字典名.update() 如果键已经存在，则更新键对应的值；如果键不存在，则添加新的键值对
# dict_movie.update({"name": "赵刚", "city": "韩国"})
# print(dict_movie) #{'name': '赵刚', 'type': '科比', 'index': 999696, 'p': '图图', 'city': '韩国'}
#
#
# #  del语句 直接删除键值对  返回：无    元字典：被修改
# # # del dict_movie["name"]
#
# #pop()方法： 会返回被删除的值 ，作用：删除键值对并返回对应的值，返回值：被删除的值， 元字典被修改
# dict_movie.pop("city")
# print(dict_movie)

# dict_movie = {"name": "749局",
#                "type": "科比",
#                "index":999696,
#                "p": "图图",
#              }
#遍历
# for key in dict_movie:
#     """
#     赵刚
#     科比
#     999696
#     图图
#     """
#     print(dict_movie[key])


# values() 字典中的键值
# for value in dict_movie.values():
#     print(value)

# items() 获取字典中的键和键值
# for key, value in dict_movie.items():
#     print(key, value)


"""
1:字典推导式
    （1）定义：使用简洁方法将迭代对象转换为字典
    （2）语法：字典名 = {键：值 for 变量 in 可迭代对象}
                字典名 = {键：值 for in 可迭代对象 if 条件} 
    
"""

# 练习 把2个列表合并成一个字典
# list_name = ["c++", "java", "python","php"]
# list_pop = [66, 77, 88, 99]
#
# dict_new = {list_name[i]: list_pop[i] for i in range(len(list_name))}
#
# print(dict_new) #{'c++': 66, 'java': 77, 'python': 88, 'php': 99}



# 调到字典的键和值
# dict_area = {"1": "上海", "2": "北京", "3": "河南", "4":"山西"}
#
# dict_new = {}
#
# for key, value in dict_area.items():
#     dict_new[value] = key
#
# dict_new = {value: key for key, value in dict_area.items()}
#
# print (dict_new) #{'上海': '1', '北京': '2', '河南': '3', '山西': '4'}



"""
综合练习
    1：创建字典存储 弯弯地区名，新增感染人数 现有感染人数
    给弯弯新增加累计感染人数， 治愈人数，给弯弯的新增感染人数100, 治愈人数增加20 
        输出所有弯弯地区的信息
            删除新增感染人数
"""

# dict_area = {
#     "region": "弯弯",
#     "new": 26,
#     "now": 65
# }
# #添加
# dict_area["total"] = 4965
# dict_area["cure"] = 699
#
# #新增
# dict_area['new'] += 100
# dict_area["cure"] += 20
#
# for key, value in dict_area.items():
#     print(f"{key}: {value}")
#
# del dict_area['new']





# """
# 现有一个字典 {'a': 1, 'b': 2, 'c': 3,'d': 4}, 编写程序给字典的值进行分组， 新字典：{1:['a','b'],2:['b','e'],3:['d']}
# """
# dict1 = {"a": 1, "b": 2, "c":3, "d":4}
# dict_new = {}
# for key, value in dict1.items():
#     if value in dict_new:
#         dict_new[value].append(key)
#     else:
#         dict_new[value] = [key]
# print(dict_new) #{1: ['a'], 2: ['b'], 3: ['c'], 4: ['d']}






