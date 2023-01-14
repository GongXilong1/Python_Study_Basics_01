
gl_num = 10
# 再定义一个全局变量
gl_name = "小明"
# 再定义一个全局变量 title = “Jason”
gl_title = "jason"


def demo():

    # 如果局部变量的名字和全局变量的名字相同，pycharm 会在局部变量下方显示一个灰色的虚线。
    num = 99
    print("%d" % num)
    print("%s" % gl_title)
    print("%s" % gl_name)


demo()


