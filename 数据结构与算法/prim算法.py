# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/17  20:37 
# 名称：prim算法.PY
# 工具：PyCharm
from pythonds.graphs import PriorityQueue, Graph, Vertex
import sys


def prim(graph, start):
    priorityQueue = PriorityQueue()
    start.setDistance(0)
    priorityQueue.buildHeap((v.getDistance(), v) for v in graph)
    while not priorityQueue.isEmpty():
        currentVert = priorityQueue.delMin()
        for neighborVert in currentVert.getConnections():
            distance = currentVert.getDistance() + currentVert.getWeight(neighborVert)
            if distance < neighborVert.getDistance() and neighborVert in priorityQueue:
                neighborVert.setDistance(distance)
                neighborVert.setPred(currentVert)
                priorityQueue.decreaseKey(neighborVert, distance)
