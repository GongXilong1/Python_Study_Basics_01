def sum_numbers(*args):
    # def sum_numbers(args):   # 使用此方法，在15行的代码中，要有两组小括号，result = sum_numbers((1, 2, 3, 4, 5))

    num = 0

    print(args)

    # 循环遍历
    for n in args:
        num += n

    return num


result = sum_numbers(1, 2, 3, 4, 5)
print(result)
