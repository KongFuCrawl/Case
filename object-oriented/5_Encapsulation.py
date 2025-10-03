"""
面向对象的三大特性：
    封装：通过私有属性或者私有方法对外隐藏内部实现的细节
        外部只能通过指定的方法来操作对象,无法直接修改和访问
            通过双下划线实现 __属性  __方法
    继承


    多态

"""

class Movie:

    def __init__(self, name, type):

        #公开的
        self.name = name
        #私有的
        self.__type = type

    def __say(self):
        print(f"电影：{self.name}的类型是{self.__type}")

        # 公开的方法
    def gerValue(self):
        return self.__type

m1 = Movie("图图", "小新")

# print(m1.name, m1.__type) #报错

# Name Mangling  机制 _类名__属性 强制访问
print(m1._Movie__type)
m1.gerValue()
print(m1.gerValue())







