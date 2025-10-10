"""
迭代器  组织代码的一种方式  统一数据结构的迭代方式
迭代：每一次对过程的重复称为一次迭代,而且每一次迭代的结果作为下一次迭代的初始值

迭代器时一个实现了迭代协议的对象，可以在循环中逐个返回值
    迭代协议（包含2个要求）:
        实现 __iter__函数的对象（类里有__iter___函数），实现具体的迭代逻辑 （其实代码就一句话 return 迭代器对象）
        实现 __next__函数的对象(类里有__next__函数)，返回下一个元素，没有元素就可以返回，抛出StopIteration异常

"""
msg = 'hello'
list1 = [1, 2, 3]
list2 = [1, 2, 3]

# 原：自动调用 __iter__ 和 __next__ 和处理异常
for item in msg:
    print(item)




# 迭代器思想
# 1.获取迭代器对象
iterator = msg.__iter__()
print(iterator) #<str_ascii_iterator object at 0x79cd98ea6920>

# 2.获取下一个元素+处理异常
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
