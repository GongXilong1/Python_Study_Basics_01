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


# 创建一个哮天犬的对象
xtq = XiaoTianQuan()

xtq.fly()  # xtq调用XiaoTianQuan类中fly的方法
xtq.bark()  # xtq调用Dog类中bark的方法
xtq.eat()  # xtq调用Animal类中eat的方法
