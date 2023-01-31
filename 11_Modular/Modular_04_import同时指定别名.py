import Modular_01_测试模块1 as DogModule  # 给模块1指定别名为：DogModule，别名的命名规则符合大驼峰命名法。
import Modular_02_测试模块2 as CatModule  # 给模块2指定别名为：CatModule

DogModule.say_hello()  # 使用别名DogModule调用say_hello()方法
CatModule.say_hello()  # 使用别名CatModule调用say_hello()方法

dog = DogModule.Dog()  # 使用DogModule中的Dog类创建一个dog对象
print(dog)

cat = CatModule.Cat()  # 使用CatModule中的Cat类创建一个cat对象
print(cat)


