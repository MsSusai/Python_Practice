# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/4/8  15:47 
# 名称：6.4.1树的嵌套列表实现.PY
# 工具：PyCharm
def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


r = BinaryTree(3)
insertLeft(r, 4)
insertRight(r, 5)
l = getLeftChild(r)
setRootVal(l, 7)
print(r)
