file = open("README.md")  # 定义变量file，来接收open函数返回的结果
while True:

    text = file.readline()  # 定义text变量来接收file对象调用readline方法的返回结果，readline方法在默认情况下只读取一行内容，方法执行完会把文件指针移动到下一行，准备再次读取。
    # 判断是否读取到内容
    if not text:  # 判断text有无内容。
        break  # 无内容的话用break退出循环。

    print(text)
    # print(text, end="")

file.close()


