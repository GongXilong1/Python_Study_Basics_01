# *-* coding:utf8 *-*      在Python2中运行含有中文的代码需要带上这句注释。

# 引号前面的u告诉解释器这是一个utf8编码格式的字符串。目的是保证含有中文的代码在Python2中可以运行。
hello_str = u"hello世界"

# hello_str = "hello世界"

print(hello_str)

for c in hello_str:  # 遍历hello_str
    print(c)  # 输出字符c

