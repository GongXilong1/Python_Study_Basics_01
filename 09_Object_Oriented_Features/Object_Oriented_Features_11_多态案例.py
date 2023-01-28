class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianDog(Dog):
    def game(self):  # 重新定义父类中的方法
        print("%s 飞到天上去玩耍..." % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


# 1. 创建一个狗对象
# wangcai = Dog("旺财")  # 使用Dog类创建wangcai对象，调用父类中的game方法。
wangcai = XiaoTianDog("飞天旺财")  # 使用XiaoTianDog类（Dog类的子类）创建wangcai对象，调用子类中的game_with_dog的方法。

# 2. 创建一个小明对象
xiaoming = Person("小明")

# 3. 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)


