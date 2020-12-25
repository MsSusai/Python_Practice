def sumNumber(number):
    strNumber = str(number)
    total = 0
    for char in strNumber:
        total += int(char)
    else:
        print("{}的各位数字之和为{}".format(number, total))


number = eval(input("输入一个数字："))
sumNumber(number)
