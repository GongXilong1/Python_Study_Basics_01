# 定义字符串变量 name，输出 我的名字叫 小明，请多多关照！
name = "大明"

print("我的名字叫 %s，请多多关照！" % name)

# 定义整数变量 student_no，输出 我的学号是 000001
# student_no = 101
# print("我的学号是 %06d" % student_no)

student_no = 10122563
print("我的学号是 %06d" % student_no)
# %06d表示原来数值小于等于6位的数，在不满足的时候输出前面用0 补齐六位，如果数值大于六位，则显示原来的值。

# 定义小数 price weight money ,
# 输出 苹果的单价 9.00元/斤，购买了5.5斤，需要支付49.5元
price = 9.0
weight = 5.5
money = price * weight
# %.2f 数字2表示小数点后的位数
print("苹果的单价 %.2f 元/斤，购买了 %.3f 斤，需要支付 %.2f 元" % (price, weight, money))


# 定义一个小数 scale. 输出 数据比例是 10.00%
scale = 0.37
print("数据比例是 %.2f%%" % (scale * 100))
# 格式化输出%，要用%%。
# (scale * 100)用括号括起来，表示scale * 100 是算数运算，不是直接输出。
