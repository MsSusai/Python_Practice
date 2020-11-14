a = eval(input("输入a："))
n = eval(input("输入n："))
numberSum = 0

for i in range(1, n + 1):
    numberSum += int(str(a) * i)
print(numberSum)