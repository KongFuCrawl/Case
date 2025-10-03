"""
使用面向对象思想完成
创建银行账户类  账户  余额  2个属性
存入  取出  2个函数
"""

class Bank:
    def __init__(self, acc, balance):
        self.acc = acc
        self.balance = balance

    def deposit(self, money):
        if money >= 1:
            self.balance += money

    def withdraw(self, money):
        if money>self.balance:
            print("余额不足")
        elif 0 < money <= self.balance:


            self.balance -= money


        print(self.balance)

acc1 = Bank(100, 100)
acc2 = Bank(100, 100)
acc1.deposit(100)
print(acc1.__dict__)





