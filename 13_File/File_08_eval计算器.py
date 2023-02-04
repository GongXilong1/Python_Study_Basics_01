# input_str = input("请输入算术题：")  # 定义input_str 接收用户输入的内容

# print(eval(input_str))  # 在print函数内部调用eval函数，并且把用户输入的字符串input_str，传递给eval。

# eval("print('asfsF')")  # eval函数内部可以执行一切命令或代码行

"""在开发时千万不要使用eval直接转换input的结果，原因：如果用户通过os这个模块来调用system方法，可以执行任何终端命令。演示如下："""


"""运行结果1："""
# 请输入算术题：__import__('os').system('dir')
#  Volume in drive D is D
#  Volume Serial Number is 5E84-D438
#
#  Directory of D:\Users\Administrator\PycharmProjects\13_File
#
# 2023/02/01  19:51    <DIR>          .
# 2023/02/01  19:51    <DIR>          ..
# 2023/02/01  19:51    <DIR>          .idea
# 2023/01/31  17:39               478 File_01_读取文件.py
# 2023/01/31  19:52               853 File_02_读取文件后文件指针会改变.py
# 2023/01/31  20:22               664 File_03_写入文件.py
# 2023/02/01  09:49               539 File_04_分行读取文件.py
# 2023/02/01  13:58               680 File_05_复制文件.py
# 2023/02/01  14:13               845 File_06_复制大文件.py
# 2023/02/01  17:08               394 File_07_Python2字符串.py
# 2023/02/01  19:51               223 File_08_eval计算器.py
# 2023/01/31  17:13               544 main.py
# 2023/02/01  13:50                27 README.md
# 2023/02/01  13:49                26 README[复件]
# 2023/02/01  14:12                27 README[复件].md
# 2023/01/31  17:13    <DIR>          venv
#               12 File(s)          5,300 bytes
#                4 Dir(s)  17,739,988,992 bytes free
# 0
#
# Process finished with exit code 0


"""运行结果2：目的是新建 aaa.txt 文件"""
# 请输入算术题：__import__('os').system('type nul>aaa.txt')
# 0
#
# Process finished with exit code 0


"""运行结果3：目的是删除 a.txt 文件"""
# 请输入算术题：__import__('os').system('del a.txt')
# 0
#
# Process finished with exit code 0


