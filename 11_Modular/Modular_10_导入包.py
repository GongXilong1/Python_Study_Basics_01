import Modular_Message  # 导入Modular_Message包

Modular_Message.send_message.send("hello")  # 通过Modular_Message包使用send_message这个模块中的send函数发送文本 hello
txt = Modular_Message.receive_message.receive()  # 用变量txt接收 通过Modular_Message包使用receive_message这个模块中的receive函数的返回结果。
print(txt)

