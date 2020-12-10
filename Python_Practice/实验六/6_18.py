s = "语文：80，数学：82，英语：90，物理：85，化学：88，美术：80"
stringList = s.split("，")
print(stringList)
sumCnt = 0
for item in stringList:
    sumCnt += int(item[-2:])
print("总分为：{:.1f}，平均分为{:.1f}".format(sumCnt, sumCnt / 6))
