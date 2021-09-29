# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/9/29  21:50 
# 名称：动态规划背包问题.PY
# 工具：PyCharm

def bag(n, c, w, v):
    """
    测试数据：
    n = 6  物品的数量，
    c = 10 书包能承受的重量，
    w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    # 置零，表示初始状态
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    for x in value:
        print(x)
    return value


def show(n, c, w, value):
    print('最大价值为:', value[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('背包中所装物品为:')
    for i in range(n):
        if x[i]:
            print('第', i + 1, '个,', end='')


def bag1(n, c, w, v):
    values = [0 for i in range(c + 1)]
    for i in range(1, n + 1):
        for j in range(c, 0, -1):
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1]:
                values[j] = max(values[j - w[i - 1]] + v[i - 1], values[j])
    return values


if __name__ == '__main__':
    n = 6
    c = 10
    w = [2, 2, 3, 1, 5, 2]
    v = [2, 3, 1, 5, 4, 3]
    value = bag(n, c, w, v)
    show(n, c, w, value)
    print('\n空间复杂度优化为N(c)结果:', bag1(n, c, w, v))
