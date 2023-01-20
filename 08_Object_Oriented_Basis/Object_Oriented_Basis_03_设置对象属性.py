class Cat:  # 定义 Cat 类

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用。这个self就是tom这个变量指向的cat对象；cat对象调用的方法，self就是cat对象的引用。
        # tom这个cat对象调用了eat方法。
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 爱喝水" % self.name)


# 创建猫对象
tom = Cat()  # 创建Cat对象，使用 tom 这个变量接收Cat这个对象，也就是tom变量对Cat对象进行引用。

# 可以使用 . 属性名  利用赋值语句就可以了
tom.name = "Tom"  # 给tom 这个对象加name属性

tom.eat()  # 让 tom 这个变量调用 eat 这个方法
tom.drink()  # 让 tom 这个变量调用 drink 这个方法
print(tom)  # <__main__.Cat object at 0x000002293BEF38E0>  tom变量 Cat对象在内存中的地址

# 再创建一个猫对象
lazy_cat = Cat()

lazy_cat.name = "大懒猫"  # 给lazy_cat这个对象加name属性

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)  # <__main__.Cat object at 0x000002293BEF38E0>  lazy_cat变量  Cat对象在内存中的地址

lazy_cat2 = lazy_cat
print(lazy_cat2)


