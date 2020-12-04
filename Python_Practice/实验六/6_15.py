string = input("输入一段英语：")
char = string.split(' ')
char.reverse()
for item in char:
    print(item, end=' ')
