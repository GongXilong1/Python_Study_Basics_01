# 注意：open函数默认是以只读方式打开文件，只读方式就不允许写入。

# 1. 打开文件
# file = open("README.md", "w")  # 给open这个函数传递一个w参数。w参数会覆盖文件内容，从头开始写入。w是write的简写。
file = open("README.md", "a")   # 给open这个函数传递一个a参数。a是append的简写，追加的意思。a参数会在已有的内容后面追加。


# 2. 写入文件
file.write("123 hello")  # 使用write方法，把需要写入的内容当做参数传递给write方法。

# 3. 关闭
file.close()



# Hello Python！
# Hello World！
# 我是Jason！
# hello hello！