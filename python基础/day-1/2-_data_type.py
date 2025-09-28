# 整型 int 整数
# int1 = 6.66666666
# int2 = 2
# int3 = -6.6666
# print (type(int2)) #<class 'int'>
# print (type(int1)) #<class 'float'>
# print (type(int3)) #<class 'float'>
#
# #整数会打印出int 非整数会打印float也就是浮点数或小数
# int4 = 111111111111.111111111
# int5 = 6
# print (type(int5)) #<class 'int'> 小数
# print (type(int4)) #<class 'float'> 浮点数
#
#
#
# int = 7
# age = 6.666666
# print (type(age)) #<class 'float'> 打印结果是float而不是代码float
# print (type(int)) # <class 'int'> 打印结果是int而不是代码int

# int = 8
# age = 9.999
# print (type(int))#<class 'int'>
# print (type(age))#<class 'float'>

# age1 = 9
# age2 = age1
# age1 = 6.66
# print (type(age1))#<class 'float'>
# print (type(age2))#<class 'int'>


# age2 = 666666
# age7 = age2
# age2 = 9999.99
# print (type(age7)) #<class 'int'>
# print (type(age2)) #<class 'float'>


# age3 = 6.178936
# age0 = age3
# age3 = 0.233261
# print (type(age0)) #<class 'float'>
# print (type(age3)) #<class 'float'>
#
# age = 12536.999
# age3 = age
# age = 66666
# print (type(age3)) #<class 'float'>
# print (type(age)) #<class 'int'>

# age = 16
# age5 = age
# age = 17.6666
# print (type(age)) #<class 'float'>
# print (type(age5)) #<class 'int'>

# int = 18
# float = 19.14
# ast = float
# a = int
# print (type(ast)) #<class 'float'>
# print(type(a))  #<class 'int'>


# age = 20
# age2 = 21.2121212121
# age5 = age
# age6 = age2
# print(type(age5)) #整数int
# print(type(age6)) #非整数小数float



# age = 22.222222
# age1 = -23
# age0 = age
# age00 = age1
# print (type(age0)) #<class 'float'> 负数和正数都有小数和整数也就是负整数和正整数
# print(type(age00)) #<class 'int'> 负数和正数都有小数和整数也就是负整数和正整数







# # 浮点数 float 小数
# float1 = 3.14
# float2 = -3.14
# float3 = 7.16
# float4 = 0.1
# float5 = 1.23e-2
# float6 = 1.2345e2
# print (float6) #123.45
# print (float5) #0.0123
# print (type (float3)) #<class 'float'>
#
#
#
#
# # 字符串 str 文本信息
# str2 = "小蕊"
# str1 = "1"
# print (type(str2)) #<class 'str'>

# age = "靓仔"
# age1 = "23"
# age3 = '3'
# age4 = '4'
# int = '5'
# float = '6'
# float7 = '7'
# Float7 = '8'
# age = '图图9'
# builtins = '10'
# s = '11'
# x = '12'
# w = '13'
# q = '14'
# print (type(q))
# print (type(w))
# print (type(x))
# print(type(s))
# print(type(builtins))
# # print (type(age))
# # print (type(Float7))
# # print(type(float7))
# # print(type(float)) #变量名
# # print (type(int))  #<class 'str'>
# # print (type(age4)) #<class 'str'>
# # print (type(age3)) #<class 'str'>不区分单双引号但是必须是英文字符
# # print (type(age)) #<class 'str'>
# # print (type(age1)) #<class 'str'>




# # 布尔 bool 表示真和假
# bool1 = True #真
# bool2 = False #假
# print (type (bool2)) #<class 'bool'>

# a1 = False
# a = True
# s = False
# d = True
# b = False
# print(type(b))
# print(type(a1))
# print(type(a1))
# print(type(a))

#数据类型的转换
# 转为整形 int()
# print (int(1.11111)) #1
# print (int(True)) #1
# print (int(False)) #0
# print (int(-1.11111)) #-1
# print (int(0.1111)) #0
# print (int(0.1111)) # 0
# print (int(0.22222)) #0
# print(int(True))  #1
# print(int(False)) #0
# print(int(10.111111)) #10
# print(int('1.1111'))#会报错

#转为浮点也就是小数,可以将整数转为浮点数小数
# print (float(1)) #1.0
# print (float(2))  #2.0
# print (float(3)) #3.0
# print (float(True)) #1.0
# print (float(False)) #0.0
# print (float(6)) #6.0
# print (float(7)) #7.0
# print (float(8)) #8.0
# print (float(9)) #9.0
# print (float(10)) #10.0




# 转为字符串 str() 添加str的目的是为了确认字符
# print (str('太阳'))
# print (str(-1))
# print (str(22))
# print (str('0.36'))
# print (str("9999"))
# print (str('图图'))
# print (str("小明"))


# print (bool(11)) #True
# print (bool(0)) #False
# print (bool(-1))#True     某些运算场景下只有0才是False
# print (bool(0.0))  #False
#
# #非空字符串就是true
# print (bool('0')) # True
# print (bool('1')) #True
# print (bool('-1')) # True
# print (bool('')) #False
# print (bool("")) #False
# print (bool(" ")) #True
# print (bool(' ')) #True





"""
    数据类型的转换
    自动转换 强制转换
"""
# int + float = float
# print (1 + 2.5) #3.5
#
#
# #int + bool = int
# print (1 + True) #2 True为1
# print (1+ False) #1  False为0


#bool + bool =int
# print (False + True) #1

# str1 = "3.5"
# print(int(float("3.5")))

# print (1 * 1) #1
# print (1 * 2) #2
# print (4 * 3) #12

#转为bool bool()
# print(bool(0)) #False
# print(bool(1)) #True
# print(bool(-1)) # True 某些时候只有0才是False
# print(bool(0.0)) # False
#
# # 非空字符串就是ture
# print(bool("0")) # True
# print(bool("1")) # True
# print(bool(" ")) # True
# print(bool("")) # False 空格都没有就是空




str1 = "3.5"
print(int(float(str1)))








