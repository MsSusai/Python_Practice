month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthSearch = eval(input("输入要查询的月份："))
while monthSearch != 0 and monthSearch <= 12:
    print("{}月有{}天".format(monthSearch, month[monthSearch-1]))
    monthSearch = eval(input("输入要查询的月份："))
