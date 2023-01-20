class Cat:
    def __init__(self):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = "Tom"

    def eat(self):
        print("%s 爱吃鱼" % self.name)


tom = Cat()  # 当使用类名加()创建对象的时候，会自动调用初始化方法，__init__ 。
print(tom.name)


