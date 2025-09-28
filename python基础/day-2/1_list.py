"""
容器类型-列表
由一系列变量组成的可变序列容器
可变：创建完成之后还可以继续删除，添加，修改
序类：有序的
容器：可以装多个数据
"""
from PIL.DdsImagePlugin import item

# 1.创建
# list_movie = ["小明", "小红", "图图", "小新", "费岩羊", "村长", "喜羊羊"]
# list_age =[18, 22, 19]

# 2.获取单个元素(索引) 索引从0开始 ,
# 正向：从0开始 最大索引 长度-1
# 反向：从-1开始
# print(list_movie[1]) #小红
# print(list_movie[-1]) #图图
#print(list_movie[5]) #索引越界：IndexError: list index out of range
#print(list_movie[-5]) #索引越界:IndexError: list index out of range


# 多个元素(切片)[开始：结束：步长]
# 包含开始，不包含结束 默认从0开始，步长为1
#[开始：结束]
# print(list_movie[2:6])
# # [开始：结束：步长]
# print(list_movie[1:6:2])
# #[:结束]
# print(list_movie[4:])
# #[开始：]
# print(list_movie[:3])

#
# print(list_movie)


# city_list = ["北京", "天津", "杭州", "广州", "山西", "山东"]
# print(city_list[1])
# print(city_list[4:5])
# print(city_list[2:5])
#
# print(city_list[::2])
# print(city_list[:5:2])

#[::步长] 如果步长为负数，开始和结束的值会自动切换
#反向切片
# print (city_list[::-2])
# print (city_list[::-3])



# city_list = ["北京", "天津", "杭州", "广州", "山西", "山东"]
# # 3.修改
# city_list[5] = "微笑"
# print(city_list) #

# # 4.删除
# del city_list[5]# ['北京', '天津', '杭州', '广州', '山西']
# del city_list[::5] #['天津', '杭州', '广州', '山西']
#del city_list[::2] #['杭州', '山西']

#值 删除第一个匹配的值
# city_list.remove("山东") #['北京', '天津', '杭州', '广州', '山东']
# city_list.remove("微笑")
# print(city_list)


# # 5.添加
# city_list.append("微笑")
# city_list.append("风神")
# city_list.append("微笑")
# city_list.insert(1,"中间人")
# city_list.insert(3, "图图")
# city_list.extend(["山河", "地理"])
# print(city_list)





#6.遍历 按照顺序逐一访问数据结构中的每个元素的过程
# for item in city_list:
#     print(item) # 列表中的每个元素

# 还有那种for循环遍历的写法
# for i in range(len(city_list)):
#     print(city_list[i])




# list_planet = ["水星", "金星", "火星", "木星","木星"]
# list_planet.insert(2, "地球")
# list_planet.extend(["土星", "天王星", "海王星"])
#
# print(list_planet[0])
# print(list_planet[-1])
# print(list_planet[:2])
#
# # list_planet.reverse("海王星")
# del list_planet[3]
#
# for item in list_planet[::-1]:
#     print(item)


"""

"""
# list_movie = ["昆迟延", ["门铃", "娃娃"]]
# print(list_movie[0]) #昆迟延
# print(list_movie[1]) #['门铃', '娃娃']
# print(list_movie[1][0]) #门铃
# print(list_movie[1][1])  #娃娃

#
# # 1 赋值
# list_new1 = list_movie
# list_new1[0] = "图图"
# list_new1[1][0] = "残阳"
# print(list_new1)



# list_number = [66, 23, 15, 78, 22]
# list_new = []
# for i in list_number:
#     if item % 2 == 0:
#         list_new.append(item)
# print(list_new)
#
# # 列表推导式
# list_new = [item for item in list_number if item % 2 == 0]
# print(list_new)













