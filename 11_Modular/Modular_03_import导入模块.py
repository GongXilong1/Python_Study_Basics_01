import Modular_01_测试模块1  # 导入模块1
import Modular_02_测试模块2  # 导入模块2

Modular_01_测试模块1.say_hello()  # 调用模块1中say_hello方法
Modular_02_测试模块2.say_hello()  # 调用模块2中say_hello方法

dog = Modular_01_测试模块1.Dog()  # 使用模块1中的Dog类创建一个dog对象
print(dog)  # 输出dog对象 --执行后的结果：<Modular_01_测试模块1.Dog object at 0x000002342EB63B50>

cat = Modular_02_测试模块2.Cat()  # 使用模块2中的Cat类创建一个cat对象
print(cat)  # 输出cat对象
