class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    @classmethod  # 使用类方法都要写这个前提。
    def show_tool_count(cls):  # 定义类方法
        print("工具对象的数量 %d" % cls.count)

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")

# 调用类方法
Tool.show_tool_count()  # python 解释器会自动传递cls方法，所以括号内不需要写。



