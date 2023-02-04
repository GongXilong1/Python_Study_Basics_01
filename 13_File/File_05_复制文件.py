# 1. 打开文件
file_read = open("README.md")  # 定义变量file_read，来接收open函数返回的结果，即打开源文件，只读方式。
file_write = open("README[复件].md", "w")  # 定义变量file_write，来接收open函数返回的结果，即打开目标文件，只写方式。

# 2. 读取源文件，写入新文件
text = file_read.read()     # 定义text变量来接收用file_read对象调用read方法返回的结果。
file_write.write(text)  # 用file_write对象调用write方法，同时把读取到的结果text当做参数传递进来。

# 3. 关闭文件
file_read.close()  # 关闭源文件
file_write.close()  # 关闭目标文件

