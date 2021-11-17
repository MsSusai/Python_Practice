# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/15  21:59 
# 名称：强连通分量.PY
# 工具：PyCharm
from 通用DFS import DFSGraph


def generateDFS(DFSgraph):
    for i in range(6):
        DFSgraph.addVertex(chr(ord('A') + i))
    # print(graph.getVertices())
    DFSgraph.addEdge(DFSgraph.getVertex('A'), DFSgraph.getVertex('D'))
    DFSgraph.addEdge(DFSgraph.getVertex('A'), DFSgraph.getVertex('B'))
    DFSgraph.addEdge(DFSgraph.getVertex('B'), DFSgraph.getVertex('C'))
    DFSgraph.addEdge(DFSgraph.getVertex('B'), DFSgraph.getVertex('D'))
    DFSgraph.addEdge(DFSgraph.getVertex('D'), DFSgraph.getVertex('E'))
    DFSgraph.addEdge(DFSgraph.getVertex('E'), DFSgraph.getVertex('B'))
    DFSgraph.addEdge(DFSgraph.getVertex('E'), DFSgraph.getVertex('F'))
    DFSgraph.addEdge(DFSgraph.getVertex('F'), DFSgraph.getVertex('C'))
    return DFSgraph


def GT(graph):  # 图转置
    newGraph = DFSGraph()
    for vertex in graph.getVertices():
        newGraph.addVertex(vertex)
    for vertex in graph.getVertices():
        for connection in newGraph.getVertex(vertex).getConnections():
            newGraph.addEdge(newGraph.getVertex(connection), vertex)
    return newGraph


if __name__ == '__main__':
    graph = DFSGraph()
    graph = generateDFS(graph)
    graph.DFS()
    newTGraph = GT(graph)
    newTGraph.DFS()
