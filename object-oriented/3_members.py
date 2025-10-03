"""
类的成员
    实例成员  属于类的实例（对象） 通过对象调用
        实例属性  在类的 __init__构造函数中定义  对像.属性

        实例方法  在类中定义的函数， 至少有一个self形参  对象.方法


    类成员 属于类本身 ，不属于类的实例 通过类名直接访问
        类属性 在类中直接通过  变量 = 值 的定义  类名.属性
            所有的实例共享，描述对象共有的数据
            一旦修改，会影响所有代码对这个属性的访问结果
        静态方法 被 @staticmethod 装饰的方法，可以没有参数  类名.方法
        类方法(知道有就行)
"""
# class Stu:
#     # 类属性
#     class_name = "明日复明日，明日何其多，我生待明日，万事成蹉跎"
#
#     def __init__(self, name, age):
#         #实例属性
#         self.name = name
#         self.age = age
#     # 实例方法
#     def say(self):
#         print(f"我叫：{self.name}，年龄:{self.age}, 吟诗(明日)：{Stu.class_name}")
#
#     #静态方法
#     @staticmethod
#     def get_shcool_name():
#         print("天南学院")
#
# s2 = Stu("侠兰", "18")
# s3 = Stu("侠兰", "33")
# # 对象. 属性
# print(s2.name, s2.age)
# # 对象方法
# s2.say()
# print(s2.__dict__)
# print(s3.__dict__)
#
#
# # 类名.方法
# Stu.get_shcool_name()







class Article():
    id = 0

    # 只要是创建对象 __init__ 构造函数必然会调用
    def __init__(self, title, content):
        Article.id += 1
        self.id = Article.id
        self.title = title
        self.content = content

    def say(self):
        print(f"ID:{self.id}文章标题是{self.title}, 内容：{self.content}")

    @staticmethod
    def get_last_id():
        print(f"最后的ID是：{Article.id}")

a2 = Article("震惊竟然还有这种事！", "某老师在休息的时候休息")
a3 = Article("围城金句", "城里的人想出去，城外的人想进来")
a2.say()
a3.say()
a2.get_last_id()















