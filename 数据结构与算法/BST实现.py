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
        self.root = self.insertNode(self.root, valList[0])  # 标记根节点，便于后续第一个传入根节点
        for i in range(1, len(valList)):  # 去除根节点使用过的数
            self.root = self.insertNode(self.root, valList[i])

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

    def __removeNode1_leaf__(self, node):  # 删除叶子节点
        if node.parent is None:  # 只有一个根节点
            self.root = None
        else:
            if node.parent.leftChild == node:  # 删除左子节点
                node.parent.leftChild = None
            else:  # 删除右子节点
                node.parent.rightChild = None

    def __removeNode2_left__(self, node):  # 有一个左子节点
        if node.parent is None:  # 要删除的是根节点
            self.root = node.leftChild
            node.leftChild.parent = None
        else:
            if node.leftChild and node == node.leftChild.parent:  # 后续节点是要删除节点的左节点
                node.leftChild.parent = node.parent
                node.parent.leftChild = node.leftChild
            else:  # 后续节点是要删除节点的右节点
                node.rightChild.parent = node.parent
                node.parent.leftChild = node.rightChild

    def __removeNode2_right__(self, node):  # 有一个右子节点
        if node.parent is None:  # 要删除的是根节点
            self.root = node.rightChild
            node.rightChild = None
        else:
            if node.leftChild and node == node.leftChild.parent:  # 后续节点是要删除节点的左节点
                node.leftChild.parent = node.parent
                node.parent.rightChild = node.leftChild
            else:  # 后续节点是要删除节点的右节点
                node.rightChild.parent = node.parent
                node.parent.rightChild = node.rightChild

    def deleteNode(self, val):
        if self.root:  # 不是空树
            node = self.searchNode(self.root, val)
            if node is None:  # 要删除的节点不存在
                raise "没有找到要删除的节点"
            else:
                if node.leftChild and node.rightChild is None:  # node是叶子节点
                    self.__removeNode1_leaf__(node)
                elif node.leftChild and not node.rightChild:  # node只有左子节点
                    self.__removeNode2_left__(node)
                elif not node.leftChild and node.rightChild:  # node只有右子节点
                    self.__removeNode2_right__(node)
                else:  # node两个子节点都有
                    minNode = node.rightChild
                    while minNode.leftChild:  # 找到最小节点
                        minNode = minNode.leftChild
                    node.data = minNode.data  # 替换
                    if minNode.rightChild:  # 移除最小节点
                        self.__removeNode2_right__(minNode)
                    else:
                        self.__removeNode1_leaf__(minNode)


tree = BinarySearchTree([4, 5, 2, 3, 6])
print(tree.searchNode(tree.root, 6))
tree.postOrder(tree.root)
print()
tree.deleteNode(5)
tree.postOrder(tree.root)
tree.deleteNode(4)
print()
tree.postOrder(tree.root)

