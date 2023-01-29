class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None

    # 记录是否执行过初始化动作
    init_flag = False  # 定义 init_flag 这个类属性，设置初始值：False，表示最开始还没有执行过初始化动作。

    # 改造new方法
    def __new__(cls, *args, **kwargs):
        # 1. 判断类属性是否是空对象
        if cls.instance is None:
            # 2. 如果对象没有被创建，调用父类的方法，为第一个对象分配空间。
            cls.instance = super().__new__(cls)  # 使用super这个特殊的对象调用父类new方法，new方法是静态方法，所以要把cls这个形参传递给父类的new方法。
            # 使用类属性记录父类方法 执行的返回结果。

        # 3. 返回类属性保存的对象引用
        return cls.instance

    # 改造初始化方法
    def __init__(self):

        # 1. 判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return
        # 2. 如果没有执行过，再执行初始化动作
        print("初始化播放器")
        # 3. 修改类属性的标记
        MusicPlayer.init_flag = True


# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)




