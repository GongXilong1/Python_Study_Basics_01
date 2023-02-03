# 1. 打开文件
file = open("README.md")  # 定义变量file，来接收open函数返回的结果，open函数第一个参数是要打开的文件名，注意：文件名是区分大小写的。

# 2. 读取文件内容
text = file.read()  # 定义text变量来接收file对象调用read方法的返回结果，read方法在默认情况下会返回文件的所有内容。
print(text)
print(len(text))  # 输出读取内容的长度

print("-" * 50)

text = file.read()  # 定义text变量来接收file对象调用read方法的返回结果，read方法在默认情况下会返回文件的所有内容。
print(text)
print(len(text))  # 输出读取内容的长度

# 3. 关闭文件
file.close()  # 用file对象调用关闭文件的方法



# read 方法执行之后，会把文件指针移动到读取内容的末尾。




