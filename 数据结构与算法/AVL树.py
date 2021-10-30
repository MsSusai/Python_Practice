# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/10/30  10:09 
# 名称：AVL树.PY
# 工具：PyCharm
from BST实现 import TreeNode, BinarySearchTree


class AVLNode(TreeNode):
    def __init__(self, val):
        super(AVLNode, self).__init__(val)
        self.balanceFactor = 0


class AVLTree(BinarySearchTree):
    def __init__(self, valList=None):
        super(AVLTree, self).__init__(valList)

    @staticmethod
    def rotateLeft(a, b):  # 书206页图6-28
        s2 = b.leftChild
        a.rightChild = s2
        if s2:
            s2.parent = a
        b.leftChild = a
        b.parent = a.parent
        a.parent = b

        # 更新平衡因子
        a.balanceFactor = 0
        b.balanceFactor = 0

    @staticmethod
    def rotateRight(a, b):
        s2 = b.rightChild
        a.leftChild = s2
        if s2:
            s2.parent = a
        b.rightChild = a
        b.parent = a.parent
        a.parent = b

        a.balanceFactor = 0
        b.balanceFactor = 0

    @staticmethod
    def rotateRightLeft(a, c):  # 书210页图6-33
        # 先右旋
        b = c.leftChild
        s3 = b.rightChild
        b.rightChild = c
        if s3:
            s3.parent = c
        c.leftChild = s3
        b.parent = c.parent
        c.parent = b

        # 再左旋
        s2 = b.leftChild
        a.rightChild = s2
        if s2:
            s2.parent = a
        b.leftChild = a
        b.parent = a.parent
        a.parent = b

        # 更新平衡因子
        if b.balanceFactor > 0:
            c.balanceFactor = 0
            a.balanceFactor = -1
        else:
            a.balanceFactor = 0
            c.balanceFactor = 1
        b.balanceFactor = 0

    @staticmethod
    def rotateLeftRight(a, c):
        # 先右旋
        b = c.rightChild
        s3 = b.leftChild
        b.leftChild = c
        if s3:
            s3.parent = c
        c.rightChild = s3
        b.parent = c.parent
        c.parent = b

        # 再左旋
        s2 = b.rightChild
        a.leftChild = s2
        if s2:
            s2.parent = a
        b.rightChild = a
        b.parent = a.parent
        a.parent = b

        # 更新平衡因子
        if b.balanceFactor < 0:
            c.balanceFactor = 0
            a.balanceFactor = 1
        else:
            a.balanceFactor = 0
            c.balanceFactor = -1
        b.balanceFactor = 0
