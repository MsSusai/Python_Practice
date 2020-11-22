value = []
n = eval(input("输入n："))
maxCount = 0

if n >= 1:
    for i in range(1, n+1):
        if i % 17 == 0:
            maxCount = i

    if maxCount != 0:
        print("{}以内能被17整除的最大正整数是{}".format(n, maxCount))
    else:
        print("没有能被17整除的整数")

else:
    print("输入有误！")
