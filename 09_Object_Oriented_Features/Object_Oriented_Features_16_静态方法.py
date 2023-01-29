class Dog(object):
    @staticmethod
    def run():
        # 如果这个方法不访问实例属性，不访问类属性，此时就可以把这个方法定义成静态方法。
        print("小狗要跑...")


# 通过类名.调用静态方法
Dog.run()  # 不用创建Dog的对象，使用类名.静态方法 的方式调用




