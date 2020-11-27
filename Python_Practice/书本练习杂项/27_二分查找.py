ls = [34, 56, 75, 23, 46, 78, 3, 2, 4, 67, 43, 21, 78, 90]
x = eval(input("输入要查找的数："))
ls.sort()

low = 0
high = len(ls) - 1

while low <= high:
    mid = int((low + high) / 2)
    if ls[mid] == x:
        print("已找到{}，索引为{}".format(x, mid))
        break
    elif ls[mid] < x:
        low = mid + 1
    elif ls[mid] > x:
        high = mid - 1
else:
    print("没有找到{}".format(x))
