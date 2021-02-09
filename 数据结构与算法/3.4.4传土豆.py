from pythonds.basic import Queue


def hotPotato(namelist, num):
    playQueue = Queue()
    for name in namelist:
        playQueue.enqueue(name)

    while playQueue.size() > 1:
        for i in range(num):
            player = playQueue.dequeue()
            playQueue.enqueue(player)
        else:
            playQueue.dequeue()
    return playQueue.dequeue()


nameList = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
print(hotPotato(nameList, 7))
