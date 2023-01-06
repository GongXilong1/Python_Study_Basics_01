# 定义（封装）函数  函数名：multiple_table
def multiple_table():

    # 1.打印九行小星星
    row = 1

    while row <= 9:

        col = 1
        while col <= row:
            # print("*", end="")
            print("%d * %d = %d" % (row, col, row * col), end="\t")
            # 1. \t 在控制台输出一个 制表符，协助在输出文本时 垂直方向 保持对齐

            col += 1

        # print("%d" % row)
        print("")

        row += 1



