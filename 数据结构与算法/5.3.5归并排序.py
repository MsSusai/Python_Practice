def mergeSort(alist):
    print("正在切分", alist)

    # 递归结束条件

    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
    else:
        return

    # 划分，递归调用
    mergeSort(left)
    mergeSort(right)

    # 合并左右列表
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            alist[k] = left[i]
            i += 1
        else:
            alist[k] = right[j]
            j += 1
        k += 1

    # 左列表还剩余
    while i < len(left):
        alist[k] = left[i]
        i += 1
        k += 1

    # 右列表还剩余
    while j < len(right):
        alist[k] = right[j]
        j += 1
        k += 1

    print("正在归并", alist)


# pythonic
def merge_sort(alist):
    # 递归结束条件
    if len(alist) <= 1:
        return alist

    # 划分，递归调用
    mid = len(alist) // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    # 合并左右列表
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)
    return merged


test = [1, 5, 6, 2, 3, 2, 6, 7, 9, 10]
print("pythonic")
print(merge_sort(test))
mergeSort(test)
print("normal")
print(test)
