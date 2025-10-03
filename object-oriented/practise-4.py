"""
创建一个银行账户类  账户， 持卡人，余额
利率是所有账户 共有 0.05
存款 取款  获取余额的实例方法
计算利息的静态方法
用面向对像思想完成

"""
class Bank:
      rate = 0.05

      def __init__(self, acc, hodler, balance=0):
          self.acc = acc
          self.hodler = hodler
          self.balance = balance

      def deposit(self, money):
          if money > 0:
             self.balance += money
             print("存款成功",self.get_balance())

          else:
              print("金额错误")

      def withdraw(self, money):
          if 0 < money < self.balance:
             self.balance -= money
             print("取款成功",self.get_balance())
          else:
              print("余额不足")

      def get_balance(self):
          return self.balance

      @staticmethod
      def cacl_interest(balance):
          return Bank.rate * balance

acc1 = Bank(1000000, "赵总")
acc1.deposit(1000000000)
acc1.withdraw(10000)
print(Bank.cacl_interest(acc1.get_balance()))


