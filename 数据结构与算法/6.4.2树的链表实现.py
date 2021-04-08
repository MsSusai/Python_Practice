# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/4/8  16:20 
# 名称：6.4.2树的链表实现.PY
# 工具：PyCharm
class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNodeValue):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNodeValue)
        else:
            r = BinaryTree(newNodeValue)
            r.leftChild = self.leftChild
            self.leftChild = r

    def insertRight(self, newNodeValue):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNodeValue)
        else:
            r = BinaryTree(newNodeValue)
            r.rightChild = self.rightChild
            self.rightChild = r

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootValue(self, newValue):
        self.key = newValue

    def getRootValue(self):
        return self.key


t = BinaryTree(1)
print(t.getRootValue())
t.insertLeft(2)
t.insertRight(3)
t.insertLeft(4)
print(t.getLeftChild().getRootValue())
