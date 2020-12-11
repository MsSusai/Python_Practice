# 递归求阶乘
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


for i in range(9):
    print("{}!={}".format(i, fact(i)))


# 递归求斐波那契数列
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


for i in range(1, 20 + 1):
    print(fibo(i), end=" " if i % 5 != 0 else "\n")
