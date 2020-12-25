import random


def redPack(totalMoney, number):
    redPackList = []
    for i in range(number):
        # randomMoney = round(random.uniform(0.01, totalMoney), 2)
        randomMoney = round(random.uniform(0.01, totalMoney / (number - i)), 2)
        redPackList.append(randomMoney)
        totalMoney = totalMoney - randomMoney
    redPackList.append(round(totalMoney, 2))
    print(redPackList)
    print(sum(redPackList))


redPack(100, 15)
