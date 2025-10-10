"""
异常处理:
    真实的处理可预知的异常

"""
#最简单的异常处理
# try:
#     age = int(input("请输入年龄："))
# except:
#     print(f"\033[31m 风 请输入数字]")
#     age = 19
#



#根据不同的异常类型来有不同的处理方法
# 名称 NameError
# 类型 TypeError
# 索引 IndexError
# 键 KeyError
# 值 ValueError
# 属性 AttributeError
# 异常基类 Exception


# try:
#     age = int(input("请输入年龄:"))
# except ValueError:
#
#     print(f"\033[31m 小可爱！ 请输入数字！]")
#     age = 18
# except NameError:
#     pass
# except TypeError:
#     pass
# else:
#     print("无异常 收队！")
# finally:
#     print("清除缓存 临时垃圾 ")







def apple(apple_count):
    try:
        person_count = int(input("请输入人数:"))

        # 人数小于0 直接抛出异常
        if person_count < 0:
            # raise 显示的抛出异常
            raise ValueError

        res = apple_count / person_count
        print(res)

    except ValueError:
        print("必须时整数且大于0")
    except ZeroDivisionError:
        print ("人不能为0")
    except TypeError:
        print("请检查参数类型")


apple(10)
apple("20")



































