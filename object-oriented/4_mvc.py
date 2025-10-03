"""
MVC  组织代码的一种方式  软件架构模式

分层  每层个尽其职

M层 模型层 Model 负责数据模型
V层 视图层 View  负责显示数据和界面
C层  控制器 Controller 负责业务逻辑

"""



# M层
class MovieModel:
  def __init__(self, name, year):
    self.name = name
    self.year = year

# V层
class MovieView:
    def __init__(self):
        self.controller = MovieController()

    def input_movie(self):
        name = input("输入电影名称")
        year = input("输入电影年份")

        movie_obj = MovieModel(name, year)
        print(movie_obj.__dict__)
        self.controller.add_movie(movie_obj)


# C层 业务逻辑
class MovieController:
    def __init__(self):
        self.list_movie = []

        #添加
    def add_movie(self, movie_obj):
        self.list_movie.append(movie_obj)
        print(self.list_movie)

view = MovieView()
controller = MovieController()
while True:
    view.input_movie()
    print(view.__dict__)
    print(view.__dict__['controller'].__dict__)
    print(view.__dict__['controller'].__dict__['list_movie'][0].__dict__)


# view对象的构成
#     view_dict = {
#         'controller':{
#             'list_movie':{
#                 'name': '1', 'year': '1',
#             }
#         }
#     }










