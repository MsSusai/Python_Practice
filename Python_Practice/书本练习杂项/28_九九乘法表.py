# 正序输出
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={}".format(i, j, i * j), end=' ')
        if i == j:
            print("\n")
# 反序输出
for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print("{}*{}={}".format(i, j, i * j), end=' ')
        if i == j:
            print("\n")
