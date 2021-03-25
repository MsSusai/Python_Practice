def bubbleSort(alist):
    total = len(alist) - 1

    for i in range(len(alist) - 1):
        for j in range(total):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]

        total -= 1


def shortBubbleSort(alist):
    exchange = True
    passNum = len(alist) - 1

    while passNum > 0 and exchange:
        exchange = False
        for i in range(passNum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

        passNum += 1


test = [1, 5, 6, 2, 3, 2]
bubbleSort(test)
print(test)
