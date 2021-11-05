# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/4  10:46 
# 名称：深度优先搜索DFS.PY
# 工具：PyCharm
from pythonds.graphs import Graph
from pythonds.basic import Stack


def knightGraph(boardSize):
    graph = Graph()
    for row in range(boardSize):
        for col in range(boardSize):
            boardNodeId = row * boardSize + col
            newPosition = legalMoves(row, col, boardSize)
            for node in newPosition:
                newNodeId = node[0] * boardSize + node[1]
                graph.addEdge(boardNodeId, newNodeId)
    return graph


def legalMoves(x, y, boardSize):
    newMoves = []
    moveTo = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveTo:
        newMoveX = x + i[0]
        newMoveY = y + i[1]
        if 0 <= newMoveX < boardSize and 0 <= newMoveY < boardSize:
            newMoves.append((newMoveX, newMoveY))
    return newMoves


def knightTour(depth, path, startNode, limit=63):
    startNode.setColor('gray')
    path.push(startNode)
    if depth < limit:
        neighborList = orderByAvail(startNode)
        done = False
        n = 0
        while n < len(neighborList) and not done:
            if neighborList[n].getColor() == 'white':
                done = knightTour(depth + 1, path, neighborList[n], limit)
            n += 1
        if not done:
            path.pop()
            startNode.setColor('white')
    else:
        done = True
    return done


# Warnsdorff启发式算法
def orderByAvail(depthNode):
    resList = []
    for v in list(depthNode.getConnections()):
        if v.getColor() == 'white':
            c = 0
            for w in list(v.getConnections()):
                if w.getColor() == 'white':
                    c += 1
            resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


if __name__ == '__main__':
    graph = knightGraph(8)
    path = Stack()
    startVert = graph.getVertex(4)
    knightTour(0, path, startVert)
    idList = []
    for i in range(path.size()):
        idList.append(path.pop().getId())
    print(idList[::-1])
