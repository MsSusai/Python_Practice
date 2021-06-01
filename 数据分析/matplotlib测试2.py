# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/6/1  20:52 
# 名称：matplotlib测试2.PY
# 工具：PyCharm
import matplotlib.pyplot as plt
import numpy as np

# 散点图
# total = 1024
# X = np.random.random(total)
# Y = np.random.random(total)
# T = np.arctan2(Y, X)

# plt.figure(figsize=(10, 10))
# plt.scatter(X, Y, c=T, alpha=0.3)

# 柱状图
n = np.arange(10)
Y1 = np.random.randint(1, 10, 10)

lst = list(Y1)
keyList = []
valueList = []
count = {}

for i in lst:
    count[i] = count.get(i, 0) + 1
# print(count)
for key, value in count.items():
    keyList.append(key)
    valueList.append(value)

plt.bar(keyList, valueList, facecolor='#9999ff')

plt.xlim((0, 10))
plt.xticks(n[::])
# plt.yticks(())

for x, y in zip(keyList, valueList):
    plt.text(x - 0.1, y + 0.1, '{}'.format(y))

axs = plt.gca()
axs.spines['right'].set_visible(False)
axs.spines['top'].set_visible(False)
# axs.spines['bottom'].set_visible(False)
# axs.spines['left'].set_visible(False)

plt.show()
