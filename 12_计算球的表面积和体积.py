import math

r = eval(input("请输入球的半径："))
s = 4 * math.pi * pow(r, 2)
v = (4 / 3) * math.pi * pow(r, 3)
print("球的面积为：{}".format(s))
print("球的体积为：{}".format(v))
