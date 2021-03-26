def gapInsertSort(alist, start, gap):
    for index in range(start + gap, len(alist), gap):
        move = alist[index]
        position = index

        while position > 0:
            if alist[position - gap] > move:
                alist[position] = alist[position - gap]
                position = position - gap
            else:
                alist[position] = move
                break
        else:
            alist[position] = move


def shellSort(alist):
    sublistCount = len(alist) // 2

    while sublistCount > 0:

        for startPosition in range(sublistCount):
            gapInsertSort(alist, startPosition, sublistCount)

        sublistCount = sublistCount // 2


test = [1, 5, 6, 2, 3, 2, 6, 7, 9, 10]
shellSort(test)
print(test)
