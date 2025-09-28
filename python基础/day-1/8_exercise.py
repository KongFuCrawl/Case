# dis = float(input("请输入位移："))
# time = float(input("请输入时间："))
# vel = float(input("请输入初速度"))
# a = (dis - vel * time) / (time ** 2 / 2)
# print(f"加速度是{a}")




# s = float(input("输入边长s："))
# d = float(input("输入边长d:"))
# v = float(input("输入边长v:"))
#
# if s + d > v and s + v > d and d + v > s:
#     if s == d and d == v:
#         print("等边")
#     elif s ==d or d ==v or s == v:
#         print("等腰")
#     else:
#         print("普通")
# else:
#     print("无法构成三角形")




six = input("请输入性别：")
if six == "男":
    print("你好先生")
elif six == "女":
    print("你好女士")
elif six == "小孩":
    print("作业写完了麻？")
else:
    print("输入错误")