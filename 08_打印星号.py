# 打印*组成的图形
for i in range(0, 6):
    for j in range(0, i+1):
        print("*", end='')
    print()
for i in range(0, 6):
    for j in range(0, 5-i+1):
        print("*", end='')
    print()
