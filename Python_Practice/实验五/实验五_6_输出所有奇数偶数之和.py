even = 0
odd = 0

for i in range(10):
    number = eval(input("第{}个数".format(i + 1)))
    if number % 2 == 0:
        even += number
    else:
        odd += number
print("奇数和为{}，偶数和为{}，平均数为{}".format(odd, even, (odd + even) / 10))
