# n为盘子数量，a为起始柱子，b为过度柱子，c为目标柱子
count = 0


def move(n, a, b, c):
    global count
    if n == 1:
        count += 1
        print(a, "-->", c)
    else:
        move(n - 1, a, c, b)
        print(a, "-->", c)
        move(n - 1, b, a, c)


move(20, 'A', 'B', 'C')
print("共执行{}次".format(count + 1))
