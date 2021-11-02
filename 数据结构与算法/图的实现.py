# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/2  16:31 
# 名称：图的实现.PY
# 工具：PyCharm
class Vertex:  # 图的顶点
    def __init__(self, key):
        self.id = key
        self.connected = {}  # 顶点连接的其他顶点

    def addNeighbor(self, neighbor, weight=0):  # 将顶点与其他顶点连接起来
        self.connected[neighbor] = weight

    def __str__(self):
        return str(self.id) + '连接到' + str([i.id for i in self.connected])


class Graph:
    def __init__(self):
        self.vertList = {}  # 主列表

    def addVert(self, key):  # 添加顶点
        newVert = Vertex(key)
        self.vertList[key] = newVert

    def addEdge(self, _from_, _to_, cost=0):
        try:
            self.vertList[_from_].addNeighbor(self.vertList[_to_], cost)
        except Exception:
            raise "请检查连接的两个节点是否都存在"

    def getVert(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


if __name__ == '__main__':
    graph = Graph()
    for i in range(2):
        graph.addVert(i)
    print(graph.getVert())
    graph.addEdge(0, 1, 5)
    graph.addEdge(1, 0, 2)
    for vert in graph:
        print(vert)
