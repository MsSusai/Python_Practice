def selectSort(alist):
    total = len(alist)

    for i in range(len(alist) - 1):
        positionMax = 0
        for location in range(1, total):
            if alist[location] > alist[positionMax]:
                positionMax = location

        alist[positionMax], alist[total - 1] = alist[total - 1], alist[positionMax]
        total = total - 1


test = [1, 5, 6, 2, 3, 2, 10, 6]
selectSort(test)
print(test)
