from math import sqrt

a = eval(input("输入第一条边长"))
b = eval(input("输入第二条边长"))
c = eval(input("输入第三条边长"))

if a > 0 and b > 0 and 0 < c < a + b and a + c > b and b + c > a:
    triRound = a+b+c
    h = triRound/2
    triSquare = sqrt(h*(h-a)*(h-b)*(h-c))
    print("三角形的周长为{:.1f}，面积为{:.1f}".format(triRound, triSquare))

else:
    print("输入的三边无法构成三角形")
