"""
1,定义：在不修改原函数定义的情况下，为函数添加额外功能的函数
"""

# 装饰器函数
# def nuw(func):
#     def inner(m, n):
#         print("新")
#     return inner
#
# @nuw
# def old(m, n):
#     print("旧", m + n)
#
# old(2, 3)







"""
定义一个权限验证装饰器，查看是否有权限运行某个函数，admin权限才能执行函数
"""
# def permission(func):
#     def inner(str_per):
#         if str_per in ["admin", "user"]:
#             if str_per == "admin":
#                 func(str_per)
#             else:
#                 print("无权限")
#         else:
#             print("权限异常")
#
#     return inner
#
#
# @permission
# def delete(str_per):
#     print(f"{str_per},删除")
#
# delete("admin") # admin,删除
# delete("user") # 无权限
# delete("text") # 权限异常








"""
定义一个函数计算0到参数n之间的和，使用装饰器扩展函数添加到打印时间的功能
    消耗了25.265241秒
"""
from datetime import datetime

def print_time(func):
    def inner(n):
        start = datetime.now()
        res = func(n)
        end = datetime.now()

        print(f"消耗了{(end - start).total_seconds()}秒")

        return res
    return inner

@print_time
def sum_date(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

print(sum_date(1000000000)) #消耗了25.265241秒





