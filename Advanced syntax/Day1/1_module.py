"""
模块：
    包含一系列数据, 函数，类的文件，通常以.py结尾

    分类：
        系统内置模块   官网提供  不用安装
        第三方模块   社区或者其他开发者  需要独立按抓
        自定义模块   开发者自己写的
"""
# 倒入模块  模块名.成员
# import sys
# import module

# print (module.str1)
# module.say()
# module.Myclass().hi()
#
# print(sys.modules)
#
# # as 起别名  别名.成员
# import module as mod
#
# mod.Myclass().hi()


# from 模块名  import  成员   成员
# from module import str1, say
# print(str1)
# say()



# from 模块名  import  成员  as  别名  别名
# from module import  Myclass as MC
# MC().hi()



# """
# 模块变量
# __name__
# 如果py 文件直接执行 __main__
# 如果是作为模块，模块名
# """
# if __name__ == "__main__":
#     print("我真帅")
#
#
# print(__name__)



"""
datetime  时间日期模块
"""
from datetime import datetime, timedelta



# 1.获取现在的日期和时间
now = datetime.now()
print(now)


#2. 创建时间和日子
custom_date = datetime(2021, 12, 30)
print(custom_date)


# 3. 获取信息
# print(sustom_date.year) # 年份
# print(sustom_date.month) # 月
# print(sustom_date.day)    # 日

# print(sustom_date.weekday())





# # 4.格式u化与解析
# print(custom_date.strftime("%Y年%m月%d日 %H时%M分%S秒"))
# print(custom_date.strftime("闰月%Y年桃"))
# date_str = "2021年9月4日 15时15分15秒"
# print(custom_date.strptime(date_str,"%Y年%m月%d日 %H时%M分%S秒"))
#
#
# # 5.计算
# deltal = now - custom_date
# print(type(deltal)) #<class 'datetime.timedelta'>
# print(deltal)
# print(deltal.days)
# print(deltal.total_seconds()) # 总秒数
#
# # 直接创建 datetime.timedelta 对象
# print(timedelta(days=2))
#
# print(timedelta(days=-2,weeks=1,hours=2) + custom_date)



from module import say,say as hi

say("礼拜")
hi("残阳")

print(say)
print(hi)












