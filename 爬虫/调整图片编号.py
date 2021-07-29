# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/7/27  21:56 
# 名称：调整图片编号.PY
# 工具：PyCharm
import os


# 首先改变所有名称，前面加标记i防止重名
def changeNames(path, files):
    newName = ""
    for file in files:
        oldName = path + os.sep + file

        if '缺' in file:
            signalFileNumber = int(file[:-7])

            if 22 <= signalFileNumber < 64:
                newName = path + os.sep + 'i' + str(signalFileNumber + 1) + '.jpg'
            elif 64 <= signalFileNumber < 143:
                newName = path + os.sep + 'i' + str(signalFileNumber + 2) + '.jpg'
            elif signalFileNumber >= 143:
                newName = path + os.sep + 'i' + str(signalFileNumber + 3) + '.jpg'
        else:
            signalFileNumber = int(file[:-4])

            if signalFileNumber <= 22:
                newName = oldName
            elif 22 < signalFileNumber <= 64:
                newName = path + os.sep + 'i' + str(signalFileNumber + 1) + '.jpg'
            elif 64 < signalFileNumber <= 143:
                newName = path + os.sep + 'i' + str(signalFileNumber + 2) + '.jpg'
            elif signalFileNumber > 143:
                newName = path + os.sep + 'i' + str(signalFileNumber + 3) + '.jpg'

        os.rename(oldName, newName)
        print(oldName, '======>', newName)


# 其次去掉所有标记i
def adjustNames(path, files):
    for f in files:
        oldName = path + os.sep + f

        if 'i' in f:
            newName = path + os.sep + str(int(f[1:-4])) + '.jpg'
        else:
            continue

        os.rename(oldName, newName)
        print(oldName, '======>', newName)


if __name__ == '__main__':
    path = r"E:\Code\python练习\爬虫\翻译"
    files = os.listdir(path)

    # files.sort(key=lambda x: int(x[:-4]))
    # print(files)

    changeNames(path, files)
    adjustNames(path, files)
