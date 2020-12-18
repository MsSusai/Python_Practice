import os

print(os.getcwd())


def readFile(fileName):
    with open(fileName, 'r', encoding='UTF-8') as file:
        result = file.read()
        return result


def comment(result):
    comCnt = {}
    res = result.split()
    for word in res:
        comCnt[word] = comCnt.get(word, 0) + 1
    return comCnt


res = readFile('mydata.txt')
comCnt = comment(res)
print(comCnt)
