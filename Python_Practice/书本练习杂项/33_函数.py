def calSum(low, high):
    numberSum = 0
    for i in range(low, high + 1):
        numberSum += i
    return numberSum


low = eval(input("输入起始数："))
high = eval(input("输入终止数："))

print(calSum(low, high))
