# 注意：再开发时，应该把模块中的所有全局变量定义在所有函数上方，
# 就可以保证所有是函数都能正常的访问到每一个全局变量了。

num = 10
# 再定义一个全局变量
name = "小明"
# 再定义一个全局变量 title = “Jason”
title = "jason"


def demo():
    print("%d" % num)
    print("%s" % title)
    print("%s" % name)


demo()


