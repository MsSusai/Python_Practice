# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/17  19:51 
# 名称：dijkstra算法.PY
# 工具：PyCharm
from pythonds.graphs import Graph, Vertex
import sys


def dijkstra(graph, start):
    queue = []
    start.setDistance(0)
    queue.append([(v, v.getDistance()) for v in graph])
    while queue:
        currentVert = queue.pop()
        for neighborVert in currentVert[0].getConnections():
            distance = currentVert[0].getDistance() + currentVert[0].getWeight(neighborVert)
            queue.append((neighborVert, distance))
            if distance < neighborVert.getDistance():
                neighborVert.setDistance(distance)
                neighborVert.setPred(currentVert[0])
                queue = queue.sort(key=lambda x: x[1], reverse=True)
