import math

a = eval(input("请输入三角形的第一条边长："))
b = eval(input("请输入三角形的第二条边长："))
c = eval(input("请输入三角形的第三条边长："))
l = (a + b + c) / 2
s = math.sqrt(l * (l - a) * (l - b) * (l - c))
print("该三角形的面积为{}".format(round(s, 2)))
