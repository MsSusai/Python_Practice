# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/27  16:04 
# 名称：快速排序.PY
# 工具：PyCharm
def quickSort(startIndex, endIndex, numList):
    if startIndex >= endIndex:
        return
    else:
        mark = partition(numList, startIndex, endIndex)
        quickSort(startIndex, mark - 1, numList)
        quickSort(mark + 1, endIndex, numList)


def partition(numList, startIndex, endIndex):
    pivot = numList[startIndex]
    mark = startIndex
    for i in range(startIndex, endIndex + 1):
        if numList[i] < pivot:
            mark += 1
            numList[i], numList[mark] = numList[mark], numList[i]
    numList[mark], numList[startIndex] = numList[startIndex], numList[mark]
    return mark


if __name__ == '__main__':
    numList = [4, 7, 3, 5, 6, 2, 8, 1]
    quickSort(0, len(numList) - 1, numList)
    print(numList)
