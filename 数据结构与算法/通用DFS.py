# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/5  11:05 
# 名称：通用DFS.PY
# 工具：PyCharm
from pythonds.graphs import Graph


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def DFS(self):
        for vertex in self:
            vertex.setColor('white')
            vertex.setPred(None)
        for vertex in self:
            if vertex.getColor() == 'white':
                self.dfsVisit(vertex)

    def dfsVisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsVisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)


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


if __name__ == '__main__':
    graph = DFSGraph()
    DFSGraph = generateDFS(graph)
    DFSGraph.DFS()
    for vertex in DFSGraph:
        print(vertex.getId(), vertex.getDiscovery(), vertex.getFinish())
