# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/10/25  16:31 
# 名称：6.7.1二叉查找树.PY
# 工具：PyCharm
class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, leftChildren, rightChildren):
        self.key = key
        self.value = value
        self.leftChild = leftChildren
        self.rightChild = rightChildren
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def _put_(self, key, value, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put_(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, value, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put_(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value, parent=currentNode)

    def put(self, key, value):
        if self.root:
            self._put_(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def __setitem__(self, key, value):
        self.put(key, value)

    def _get_(self, key, currentNode):
        if key < currentNode.key:
            return self._get_(key, currentNode.leftChild)
        elif key > currentNode.key:
            return self._get_(key, currentNode.rightChild)
        elif key == currentNode.key:
            return currentNode
        else:
            return None

    def get(self, key):
        if self.root:
            res = self._get_(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get_(key, self.root):
            return True
        else:
            return False
