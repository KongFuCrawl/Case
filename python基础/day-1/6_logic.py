"""
    逻辑运算 返回布尔值

    and :逻辑与 且的关系 一假俱假 全真才是真

    or ：逻辑或 或者的关系 一个真就是真 全假才是假

    not：逻辑非 取反
"""

# # and :逻辑与 且的关系 一假俱假 全真才是真
# print (1 < 2 and 2 == 2) # True
# print (2 < 2 and 2 == 2) # False
# print (0 < 1 and 0 != 0) # False
#
# # or ：逻辑或 或者的关系 一个真就是真 全假才是假
# print (0 > 1 or 2 == 1) #False
# print (0 < 1 or 1 == 2) #True
#
#
# # not：逻辑非 取反
# print (not True) # False
# print (not False)  # True



# year = int (input("请输入4为数年份："))
# res = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
# print(res)



number = int(input("请输入整数："))
print (not number % 2 !=0)

