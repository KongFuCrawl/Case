"""
函数：（组织代码的方式）
    一段组织好能够实现一定功能的代码，可重复使用
"""

#函数定义
# def 关键字 define
# add1 函数名 功能的描述
# 函数体 完成功能的代码
# def add1():
#         print(1+2)
#
# #函数调用(只有调用才会执行代码)  函数名()
# add1()
#
#
# # 写在函数定义时的小括号内的参数，称为形式参数，也叫形参(数量0个及0个以上)
# def add2(m,n):
#     # m , n 本质上就是变量
#     print(m+n)
#
# # 写在函数调用时的小括号内的参数，称为实际参数，也叫实参
# add2(1, 2)
# add2(5, 2)




"""
定义一个函数 接受2个整数和一个符号作为参数，完成四则运算
"""
# def add1(s, n):
#     print(s + n)
#     print(s - n)
#     print(s * n)
#     print(s / n)
#
# add1(999, 666)


# def calc(num1, num2, f):
#     if f == "+":
#         print(num1 + num2)
#     elif f == "-":
#         print(num1 - num2)
#     elif f == "*":
#         print(num1 * num2)
#     elif f == "/":
#         if num2 == 0:
#             print("除数不能为0")
#         else:
#             print(num1 / num2)
#     else:
#         print("符号异常")
#
# num1 = int(input("请输入数字1:"))
# num2 = int(input("请输入数字2："))
# f = input("请输入运算符：")
#
# calc(num1, num2, f)






"""
定义一个函数 接受一个字符串作为参数，判断是不是回文符串
    忽略大小写和非数字字符
"""
# def is_palindrome(s):
#     clean_str = "".join([char.lower() for char in s if char.isalpha()])
#     print(clean_str)
#
#
#
#
# str1 = "上海自来水来自上海"
# str2 = "A man, a plan, a canal: Panama"
# str3 = "HELLO WORLD"
#
#
# is_palindrome(str1)
# is_palindrome(str2)
# is_palindrome(str3)



#3 return 只能返回一个值
#1 return返回函数的执行结果
# def func1(m, n):
#     return m + n
#
# res = func1(10, 20)
# print(res)  #30
#
#
# #2
# def func2():
#     print("func2执行")
#     return
# res = func2()
# print(res)  #None
#
#
#
# # 3 return可以退出函数
# def func3():
#     print("func3执行1")
#     return
# print("func3执行2")
# func3()  #func3执行1






# """
# 练习
#     封装一个函数 计算并打印1到100之间的所有的平方和
# """
# def print_square_sum():
#     square_sum = 0
#     for i in range(1, 101):
#         square_sum += i**2
#     print(f"1到100之间所有整数的平方和是：{square_sum}")
# # 调用函数
# print_square_sum()  #1到100之间所有整数的平方和是：338350





"""
练习
    封装一个计算器的函数接受用户在终端输入任意2个数字及符号，实现四则运算并打印相关运算结果
"""
# def calc(num1, f, num2):
#     if f == "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     elif f == "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     elif f == "*":
#         print(f"{num1} * {num2} = {num1 * num2}")
#     elif f == "/":
#         if num2 == 0:
#             print("除数不能为0")
#         else:
#             print(f"{num1} / {num2} = {num1 / num2}")
#
#     else:
#         print("暂不支持此运算符")
#
# num1 = float(input("请输入数字1："))
# f = input("请输入运算符号：")
# num2 = float(input("请输入数字2："))
#
# # 调用函数
# calc(num1, f, num2)




"""
声明一个函数，接受一个列表作为参数，打印列表时能够同时被3和5整除的数字
"""
# list = [1, 15, 86, 7, 9, 22, 30]
#
# def fn(lst):
#     list_new = []
#     for item in lst:
#         if not item % 3 and not item % 5:
#             list_new.append(item)
#         print(list_new)
#
# fn(list) # [15, 30]







"""
实参传递方式argument
"""
# 位置传参：实参与形参的位置依次对应
# def func1 (p1, p2, p3):
#     print(p1)
#     print(p2)
#     print(p3)
#     # print(p1, p2, p3)
# # 位置实参
# func1(1, 2, 3)



# """
# 关键字参数
#     实参根据形参的名字进行对应
# """
# def func1 (p1, p2, p3):
#     print(p1)
#     print(p2)
#     print(p3)
#
# func1(p3=1, p1=2, p2=3) #231
# func1(2, p2=3, p3=1) #231
# # func1(p2=3, p3=1, 2)  # 报错



"""
序列参数：
    实参用*将序列拆解后与形参的位置一次对应
"""
# def func1(p1, p2, p3):
#     print(p1)
#     print(p2)
#     print(p3)
#
# dict = {
#     "cn":110,
#     "en":120,
#     "ma":130
# }
# func1(*[1, 2, 3]) # 1 2 3
# func1(*[11, 22, 33]) # 11  22  33
#
# """
# 序列传参中 *dict 默认是键
# 如果想要值可以使用 *dict.values()
# 如果使用 *dict.items() 形参接受到值则是包含字典键值对的元组，元组的第一个元素是字典的键，第二个元素是字典的值
# """
# func1(*dict.items()) # ("cn",110) ("en",120) ("ma",130)







