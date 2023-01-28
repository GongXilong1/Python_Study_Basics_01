class A:
    def test(self):
        print("A --- test 方法")

    def demo(self):
        print("A --- demo 方法")


class B:
    def demo(self):
        print("B --- demo 方法")

    def test(self):
        print("B --- test 方法")


class C(B, A):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass


# 创建子类对象
c = C()

c.test()  # 子类c对象调用A或B类中的test方法
c.demo()  # 子类c对象调用A或B类中的demo方法  运行结果：

# 确定C类对象确定方法的顺序
print(C.__mro__)


