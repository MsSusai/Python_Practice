# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/4/8  17:01 
# 名称：6.5.1解析树.PY
# 工具：PyCharm
from pythonds.basic import Stack
from pythonds.trees import BinaryTree


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
