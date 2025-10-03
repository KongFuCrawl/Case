"""
    CSV模块示例


"""
#倒入csv模块
import csv

with open('test.csv', 'w') as f:
    #初始化csv文件的写入对象

    writer = csv.writer(f)
    writer.writerow(['越光宝盒', '周星驰', '1993-01-01'])