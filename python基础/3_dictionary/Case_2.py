"""
老师开了一家图书馆，图书管理系统V1
运行文件之后 显示菜单
1. 添加图书信息
2. 显示图书信息
3. 删除图书信息
4. 修改图书信息
5. 退出图书管理系统
选择菜单(1 2 3 4 5) 执行相关操作
按1键添加图书信息
（图书名称、作者、价格）
按2键显示图书信息
（显示所有内容，平乐园的作者是渡边淳一，价格为85元）
按3键删除图书信息
（根据图书名称删除）
按4键修改图书信息
（根据图书名称修改，可以修改图书名称、价格）
按5键退出图书管理系统
"""
from openpyxl.comments import author

list_book = []
while True:
    # 显示菜单
    print("按1键添加图书信息")
    print("按2键显示图书信息")
    print("按3键删除图书信息")
    print("按4键修改图书信息")
    print("按5键退出图书管理系统")

    # 2.选择菜单
    number = input("请输入对应的服务数字:")
    if number == "1":
        dict_book = {
            "name": input("请输入书籍名称："),
            "author": input("请输入书籍作者："),
            "price": input("请输入书籍价格：")
        }
        list_book.append(dict_book)
        print(list_book)

    elif number == "2":
        for item in list_book:
            print(f"{item['name']}的作者是{item[author]}, 价格为:{item['price']}元")
        pass
    elif number == "3":
        name = input("请输入删除的书籍名称：")
        for i in range(len(list_book)):
            if list_book[i] ['name'] == name:
                del list_book[i]
                break
            else:
                print("书籍不存在")

    elif number == "4":
        name = input("请输入修改的书籍名称：")
        for item in list_book:
            if item['name'] == name:
                item['name'] = input("请输入修改后的名称：")
                item['price'] = float(input("请输入修改后的价格："))

            else:
                print("书籍不存在")

        pass
    elif number == "5":
        print("Bye~")
        break
    else:
        print("启动爆炸模式")

