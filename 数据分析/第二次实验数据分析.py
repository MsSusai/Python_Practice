# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/10/5  16:18 
# 名称：第二次实验数据分析.PY
# 工具：PyCharm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from scipy import stats

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['axes.unicode_minus'] = False

data = pd.read_excel(r"C:\Users\sosai\Desktop\实验数据.xlsx")
data = data.dropna(axis=0, how='all').drop(axis=0, index=152)
print(data)

yield_sample = data[["湖南产量", "安徽产量", "四川产量", "重庆产量", "湖北产量"]] \
    .rename(index=data["年份"])
# plt.legend(bbox_to_anchor=(0.5, -0.2), loc=8, ncol=10)
yield_sample.plot.line(subplots=True)

plt.show()
