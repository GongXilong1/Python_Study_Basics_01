class MusicPlayer(object):

    # 重写父类的new方法，new方法可以接收三个参数，第一个参数 cls，第二个参数 *args 表示多值的元组参数，第三个参数 **kwargs 表示多值字符数。
    def __new__(cls, *args, **kwargs):

        # 1. 创建对象时，new方法会被自动调用
        print("创建对象，分配空间")

        # 2. 为对象分配空间
        instance = super().__new__(cls)   # 使用super对象调用父类object类下的new方法，new是静态方法，所以要把cls参数传递给父类的new方法。
        # 用instance变量接收new方法的返回结果。

        # 3. 返回对象的引用
        return instance

    def __init__(self):  # 通过初始化方法定义实例属性
        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()
print(player)

