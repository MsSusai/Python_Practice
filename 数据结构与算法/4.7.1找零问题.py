def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(1, change + 1):
        coinCount = cents
        newCoin = 1
        for i in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - i] + 1 <= coinCount:
                coinCount = minCoins[cents - i] + 1
                newCoin = i
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


def printCoins(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin -= thisCoin


cl = [1, 5, 10, 21, 25]
coinUsed = [0] * 64
coinCount = [0] * 64
print(dpMakeChange(cl, 63, coinCount, coinUsed))
print(printCoins(coinUsed, 63))
