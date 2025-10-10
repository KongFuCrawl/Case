"""
定义一个函数，接受年月日计算星期几，返回中文

"""
from datetime import datetime

def calc_weekday(year, month, day):
    date = datetime(year, month, day)

    weeks = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六")
    # return weeks[date.weekday()]

    return date.strftime("%A")

print(calc_weekday(2025, 10, 6))




