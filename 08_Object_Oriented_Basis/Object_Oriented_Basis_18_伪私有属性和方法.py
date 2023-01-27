class Women:  # 创建 Women 类
    def __init__(self, name):  # 在初始化方法中增加name的形参
        self.name = name  # 定义name的属性
        self.__age = 18  # 定义私有的 age属性

    def __secret(self):  # 定义私有的 秘密方法
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")  # 创建变量xiaofang，用Women类指定小芳的名字

print(xiaofang._Women__age)  # 私有属性，在外界不能够被直接访问，需要加_类名__名称

xiaofang._Women__secret()  # 私有方法，同样不允许在外界直接访问，需要加_类名__名称


