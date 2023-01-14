def demo(num_list):
    print("函数内部的代码")

    # 使用方法修改列表的内容
    num_list.append(9)  # 在列表[1, 2, 3]后追加一个数字9

    print(num_list)  # 打印追加9的列表。

    print("函数执行完成")


gl_list = [1, 2, 3]  #
demo(gl_list)  # 将 gl_list 当做实参传递到demo函数内部。临时让num_list也引用列表[1, 2, 3]在内存中的地址。
print(gl_list)  # 因为 gl_list 的引用和num_list 引用的是同一个内存地址，所以 gl_list 变量中的值也会变成 [1, 2, 3, 9]打印出来。
