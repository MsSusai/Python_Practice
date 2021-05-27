# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/5/26  10:21 
# 名称：卡平方检验
# 工具：PyCharm
import numpy as np


def numberSum(O, E):
    spareSum = ((O - E) * (O - E)) / E
    print(spareSum)
    total = spareSum.sum()
    print(total)


if __name__ == '__main__':
    o = np.array([13, 1, 2, 3])
    e = np.array([4.75, 4.75, 4.75, 4.75])
    numberSum(o, e)
