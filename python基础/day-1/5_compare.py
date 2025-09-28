"""
    比较运算符
    >  >=  <  <=   ==    !=
"""

# print(1>2)  # False
# print (2>1) # True
#
# print (3>=1) #True  大于或等于>=   小于或等于 <=
# print (1>=1) #True
# print (1<=1) #True
#
# #字符串比较 逐位比较 字典序(unicode码点)
# print ("5">="20") # True
# print ("ass" < "llll") #True
#
#
# # 比较两个值相等 相等返回True 反之返回False
# print (1==1) # True
# print (1==2) # False
#
# # 比两个值不相等 不相等反复True 反之返回False
# print (1!=2) #True


number = int(input("请输入一个整数:"))

res1 = number % 2 != 0
res2 = number % 2 == 0
print(res1, res2)


