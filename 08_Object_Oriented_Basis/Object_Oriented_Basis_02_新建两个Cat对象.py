class Cat:  # 定义 Cat 类

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


# 创建猫对象
tom = Cat()  # 创建Cat对象，使用 tom 这个变量接收Cat这个对象

tom.eat()  # 让 tom 这个变量调用 eat 这个方法
tom.drink()  # 让 tom 这个变量调用 drink 这个方法
print(tom)  # <__main__.Cat object at 0x000002293BEF38E0>  tom变量 Cat对象在内存中的地址

# 再创建一个猫对象
lazy_cat = Cat()

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)  # <__main__.Cat object at 0x000002293BEF38E0>  lazy_cat变量  Cat对象在内存中的地址

lazy_cat2 = lazy_cat
print(lazy_cat2)


