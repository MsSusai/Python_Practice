a = eval(input("请输入第一个整数"))
b = eval(input("请输入第二个整数"))
if a > b:
    a, b = b, a
print(a, b)
