class Animal:
    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")

    def bark(self):  # 对父类bark方法的扩展

        # 1.针对子类特有的需求，编写代码
        print("神一样的叫唤...")
        # 2. 使用 super(). 调用原本在父类中封装的方法
        super().bark()
        # 3. 增加其他子类的代码
        print("￥#^%^#^@^%")


xtq = XiaoTianQuan()

xtq.bark()  # 如果子类中重写了父类的方法，在使用子类对象调用方法时，只会调用子类中重写的方法。



