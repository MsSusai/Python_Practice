def insertSort(alist):
    for index in range(1, len(alist)):
        move = alist[index]
        vacantIndex = index

        while vacantIndex > 0:
            if alist[vacantIndex - 1] > move:
                alist[vacantIndex] = alist[vacantIndex - 1]
                vacantIndex -= 1
            else:
                alist[vacantIndex] = move
                break


test = [1, 5, 6, 2, 3, 2, 6, 7, 9, 10]
insertSort(test)
print(test)
