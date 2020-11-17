x = eval(input("x="))
if x < 0:
    y = 0
    print(y)
elif 0 <= x < 5:
    y = x
    print(y)
elif 5 <= x < 10:
    y = 3 * x - 5
    print(y)
elif 10 <= x < 20:
    y = 0.5 * x - 2
    print(y)
else:
    y = 0
    print(y)
