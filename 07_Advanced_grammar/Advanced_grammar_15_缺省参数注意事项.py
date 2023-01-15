def print_info(name, title="", gender=True):  # gender=Ture 指定缺省参数的默认值
    """

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: Ture 表示男生  False 表示女生。
    """
    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("[%s]%s 是 %s" % (title, name, gender_text))


# 假设班上的同学，男生居多！
# 提示：在指定缺省出参数的默认值时，应该使用最常见的值作为默认值！
print_info("小明")
print_info("老王")
print_info("小美", gender=False)
# 在调用具有多个缺省值的函数时，如果想要给某一个具体地缺省参数传递数据，
# 就可以先写出参数的名字，然后跟上一个等号，再跟上要传递的实参。



