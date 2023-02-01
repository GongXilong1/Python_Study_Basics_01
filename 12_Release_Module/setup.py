from distutils.core import setup  # 从distutils.core中导入setup函数

# 调用setup函数
setup(name="Modular_Message",  # 包名
      version="1.0",  # 版本
      description="jason 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整的描述信息
      author="jason",  # 作者名字
      author_email="123456789@163.com",  # 作者邮箱
      url="www.jason.com",  # 作者主页
      py_modules=["Modular_Message.send_message",
                  "Modular_Message.receive_message"])  # 列表中记录包中所包含的模块


