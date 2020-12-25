def isTrue(number):
    total = 0
    numberLst = []
    for i in range(3, 7 + 1):
        strNumber = str(number * i)
        for char in strNumber:
            total += int(char)
        numberLst.append(total)
        total = 0
    return numberLst


sumNumber = 0
for j in range(100, 1000):
    numberList = isTrue(j)
    setList = set(numberList)
    if len(setList) == 1:
        sumNumber += 1
        print("x={}:x*3={},x*4={},x*5={},x*6={},x*7={}"
              .format(j, j * 3, j * 4, j * 5, j * 6, j * 7))
print("共有{}个符合条件的三位数".format(sumNumber))
