def insertSort(alist):
    for index in range(1, len(alist)):
        move = alist[index]
        position = index

        while position > 0:
            if alist[position - 1] > move:
                alist[position] = alist[position - 1]
                position -= 1
            else:
                alist[position] = move
                break


test = [1, 5, 6, 2, 3, 2]
insertSort(test)
print(test)
