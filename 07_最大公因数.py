a = int(input("输入第一个数\n"))
b = int(input("输入第二个数\n"))
c = int(input("输入第三个数\n"))
for i in range(min(a, b, c), 0, -1):
    if a % i == 0 and b % i == 0 and c % i == 0:
        print("{}和{}和{}的最大公因数为：{}".format(a, b, c, i))
        break
