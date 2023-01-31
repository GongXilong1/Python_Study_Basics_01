# from Modular_01_测试模块1 import say_hello  # 从模块1中导入say_hello函数
from Modular_02_测试模块2 import say_hello as module2_say_hello  # 从模块2中导入say_hello函数，并设置别名：module2_say_hello
from Modular_01_测试模块1 import say_hello

say_hello()  # 调用say_hello函数
module2_say_hello()  # 通过别名module2_say_hello调用say_hello函数


# 注意：如果被导入的两个模块存在同名函数，那么后导入模块的函数会覆盖掉先导入的函数。


