"""
    算术运算符
    + - * /
    //整除
    % 求余
    ** 幂
"""
# a = 9
# b = 2
#
# print(a + b) # 11
# print(a - b) # 7
# print(a * b) #18
# print(a / b) # 4.5
# print(a // b) # 4
# print(a % b) # 1
# print(a ** b) # 81
#
# total = 36
# jin = total // 16
# liang = total % 16
# print (jin,"斤", liang,"两")
# print (f"{jin}斤{liang}两")



"""
在终端输入4为数，计算单位相加的和
"""
number = int (input("请输入四位整数："))
print(type(number))

# 个
unit1 = number % 10

# # 十
unit2 = number // 10 % 10
#
# # 百
unit3 = number // 100 % 10
#
# # 千
unit4 = number // 1000
print(unit1 + unit2 + unit3 + unit4)




