domName = []

for i in range(4):
    name = input("输入第{}位舍友名字：".format(i+1))
    domName.append(name)

# print(domName)

for j in range(4):
    print(str(domName[j])[-1])
