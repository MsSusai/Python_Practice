# 三位水仙花数
span = int(input("输入一个不小于100且不大于1000的数："))
count = 1
if span <= 100 or span >= 1000:
    print("输入有误！")
else:
    for i in range(100, span):
        a = int(str(i)[0])
        b = int(str(i)[1])
        c = int(str(i)[2])
        if a ** 3 + b ** 3 + c ** 3 == i:
            print(i, end=' ')
