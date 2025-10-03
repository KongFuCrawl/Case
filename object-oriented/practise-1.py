"""
观察淘宝首页商品， 使用面向对象的思想来表示 商品这类事物
属性不低于3个 创建2个商品对像 介绍商品方法
"""

class Prd:
    def __init__(self, type,title,price):
        self.type = type
        self.title = title
        self.price = price

    def say(self):
        print(f"商品：{self.type}{self.title}价格为{self.price}")

    def getSource(self,source):
        print(f"商品来源：{source}")

p1 = Prd("苹果手机", "网络延迟", 5)
p2 = Prd("三星手机", "神迹", 5)

p1.say()
p2.say()
p2.getSource("首页推荐")
