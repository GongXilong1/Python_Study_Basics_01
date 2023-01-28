class A:
    def test(self):
        print("test 方法")


class B:
    def demo(self):
        print("demo 方法")


class C(A, B):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass


# 创建子类对象
c = C()

c.test()  # 子类c对象调用A类中的test方法
c.demo()  # 子类c对象调用B类中的demo方法

