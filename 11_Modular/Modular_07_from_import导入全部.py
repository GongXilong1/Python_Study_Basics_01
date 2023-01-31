from Modular_01_测试模块1 import *  # 使用from xxx import * 这种方式导入全部工具
# from Modular_02_测试模块2 import *

print(title)
say_hello()  # 调用say_hello 方法

wangcai = Dog()
print(wangcai)


# 注意：这种方式在开发中不推荐使用，因为这种方式函数重名没有任何提示，出现问题不好排查。
