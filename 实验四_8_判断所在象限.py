x = eval(input())
y = eval(input())
if x > 0 and y > 0:
    print("在第一象限")
elif x < 0 < y:
    print("在第二象限")
elif x < 0 and y < 0:
    print("在第三象限")
elif x > 0 > y:
    print("在第四象限")
else:
    print("输入错误！")