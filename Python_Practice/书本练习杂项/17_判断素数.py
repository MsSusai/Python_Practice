# 判断一个范围内的所有素数
span = eval(input("输入一个大于等于二的数："))
n = 0
if span < 2:
    print("输入有误！")
elif span == 2:
    print("2")
else:
    for i in range(2, span+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(end="{}\t".format(i))
            n += 1
            if n % 5 == 0:
                print("\t")
print("共有{}个素数".format(n))
