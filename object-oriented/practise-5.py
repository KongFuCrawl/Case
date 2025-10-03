
import sys
# M层
class PrdModel:
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price
    def __str__(self):
        return f'{self.id} 的作者是{self.title}, 价格 {self.price}'

# V层
class BookModel:
    pass


class PrdView:
    def __init__(self):
        self.controller = PrdController()

    def run(self):
        while True:
            self.__display_menu()
            self.__select_menu()
    def __display_menu(self):
        print("按1键添加图书信息")

    def __select_menu(self):
        print("按1键添加商品信息")
        print("按2键显示商品信息")
        print("按3键修改商品信息")
        print("按4键删除商品信息")
        print("按5键退出管理系统")

    # 选择菜单
    def __select_menu(self):  #
        number = input("请输入服务数字:")
        if number == "1":
            self.input_book()
        elif number == "2":
            self.__display_book()
        elif number == "3":
            self.__del_book()
        elif number == "4":
            self.__modify_book
        elif number == "5":
            print("Bye~")

            # 从当前的运行程序中退出
            sys.exit()


        else:
            print("你闲的蛋滕?")

    #  添加
    def _input_book(self):
        id = input("请输入商品ID")
        title = input("请输入商品标题")
        price = input("请输入商品价格")
        model = BookModel(id, title, price)
        self.controller.add(model)

        if not id or not title or not price:
            print("内容不能为空，请重新输入！")
            return

        if price.isdigit() or price.replace(".", "",1).isdigit():
            price = float(price)
        else:
            print("价格必须是数字，请重新输入")
            return

        # 创建商品对象
        prd_obj = PrdModel(id, title, price)
        if self.controller.add_prd(prd_obj):
            print("添加成功")
        else:
            print("添加失败")

        # 显示
        def display_prd():
            if not self.controller.list_prd:
                print("暂无商品信息～")
                return
        for item in self.controller.list_prd:
            print(f"ID: {item.id}标题: {item.title}, 价格: {item.price}")



# C层
class PrdController:
    def __init__(self):
        self.list_prd = []

    def add_prd(self,prd_obj):
        self.list_prd.append(prd_obj)
        print (self.list_prd)

        return True


# 主入口
def main():
    view = PrdView()
    view.run()


# 添加程序入口
if __name__ == "__main__":
    main() # 梦开始的地方


