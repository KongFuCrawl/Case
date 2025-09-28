"""
    流程控制-分支
        根据条件选择性的执行代码
"""


# time = 19
#
# if time >= 18:
#     print( input("成年"))
#
# else:
#     print("未成年")





"""
    比较2个数字的大小
        如果 a > b 则交换2个变量的值，然后输出，否则直接输出
"""

# a = 10
# b = 3
#
# if a > b:
#      temp = a
#      a = b
#      b = temp
#      print(a , b)
# else:
#      print(a, b)




"""
    0 待付款 1待收货  2待发货  3待平价
"""

# status = 3
# if status == 0:
#     print ("待付款")
# elif status == 1:
#     print("待收货")
# elif status == 2:
#     print("待发货")
# elif status == 3:
#     print("待评价")


# score = int(input("请输入成绩:"))
#
# if score == 100 :
#     print("满分")
# elif score >= 90 and score <= 100 :
#     print ("优秀")
# elif score >= 60 and score <= 90 :
#     print ("良好")
# elif score >= 0 and score <= 60 :
#     print("继续努力")
# else:
#     print("成绩无效")


# score = int(input("请输入成绩:"))
#
# # 判断边界
# if score < 0 or score > 100:
#     print ("成绩无效")
# elif score == 100:
#     print ("满分")
# elif score >= 90:
#     print ("优秀")
# elif score >= 60:
#     print ("及各")
# elif score >= 0:
#     print("继续努力")



number = int(input("请输入数字："))

if number % 2 == 0:
    print("偶数")
else:
    print("奇数")

if number % 2:
    print ("奇数")
else:
    print("偶数")

if number % 2:
    print("奇数")
else:
    print("偶数")





