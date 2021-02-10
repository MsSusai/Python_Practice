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


# 无序列表类
class UnorderedList:
    def __init__(self):
        self.head = None

    # 判断链表是否为空
    def isEmpty(self):
        return self.head is None

    # 添加链表节点
    def addNode(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    # 查询链表长度
    def length(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.getNext()

        return count

    # 查询链表数据是否存在
    def searchNode(self, item):
        current = self.head
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

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

    # 在链表尾部添加数据
    def appendNode(self, item):
        current = self.head
        temp = Node(item)

        while current.getNext() is not None:
            current = current.getNext()

        current.setNext(temp)

    # 在链表指定的位置前插入数据
    def insertNode(self, item, index):
        temp = Node(item)
        current = self.head
        previous = None

        for i in range(index):
            if current is not None:
                previous = current
                current = current.getNext()
            else:
                break

        if previous is not None:
            if current is not None:  # 插入位置不在最后
                temp.setNext(current)
                previous.setNext(temp)
            else:  # 插入位置在最后或更多
                previous.setNext(temp)  # 直接插入最后
        else:  # 插入位置在头部
            temp.setNext(self.head)
            self.head = temp

    # 获得元素在节点中的位置
    def indexNode(self, item):
        index = 0
        current = self.head
        found = False

        while not found and current is not None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index += 1

        return index

    def popNode(self, *index):
        current = self.head
        previous = None

        if index:  # 删除中间节点
            count = index[0]
            for i in range(count):
                previous = current
                current = current.getNext()
            previous.setNext(current.getNext)

        else:  # 删除最后的节点
            while current.getNext() is not None:
                previous = current
                current = current.getNext()
            previous.setNext(None)

        return current.getData()
