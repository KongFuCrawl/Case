"""
创建一个学生类  姓名  年龄  成绩 (字典  默认为空， 不需要传参)

函数：添加学科成绩
函数：计算平均分

"""
import self


class Stu:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = {}

    def add(self, subject, score):
        if score >=0:
            self.score[subject] = score
            return "添加成功"
        else:
            return "添加失败"

    def calc_avg(self):
        if not self.score:
            return 0
        else:
            # 学科的总分 / 学科数量
         return sum(self.score.values()) / len(self.score)

stu1 = Stu("ls",20)
stu1.add("语文",100)
stu1.add("数学",100)
print(stu1.calc_avg())

















