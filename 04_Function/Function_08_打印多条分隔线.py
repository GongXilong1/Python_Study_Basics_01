def print_line(char, times):  # 定义两个形参
    """打印单行分隔线
    :param char:分隔字符
    :param times: 重复次数
    """
    print(char * times)


def print_lines(char, times):  # 定义两个形参
    """打印多行分隔线

    :param char:分隔线使用的分隔字符
    :param times:分隔线重复的次数
    """
    row = 0

    while row < 5:
        print_line(char, times)  # 调用之前写好的print_line()函数

        row += 1


print_lines("-", 20)  # 传入实参

