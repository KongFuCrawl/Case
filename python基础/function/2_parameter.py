"""
形参定义方式 parameter

"""
from inspect import cleandoc

# 1：默认值形参，函数的形参拥有默认值且必须自右至左依次存在
# def func1(p1, p2=2, p3=3):
#     print(p1)
#     print(p2)
#     print(p3)
#
# func1(1) #1 2 3
# func1(11, 22, 33) # 11  22  33
#
# # 同时支持位置实参与关键字实参
# func1 (111, p2=222) #111  222  3
#
# # 先位置，后关键字
# # func1(p2=222, 111) # 报错





"""
可变数量的位置参数（*号元组形参）
    可以将多个实参合并成一个元组
        一般的形参名称 "args" 且形参列表中最多存在1个
"""
# def func1(*args):
#     print(args)
#
# func1 (1, 2, 3, 5) #(1, 2, 3, 5)
# func1 () #() 空元组





"""
可变数量的关键字参数{**字典形参}
    可以将多个实参合并成一个字典
        一般的形参名称是 "kwargs" 且形参列表中最多存在1个
"""
# def func1(**kwargs):
#     print(kwargs)
#
# func1(name="xiaoyi", age=18) #{'name': 'xiaoyi', 'age': 18}




"""
 综合练习
    定义一个函数，根据小时，分钟 秒钟计算秒数 小时 分钟 秒钟 可同时存在或单独存在
"""

# def calc_sec(hour=0, min=0, sec=0):
#     total = 0
#     total +=hour * 60 * 60
#     total +=min * 60
#     total +=sec
#     print(total)
#
# calc_sec(6, 2, 3) #21723
# calc_sec(6) #21600
# calc_sec(min=2) #120






"""
定义一个函数接受一个字符串作为参数，判断是不是回文字符串（忽略大小写和非字母数字字符）
"""
# def is_palindrome(d):
#     cleandoc_s = "".join(char.lower() for char in d if char.isalnum())
#     length = len(cleandoc_s)
#     for i in range(length // 2):
#         if cleandoc_s[i] != cleandoc_s[length - i -1 ]:
#             return False
#     return  True
#
# print(is_palindrome("A man, a plan, a canal: Panama")) #True





"""
定义一个函数，计算所有位置参数的和以及所有的关键自参数值的乘和
"""

# def sum_and_product(*args, **kwargs):
#     arg_sum = sum(args)
#     kwargs_product = 1
#     for key, value in kwargs.items():
#         kwargs_product *= value
#     return arg_sum, kwargs_product
#
# print(sum_and_product(1, 2, 3, a=7, b=3, c=4)) #(6, 84)







"""
老师开了一家图书馆，图书管理系统V2
运行文件之后 显示菜单
    1.添加图书信息
    2.显示图书信息
    3.删除图书信息
    4.修改图书信息
    5.退出图书管理系统
    
选择菜单（1 2 3 4 5 ）执行相关操作
    按1键添加图书信息
        （图书名称 ， 作者， 价格）
    按2键显示图书信息
        （显示所有内容，平乐园的作者是渡边淳一，价格为95）
    按3键删除图书信息
        (根据图书名称删除)
    按4键修改图书信息
        （根据图书名称修改，可以修改图书名称，价格）
    按5键退出图书管理系统
"""
list_book = []

# 1.显示菜单
def display_menu():
    print("按1键添加图书信息")
    print("按2键显示图书信息")
    print("按3键删除图书信息")
    print("按4键修改图书信息")
    print("按5键退出图书管理系统")


# 添加图书
def add_book():
    dict_book = {
        "name": input("请输入书籍名称:"),
        "author": input("请输入书籍作者:"),
        "price": input("请输入书籍价格:")
    }
    list_book.append(dict_book)
    print(list_book)


# 显示图书
def display_book():
    for item in list_book:
        print(f"{item['name']}的作者{item['author']}, 价格为: {item['price']}元")




# 删除图书
def del_book():
    name = input("请输入删除的书籍名称:")
    for i in range(len(list_book)):
        if list_book[i]['name'] == name:
            del list_book[i]
            break
        else:
            print("书籍不存在")


# 修改图书
def modify_book():
    name = input("请输入修改的书籍名称:")
    for item in list_book:
        if item['name'] == name:
            item['name'] = input("请输入修改后的名称:")
            item['price'] = float(input("请输入修改后的价格:"))
        else:
            print("书籍不存在")


# 主程序
def main():
    while True:
        display_menu()
        number = input("请输入对应的服务数字：")
        if number == "1":
            add_book()
        elif number == "2":
            display_book()
        elif number == "3":
            del_book()
        elif number == "4":
            modify_book()
        elif number == "5":
            print("Bye~")
            break
        else:
            print("启动爆炸模式")

main()



















