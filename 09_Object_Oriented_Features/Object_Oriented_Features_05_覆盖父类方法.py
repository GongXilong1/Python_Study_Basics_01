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

    def bark(self):  # 在子类中重写编写父类的方法。
        print("叫得跟神一样")


xtq = XiaoTianQuan()

xtq.bark()  # 如果子类中重写了父类的方法，在使用子类对象调用方法时，只会调用子类中重写的方法。
