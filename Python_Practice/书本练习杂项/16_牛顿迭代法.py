import math

x = eval(input("输入一个数："))
y = 1.0
n = 0
while abs(pow(y, 2) - x) >= 1e-8:
    y = (y + x / y) / 2
    n += 1
print("一共迭代了{}次".format(n))
print("通过牛顿迭代法{}的算数平方根为：{}".format(x, y))
print("通过平方根函数计算结果为：{}".format(math.sqrt(x)))
