"""
2个类方式实现（仅限案例）
"""



# 实现迭代器
class MovieIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __next__(self):
        if self.index < len(self.data) - 1:
            self.index += 1
            return self.data[self.index]
        raise StopIteration

class MovieIterable:
    def __init__(self, lst_movie):  # 修正：应该是 __init__ 不是 init
        self.lst_movie = lst_movie

    def __iter__(self):
        return MovieIterator(self.lst_movie)

# 创建实例
movie = MovieIterable(["749", "1916", "1997"])

# 正确的遍历方式
# 方法1：使用 for 循环（推荐）
for item in movie:
    print(item)

# 方法2：手动使用迭代器
print("\n手动迭代：")
iterator_obj = iter(movie)
while True:
    try:
        item = next(iterator_obj)  # 修正：使用 next() 函数
        print(item)
    except StopIteration:
        break


