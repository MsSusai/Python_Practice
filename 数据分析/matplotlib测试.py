# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/5/28  19:35 
# 名称：matplotlib测试.PY
# 工具：PyCharm
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family'] = 'kaiti'  # 解决汉字问题
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串

x = np.linspace(-10, 10, 50)
# y1 = x + 1
y2 = x ** 2
y3 = x

# plt.figure(num=3, figsize=(8, 5)) # figure分开画图
# plt.plot(x, y1)

plt.figure(figsize=(8, 8))
plt.plot(x, y2, color='yellow', label='up')
plt.plot(x, y3, color='red', linewidth=1.4, linestyle='--', label='down')  # 设置图线样式

# plt.xlim((-1, 2))
# plt.ylim((-2, 3))
plt.title('测试')
plt.xlabel('x轴')
plt.ylabel('y轴')

# plt.yticks([-2, -1, 0, 0.5, 3,], ['really bad', 'bad', 'normal', r'$good$', r'$really\ \alpha\ good$'])

# ax = plt.gca()  # 获取坐标轴
# ax.spines['right'].set_color('none')  # 除去右边边框
# ax.spines['top'].set_color('red')


plt.legend(loc='best')  # 生成图例

plt.show()
