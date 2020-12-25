def yourBirth(phoneNumber, birthYear):
    number = 0
    number = (((phoneNumber * 2) + 5) * 50) + 1766
    number = number - birthYear
    # 原测试为2016年时的测试
    # print(str(number)[-2:])
    # 此为2020年测试
    print(str(number + 4)[-2:])


phoneNumber = eval(input("输入手机号的最后一位："))
birthYear = eval(input("输入出生年份："))
yourBirth(phoneNumber, birthYear)
