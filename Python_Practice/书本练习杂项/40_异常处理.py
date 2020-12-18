try:
    a = int(input("a="))
    b = int(input("b="))
    c = a / b
except ZeroDivisionError:
    print("除数不能为0！")
else:
    print(c)
