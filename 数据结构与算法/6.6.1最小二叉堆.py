# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/4/22  16:11 
# 名称：6.6.1最小二叉堆.PY
# 工具：PyCharm
class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, current):
        stop = False
        while current // 2 > 0 and not stop:
            if self.heapList[current] < self.heapList[current // 2]:
                self.heapList[current], self.heapList[current // 2] = self.heapList[current // 2], self.heapList[
                    current]
            else:
                stop = True
            current = current // 2

    def findMin(self):
        return self.heapList[1]

    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False

    def size(self):
        return self.currentSize

    def delMin(self):
        minValue = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize -= 1
        self.percDown(1)
        return minValue

    def percDown(self, current):
        stop = False
        while current * 2 <= self.currentSize and not stop:
            father = self.minChild(current)
            if self.heapList[current] > self.heapList[father]:
                self.heapList[current], self.heapList[father] = self.heapList[father], self.heapList[current]
            else:
                stop = True
            current = father

    def minChild(self, current):
        if current * 2 + 1 > self.currentSize:
            return current * 2
        else:
            if self.heapList[current * 2] > self.heapList[current * 2 + 1]:
                return current * 2 + 1
            else:
                return current * 2

    def buildHeap(self, alist):
        self.heapList = [0] + alist[:]
        self.currentSize = len(alist)
        father = len(alist) // 2
        while father > 0:
            self.percDown(father)
            father -= 1


bh = BinaryHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)
print(bh.delMin())
print(bh.delMin())
print(bh.isEmpty())
print(bh.size())
print(bh.findMin())
ls = [9, 6, 5, 2, 3]
bh2 = BinaryHeap()
bh2.buildHeap(ls)
print(bh2.delMin())
