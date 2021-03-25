def selectSort(alist):
    for i in range(len(alist) - 1, 0, -1):
        positionMax = 0
        for location in range(1, i + 1):
            if alist[location] > alist[positionMax]:
                positionMax = location

        alist[positionMax], alist[i] = alist[i], alist[positionMax]


test = [1, 5, 6, 2, 3, 2]
selectSort(test)
print(test)
