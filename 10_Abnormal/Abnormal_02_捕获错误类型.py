try:
    # 提示用户输入一个整数
    num = int(input("输入一个整数："))

    # 使用 8 除以用户输入的整数并且输出
    result = 8 / num
    print(result)
except ZeroDivisionError:  # except + 错误类型（Python报错最后一行的第一个单词）
    print("除0错误")
except ValueError:
    print("值错误，请输入正确的整数")

