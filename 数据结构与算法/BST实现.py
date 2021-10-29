# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/10/29  10:11 
# 名称：BST实现.PY
# 工具：PyCharm
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.leftChild = None
        self.rightChild = None
        self.parent = None


class BinarySearchTree:
    def __init__(self, valList):
        self.root = None
        node = self.root = self.insertNode(self.root, valList[0])
        for i in range(1, len(valList)):
            node = self.insertNode(node, valList[i])

    def searchNode(self, node, val):
        if node is None:
            return None
        else:
            if val == node.data:
                return node
            elif val > node.data:
                self.searchNode(node.rightChild, val)
            elif val < node.data:
                self.searchNode(node.leftChild, val)
            else:
                raise "搜索时发生错误"

    def insertNode(self, node, val):
        if node is None:
            node = TreeNode(val)
        elif val > node.data:
            node.rightChild = self.insertNode(node.rightChild, val)
            node.rightChild.parent = node
        elif val < node.data:
            node.leftChild = self.insertNode(node.leftChild, val)
            node.leftChild.parent = node
        return node

    def postOrder(self, root):
        if root:
            self.postOrder(root.leftChild)
            print(root.data, end=" ")
            self.postOrder(root.rightChild)


tree = BinarySearchTree([1, 6, 4])
tree.postOrder(tree.root)
