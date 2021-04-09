# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/4/8  17:01 
# 名称：6.5.1解析树.PY
# 工具：PyCharm
from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator


# 解析树
def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for word in fplist:
        if word == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif word not in '+-*/)':
            currentTree.setRootVal(eval(word))
            currentTree = pStack.pop()
        elif word in '+-*/':
            currentTree.setRootVal(word)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif word == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError('运算表达式出现问题：' + word)

    return eTree


# 计算解析树
def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


# 前序遍历
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


# 中序遍历
def postorder(tree):
    if tree:
        preorder(tree.getLeftChild())
        print(tree.getRootVal())
        preorder(tree.getRightChild())


# 后序遍历
def inorder(tree):
    if tree:
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        print(tree.getRootVal())


# 后序求值
def postorderEval(tree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}
    if tree:
        leftVal = postorderEval(tree.getLeftChild())
        rightVal = postorderEval(tree.getRightChild())
        if leftVal and rightVal:
            return opers[tree.getRootVal()](leftVal, rightVal)
        else:
            return tree.getRootVal()


# 还原完全括号表达式
def printExp(tree):
    sumVal = ''

    if tree:
        currentVal = tree.getRootVal()
        if isinstance(currentVal, int):
            sumVal = printExp(tree.getLeftChild())
        else:
            sumVal = '(' + printExp(tree.getLeftChild())

        sumVal = sumVal + str(tree.getRootVal())

        if isinstance(currentVal, int):
            sumVal = sumVal + printExp(tree.getRightChild())
        else:
            sumVal = sumVal + printExp(tree.getRightChild()) + ')'
    return sumVal


etree = BinaryTree('*')
etree.insertRight(2)
etree.insertLeft(3)
preorder(etree)
print(printExp(etree))
print(postorderEval(etree))
