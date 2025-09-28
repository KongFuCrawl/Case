"""
单层for

for 变量列表 in 可迭代对象：
    循环体
"""
#range函数，产生一个可迭代对像，包含开始点，但不包含结束点的整数序列

# for i in range(2, 20):
#     print(i)


# for i in range(5):
#     print(i)

# for i in range(1, 10, 3):  #1+3+3
#     print(i)


# for i in range(0, 11, 2): #0 2 4 6 8 10
#     print(i)



# for i in range(-1, -6, -1): #-1 -2 -3 -4 -5
#     print(i)



# total = 0
# for i in range(1, 101):
#     if not i % 5:
#         total +=i
#         print(total)
#
#
# total = 0
# for i in range(5, 101, 5):
#     total += i
#     print(total)



"""
for循环嵌套（双层）
1.外层循环每执行1次，内层循环要从头执行n次
2.外层循环结束，整个循环才终止

"""
# for i in range(3):
#     print("外层i:", i)
#     for j in range(2):
#         print("内层j:", j)





"""
for 循环打印下列图形
"""


# for i in range(1, 6):
#     for a in range(i):
#         print("*", end='')
#     print()




# line = int(input("请输入要打印的行数："))
#
# for i in range(1, line + 1):
#     for _ in range(line - i):
#         print(" ", end="")
#
#         for _ in range(i * 2 - 1):
#             print("*", end="")
#
#     print()





# for i in range(1, 10):
#     for a in range(1, i + 1):
#         print(f"{a} * {i} = {a * i}",end="\t")
#
#     print()



for n in range(9,0,-1):
    for c in range(1,n + 1):
        print(f"{c}*{n}={c * n}", end="\t")
    print()




