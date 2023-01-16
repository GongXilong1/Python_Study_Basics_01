class Cat:  # 定义 Cat 类

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


# 创建猫对象
tom = Cat()  # 创建Cat对象，使用 tom 这个变量接收Cat这个对象

tom.eat()  # 让 tom 这个变量调用 eat 这个方法
tom.drink()  # 让 tom 这个变量调用 drink 这个方法

print(tom)  # <__main__.Cat object at 0x000002293BEF38E0>  Cat对象在内存中的地址

addr = id(tom)  # 用addr这个变量接收id这个函数，同时把tom这个变量传递给id这个函数
print("%d" % addr)  # %d 的打印结果：2270929500384，是以十进制的整数打印数字。
print("%x" % addr)  # %x 的打印结果：1a0ca933b50，以十六进制打印数字。

