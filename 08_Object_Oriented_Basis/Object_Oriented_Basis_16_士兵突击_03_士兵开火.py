class Gun:

    def __init__(self, model):
        # 1. 枪的型号
        self.model = model

        # 2. 子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 1. 判断子弹数量
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了..." % self.model)
            return

        # 2. 发射子弹，数量-1
        self.bullet_count -= 1

        # 3. 提示发射信息
        print("[%s] 突突突...[%d]" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        # 1. 姓名
        self.name = name

        # 2. 枪-新兵没有枪
        self.gun = None

    def fire(self):

        # 1. 判断士兵是否有枪
        # if self.gun == None:  # ==是用来判断变量的值是否相等
        if self.gun is None:  # is用于判断两个变量引用的对象是否为同一个。（两个内存地址是否一致）
            print("[%s] 还没有枪..." % self.name)
            return

        # 2. 高喊口号
        print("冲啊...[%s]" % self.name)

        # 3. 让枪装填子弹
        self.gun.add_bullet(50)  # 让枪调用封装好的添加子弹方法

        # 4. 让枪发射子弹
        self.gun.shoot()  # # 让枪调用封装好的发射子弹方法


# 1. 创建枪对象
ak47 = Gun("AK47")

# ak47.add_bullet(50)
# ak47.shoot()

# 2.  创建许三多
xusanduo = Soldier("许三多")

xusanduo.gun = ak47
xusanduo.fire()  # 让许三多调用FIRE方法

print(xusanduo.gun)






