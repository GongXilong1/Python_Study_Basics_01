def demo(num, num_list):
    print("函数开始")

    num += num  # num = num + num

    # num_list = num_list + num_list

    # 列表变量使用 += 不会做相加再赋值的操作，本质上是在调用列表的 extend 方法
    num_list += num_list
    # num_list.extend(num_list)  # num_list 参数调用 extend 方法，同时将等号右侧的 num_list 以参数的形式传递给 extend 方法。

    print(num)
    print(num_list)
    print("函数完成")


gl_num = 9  # 定义全局变量 gl_num 并且设置初始值9
gl_list = [1, 2, 3]  # 定义全局变量 gl_list
demo(gl_num, gl_list)  # 调用demo函数，将 gl_num 和 gl_list 全局变量当做实参传入demo函数中
print(gl_num)
print(gl_list)



