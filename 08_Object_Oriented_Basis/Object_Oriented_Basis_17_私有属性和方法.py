class Women:  # 创建 Women 类
    def __init__(self, name):  # 在初始化方法中增加name的形参
        self.name = name  # 定义name的属性
        self.__age = 18  # 定义age的私有属性

    def __secret(self):  # 定义 私有秘密方法
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")  # 创建变量xiaofang，用Women类指定小芳的名字

# print(xiaofang.age)
# print(xiaofang.__age)  # 私有属性，在外界不能够被直接访问

# xiaofang.secret()  # 让变量xiaofang 调用 秘密的方法
# xiaofang.__secret()  # 私有方法，同样不允许在外界直接访问
