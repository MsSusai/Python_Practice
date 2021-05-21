# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/5/21  15:00 
# 名称：pandas测试.PY
# 工具：PyCharm
import numpy as np
import pandas as pd

# df1 = pd.DataFrame(np.random.randn(6, 4), columns=['A', 'B', 'C', 'D'], index=[1, 2, 3, 4, 5, 6])
# print(df1)

# print(df1.describe())
# print(df1.values)
# print(df1.columns)
# print(df1.index)

# print(df1.T)
# print(df1.transpose)

# print(df1.sort_index(axis=0, ascending=False))
# print(df1.sort_values(by='A'))

dates = pd.date_range('20210521', periods=6)
value = np.arange(24).reshape(6, 4)
df1 = pd.DataFrame(value, index=dates, columns=['A', 'B', 'C', 'D'])
print(df1)

# 简单切片
# print(df1.A)  # 打印A行数据
# print(df1['A'])
# print(df1[1:3])  # 打印1-2行数据
# print(df1['20210521':'20210523']) # 切片索引

# 按照标签选择数据：loc
# print(df1.loc['20210521'])  # 具体查找20210521一行的值
# print(df1.loc[:, ['A', 'B']])  # 筛选AB行数据（前行后列）

# 按照位置选择数据：iloc
# print(df1.iloc[0, 0]) # 单个筛选
# print(df1.iloc[:2, 0:2]) # 连续筛选
# print(df1.iloc[[0, 1, 3], :2])  # 不连续筛选

# 指定大小关系数据筛选
# print(df1[df1['A'] > 8])  # 按照A行为标准筛选出大于8的所有数据
# print(df1[df1['A'] > 8]['C'])  # 大于8且C行数据
# print(df1[df1['A'] > 8].loc[:, ['A', 'B']]) # 大于8且AB行数据

# 修改数据
# df1.loc['20210521', 'A'] = 111 # 单个修改
# print(df1)

# df1[df1['A'] > 0] = 111 # 选择性修改
# print(df1)
# df1.B[df1.A > 0] = 111 # 只改B行，基准为A行
# print(df1)

# 处理丢失数据
# df1.iloc[0, 0] = np.nan
# print(df1)
# print(df1.dropna(axis=0, how='any'))  # 有nan就丢掉行
# print(df1.dropna(axis=0, how='all'))  # 全nan才丢掉行
# print(df1.fillna(value=111)) # 替换nan值

