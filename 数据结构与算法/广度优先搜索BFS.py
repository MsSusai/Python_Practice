# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/11/3  10:34 
# 名称：广度优先搜索BFS.PY
# 工具：PyCharm
from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue


def buildGraph(file):
    bucket = {}
    wordGraph = Graph()
    # 构建词桶
    with open(file, 'r') as wordFile:
        for word in wordFile:
            word = word.strip('\n')  # 去除每一行的换行符
            for i in range(len(word)):
                underlineWord = word[:i] + '_' + word[i + 1:]
                if underlineWord in bucket:
                    bucket[underlineWord].append(word)
                else:
                    bucket[underlineWord] = [word]
    # 为词桶里每个词创建边
    for underlineWord in bucket.keys():
        for word1 in bucket[underlineWord]:
            for word2 in bucket[underlineWord]:
                if word1 != word2:
                    wordGraph.addEdge(word1, word2)

    return wordGraph


def breadthFirstSearch(start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        dequeueVert = vertQueue.dequeue()
        for neighbor in dequeueVert.getConnections():
            if neighbor.getColor() == 'white':
                vertQueue.enqueue(neighbor)
                neighbor.setColor('gray')
                neighbor.setDistance(dequeueVert.getDistance() + 1)
                neighbor.setPred(dequeueVert)
        dequeueVert.setColor('black')


def traverse(lastWord):
    while lastWord.getPred():
        print(lastWord.getId())
        lastWord = lastWord.getPred()
    print(lastWord.getId())


if __name__ == '__main__':
    wordGraph = buildGraph("fourletterwords.txt")
    # print(wordGraph.getVertices())
    start = wordGraph.getVertex('FOOL')
    # print(start)
    breadthFirstSearch(start)
    traverse(wordGraph.getVertex('SAGE'))
