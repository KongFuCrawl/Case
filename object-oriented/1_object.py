"""
面向对象 组织代码的一种方式   万物皆对象
类：
    变量 + 函数组成的新的数据类型  类别  设计图

对象：
    类的具体实例 ==> 实例化类得到实例化对像   根觉设计图设计出的产品

"""



class Movie:
    # 构造函数 创建对象时自动被调用  初始化对象的属性
    # self 约定俗称的名称  代表调用该方法的对像
    def __init__(self, name, type):
        # 对象 属性 = 值
        self.name = name
        self.type = type


    def say(self):
        # 对像.属性  获取对像的属性值
        print(f"电影：{self.name}的类型是{self.type}")
# 类名() ==> 实例化 ==> 实例对象
M1 = Movie("图图", "小新")
M2 = Movie("雷震子", "锋发韵流")

# 保存的是对像的地址
print(M1) #<__main__.Movie object at 0x75a2659a8ec0>

print (M1.name, M1.type) #图图 小新

# __dict__ 是内置属性 用字典形式显示对象
print(M1.__dict__) # {'name': '图图', 'type': '小新'}

M1.say() #电影：图图的类型是小新
M2.say() # 电影：雷震子的类型是锋发韵流


