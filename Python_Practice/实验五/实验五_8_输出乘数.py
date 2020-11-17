first = 1
second = 2
third = 3
numberSum = 0

for i in range(1, 100, 2):
    numberSum += first * second * third
    first += 2
    second += 2
    third += 2

print(numberSum)

