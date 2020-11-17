even = 0
odd = 0
number = input("输入一个数，输入‘A’结束：")
i = 0

while number != 'A':
    i += 1
    number = eval(number)
    if number % 2 == 0:
        even += number
    else:
        odd += number
    number = input("第{}个数".format(i + 1))

print("奇数和为{}，偶数和为{}，平均数为{}".format(odd, even, (odd + even) / i))
