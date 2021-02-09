from pythonds.basic import Queue
import random


class Printer:
    def __init__(self, ppm):
        self.pageRate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask is not None:
            return True
        else:
            return False

    def startNext(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60 / self.pageRate


class Task:
    def __init__(self, time):
        self.timeStamp = time
        self.pages = random.randint(1, 20)

    def getStamp(self):
        return self.timeStamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        return currentTime - self.timeStamp


def simulation(numSeconds, pagePerMinute):
    labPrinter = Printer(pagePerMinute)
    printQueue = Queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labPrinter.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            labPrinter.startNext(nextTask)

        labPrinter.tick()

    averageWait = sum(waitingTimes) / len(waitingTimes)
    print("平均等待时间是{:.2f}秒，有{}个任务剩余".format(averageWait, printQueue.size()))


def newPrintTask():
    num = random.randint(1, 180)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 5)
