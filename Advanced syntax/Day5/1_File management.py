# """
# 文件管理：
#     1：文本文件：内容主要时字符，通常以人可读的格式保存，比如：文本文件 .txt   .html   .json  等
#     2：二进制文件：内容由文本的二进制数据构成，不能直接被人阅读，如  .jpg   .mp3  .mp4 程序可执行文件.exe等
#
#     绝对路径：
#         绝对路径是指系统的根目录开始，逐级向目标或文件夹的完整路径
#            windows 结构： C:\Users\Username\Documents\file.txt
#             Linux  结构：/home/username/Documents/file.txt
#     相对路径：
#         相对路径时相对于工作目录（即当前所在的位置）来描述文件或者文件夹的位置
#             子文件夹\file.txt
#
# 特殊符号：(1) .代表当前目录，  (2) ..上级目录（父级）,    (3)/和\
#     在linux和macOS中，路径使用正斜杠/分隔目录
#     在windows中，路径使用反斜杠\
# """


# Pathlib模块用于处理和操作文件系统路径，提供了面向对象的方式来处理文件和目录路径，比传统的os模块更加简洁，直观，强大
# 文件管理-创建，删除，重命名
from pathlib import Path
#创建文件
# Path("xiaoyi.text").touch()
# # 目录
# Path("test").mkdir(exist_ok=True)
#
# # 删除 如果不存在会报错,（文件）
# Path("xiaoyi.text").unlink()
#
# # 删除目录 如果不存在也会报错
# Path("test").rmdir()

# from pathlib import Path
#
# # 1. 删除目录或文件
# target = Path("text")
# if target.exists():
#     if target.is_dir():  # 🎯 检查是否是目录
#         target.rmdir()   # 删除空目录
#     else:
#         target.unlink()  # 删除文件
#
# # 2. 重命名（安全写法）
# source_file = Path("xiaoyi.txt")  # 🎯 修正文件名
# if source_file.exists():
#     source_file.rename("A.txt")
# else:
#     print("❌ 要重命名的文件不存在")
#
# # 3. 如果要重命名目录
# target_dir = Path("text")
# if target_dir.exists() and target_dir.is_dir():
#     target_dir.rename("B")
# else:
#     print("❌ 要重命名的目录不存在")







"""
找出当前month01 目录内所有.png结尾的图片和所有文件并打印ctime,
"""
# from pathlib import Path
# from datetime import datetime
#
# for item in Path.cwd().parent.glob('*.png'):
#     print(item)
#
# for item in Path.cwd().parent.rglob("*.txt"):
#     print(f"{item}:", datetime
#             .fromtimestamp(item.stat().st_mtime)
#             .strftime("%Y年%m月%d日 %H时%M分%S秒")
#     )








"""
文件管理-文件信息
"""
# from pathlib import Path
#
# # 1 返回当前工作目录
# print(Path.cwd()) #/home/zbc/PyCharmMiscProject/Advanced syntax/Day5
#
# # 2  拼接路径
# print(Path.cwd().joinpath("day01.png")) #/home/zbc/PyCharmMiscProject/Advanced syntax/Day5/day01.png
#
# # 3 判断存不存在 存在就是True反之就是False
# print(Path("xiaoyi.txt").exists()) #True
# print(Path("canyi.txt").exists()) #False
#
#
# # 4 判断时文件还是目录
# # 创建一个指向Demo.py的Path对象
# p = Path("Demo.py")
# print(type(p)) # <class 'pathlib._local.PosixPath'>
# print(p.name) # 文件名 Demo.py
# print(p.is_file()) # True
# print(p.is_dir()) # False
# print(p.stem) # Demo
# print(p.suffix) # .py
# print(p.suffixes) # ['.py']
#
#
#
# # os.stat_result(
# # st_mode=33204, 文件模式
# # st_ino=681040, 文件的 inode 编
# # st_dev=64513, 设备标识符
# # st_nlink=1,   连接数
# # st_uid=1000,  用户 ID
# # st_gid=1000,  组 ID
# # st_size=0,    文件大小（以字节为单位）
# # st_atime=1760067463,  最后访问时间
# # st_mtime=1760067463,  最后修改时间
# # st_ctime=1760067463)  最后状态改变时间
# print(p.stat())








#  glob() 非递归的遍历目录的文件   方法：rglob()    递归遍历所有子目录的文件
# 文件查找
from pathlib import Path

# 当前目录
# for item in Path.cwd().glob('*Demo*'):
#     print(item) #/home/zbc/PyCharmMiscProject/Advanced syntax/Day5/Demo.py
#
#
# # parent 父级目录
# for item in Path.cwd().parent.glob("*Day*"):
#     print(item)


# 递归搜索
# for item in Path.cwd().parent.rglob("*.py"):
#     print(item)















