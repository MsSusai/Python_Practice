# 节点类
class Node:
    def __init__(self, initData):
        self.data = initData
        self.next = None

    # 获得当前节点数据
    def getData(self):
        return self.data

    # 到达下一个节点
    def getNext(self):
        return self.next

    # 设置节点数据
    def setData(self, newData):
        self.data = newData

    # 设置指向下一个节点
    def setNext(self, newNext):
        self.next = newNext


class OrderedList:
    def __init__(self):
        self.head = None

    # 判断链表是否为空
    def isEmpty(self):
        return self.head is None

    # 查询链表长度
    def length(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.getNext()

        return count

    # 移除链表数据
    def removeNode(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext)

    # 查找链表元素
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
