import math

r = eval(input("输入半径:\n"))
h = eval(input("输入高度:\n"))
volume = math.pi * r * r * h
print("半径为{}，高度为{}，体积为{:.2f}:\n".format(r, h, volume))
