def sumSquare(n, m):
    total = 0
    for j in range(1, n + 1):
        total += pow(j, m)
    return total


totalSum = 0
totalSum += sumSquare(100, 1)
totalSum += sumSquare(50, 2)
totalSum += sumSquare(10, -1)
print(totalSum)
