year = eval(input("输入一个年份："))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("{}年是闰年".format(year))
else:
    print("{}不是闰年".format(year))

