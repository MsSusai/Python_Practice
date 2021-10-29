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
        # 构造BST的方法
        node = self.root = self.insertNode(self.root, valList[0])  # 标记根节点，便于后续第一个传入根节点
        for i in range(1, len(valList)):  # 去除根节点使用过的数
            node = self.insertNode(node, valList[i])

    # BST搜索
    def searchNode(self, node, val):
        if node is None:  # 树为空
            return None
        else:  # 树不为空
            if val == node.data:
                return node
            elif val > node.data:
                find = self.searchNode(node.rightChild, val)
            elif val < node.data:
                find = self.searchNode(node.leftChild, val)
            else:
                raise "搜索时发生错误"
        return find

    # BST插入
    def insertNode(self, node, val):
        if node is None:  # 创造节点
            node = TreeNode(val)
        elif val > node.data:  # 值大于节点
            node.rightChild = self.insertNode(node.rightChild, val)  # node.rightChild = self...是为了连接父节点的右子节点
            node.rightChild.parent = node  # 将右子节点的父节点标记上
        elif val < node.data:  # 值小于节点
            node.leftChild = self.insertNode(node.leftChild, val)  # node.leftChild = self...是为了连接父节点的左子节点
            node.leftChild.parent = node  # 将左子节点的父节点标记上
        return node

    def postOrder(self, root):
        if root:
            self.postOrder(root.leftChild)
            print(root.data, end=" ")
            self.postOrder(root.rightChild)


tree = BinarySearchTree([1, 6, 4, 2])
print(tree.searchNode(tree.root, 6))
tree.postOrder(tree.root)
