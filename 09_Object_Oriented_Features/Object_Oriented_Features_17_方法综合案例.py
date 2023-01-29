class Game(object):  # 写上Game类继承自object基类，防止在Python2.0环境下报错。
    # 历史最高分
    top_score = 0  # 使用赋值语句定义类属性

    def __init__(self, player_name):  # 通过初始化方法定义实例属性，用实例属性记录玩家姓名，给初始化方法指定player_name的形参。
        self.player_name = player_name  # 在初始化内部 使用self.定义 player_name 属性，并且把形参player_name传递给属性。
        # self.player_name 是定义player_name 属性。     = player_name 是把形参player_name传递给属性。

    @staticmethod
    def show_help():  # 定义 show_help()这个静态方法
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):  # 定义 show_top_score这个类方法
        print("历史记录 %d 分" % cls.top_score)  # 在类方法内部要访问类属性可直接使用参数cls 调用类属性的值。

    def start_game(self):  # 定义 start_game这个实例方法，让self作为这个方法的参数。
        print("%s 开始游戏啦" % self.player_name)


# 1. 查看游戏的帮助信息
Game.show_help()  # 用 类名.的方式调用类的静态方法

# 2. 查看历史最高分
Game.show_top_score()  # 用 类名.的方式调用类方法，默认第一个参数是cls ，但不用写出来传递。

# 3. 创建游戏对象
game = Game("小明")  # 使用Game类 创建game对象，指定玩家名字：小明
game.start_game()  # 让 game对象 调用 start_game()实例方法。



