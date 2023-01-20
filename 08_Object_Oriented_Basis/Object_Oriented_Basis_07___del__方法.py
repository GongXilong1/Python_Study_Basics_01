class Cat:

    def __init__(self, new_name):
        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):

        print("%s 我去了" % self.name)


tom = Cat("Tom")  # tom是一个全局变量
print(tom.name)

del tom  # del关键字可以删除一个对象

print("-" * 50)