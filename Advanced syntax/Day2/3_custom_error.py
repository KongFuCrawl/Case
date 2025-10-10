"""
自定义异常
"""
class AgeOutOfRange(Exception):
    def __init__(self, age):
        super().__init__(f"年龄{age}不再有效范围")
        self.age = age
# print(age)
# 要求年龄大于0
def check_age(age):
    if age <= 0:
        raise AgeOutOfRange(age)

    else:
        print("age:", age)

try:
    check_age(-5)
except AgeOutOfRange as e:
    print(e)

