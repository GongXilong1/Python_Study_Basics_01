class HouseItem:

    def __init__(self, name, area):
        self.name = name  # self.属性 = 形参
        self.area = area  # 等号右侧name是形参，等号左侧name是属性

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area  # 剩余面积的初始值就是总面积，不需要外部传递

        # 家具名称列表
        self.item_list = []  # 家具名称列表的初始值是空列表，不需要外部传递

    def __str__(self):
        # Python 能够自动的将一对括号内部的代码连接在一起
        return ("户型：%s\n总面积：%.2f[剩余面积：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):

        print("要添加 %s" % item)


# 1. 创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print(bed)
print(chest)
print(table)

# 2. 创建房子对象
my_home = House("两室一厅", 80)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)


