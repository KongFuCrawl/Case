#引入模块
# import random
#
# # 随机数
# rand = random.randint(1, 100)
# print(rand)
#
# count = 0
# while True:
#     count = int(input("请输入数字："))
#     count += 1
#
#     if count > rand:
#         print("猜大了")
#     elif count < rand:
#         print("猜小了")
#     else:
#         print(f"猜对了，猜了{count}次")
#         break


# num_count = 0
# even_count = 0
#
# while True:
#     number = int(input("请输入数字："))
#     num_count += 1
#
#     if number > 0:
#         print("正数")
#
#         if number % 2:
#             print("奇数")
#         else:
#             print("偶数")
#             even_count += 1
#
#     elif number < 0:
#         print("负数")
#     else:
#         print(f"用户输入{num_count}次数字，有{even_count}偶数")
#         break





"""
    求10到60之间，个数位不能是 2 5 8 的整数的数字之和
"""

# number = 10
# total = 0
# while number <= 60:
#     print(number)
#     unit = number % 10
#     if unit == 2 or unit ==5 or unit ==8:
#         number += 1
#         continue
#     total += number
#     number += 1
# print(total)



