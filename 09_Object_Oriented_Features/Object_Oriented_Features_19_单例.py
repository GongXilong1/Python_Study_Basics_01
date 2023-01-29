class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None

    # 改造new方法
    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 如果对象没有被创建，调用父类的方法，为第一个对象分配空间。
            cls.instance = super().__new__(cls)  # 使用super这个特殊的对象调用父类new方法，new方法是静态方法，所以要把cls这个形参传递给父类的new方法。
            # 使用类属性记录父类方法 执行的返回结果。

        # 3. 返回类属性保存的对象引用
        return cls.instance


# 创建多个对象
player1 = MusicPlayer()
print(player1)  # 没使用单例时候的 输出的内存地址：<__main__.MusicPlayer object at 0x000001763FC73E20>
# <__main__.MusicPlayer object at 0x000001994A0C36D0>

player2 = MusicPlayer()
print(player2)  # 没使用单例时候的 输出的内存地址：<__main__.MusicPlayer object at 0x000001763FC738B0>
# <__main__.MusicPlayer object at 0x000001994A0C36D0>

