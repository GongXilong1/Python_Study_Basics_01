import random  # 导入random模块

print(random.__file__)  # 输出random模块的内置属性__file__，可以知道当前被导入的random模块的路径。

rand = random.randint(0, 10)  # 定义变量rand，使用random模块调用randint函数，用来生成0-10的随机数

print(rand)


# 注意：python解释器会先在当前目录（工程）中找导入的模块，找到的话就不会去系统目录找了。

