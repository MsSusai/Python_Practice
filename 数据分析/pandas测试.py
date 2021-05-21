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


# dates = pd.date_range('20210521', periods=6)
# value = np.arange(24).reshape(6, 4)
# df1 = pd.DataFrame(value, index=dates, columns=['A', 'B', 'C', 'D'])
# print(df1)

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


# 合并concat
# df2 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['A', 'B', 'C', 'D'])
# df3 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['A', 'B', 'C', 'D'])
# df4 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['A', 'B', 'C', 'D'])
# res = pd.concat([df2, df3, df4], axis=0, ignore_index=True)
# print(res)

# join ['inner','outer']
# df3 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['A', 'B', 'C', 'D'], index=[1, 2, 3])
# df4 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['B', 'C', 'D', 'E'], index=[2, 3, 4])
# res = pd.concat([df3, df4], join='inner', ignore_index=True)  # 交集
# res = pd.concat([df3, df4], join='outer')  # 并集
# print(res)

# append
# df2 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['A', 'B', 'C', 'D'])
# df3 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['A', 'B', 'C', 'D'])
# res = df2.append(df3, ignore_index=True)
# print(res)

# merge
# left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                      'A': ['A0', 'A1', 'A2', 'A3'],
#                      'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
#                       'C': ['C0', 'C1', 'C2', 'C3'],
#                       'D': ['D0', 'D1', 'D2', 'D3']})
# res = pd.merge(left, right, on='key')
# print(res)


# how参数
# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                      'key2': ['K0', 'K1', 'K0', 'K1'],
#                      'A': ['A0', 'A1', 'A2', 'A3'],
#                      'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                       'key2': ['K0', 'K0', 'K0', 'K0'],
#                       'C': ['C0', 'C1', 'C2', 'C3'],
#                       'D': ['D0', 'D1', 'D2', 'D3']})
# res = pd.merge(left, right, on=['key1', 'key2'], how='inner')  # default for how='inner'
# how = ['left', 'right', 'outer', 'inner']
# res = pd.merge(left, right, on=['key1', 'key2'], how='left')
# print(res)


# indicator
# df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
# df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
# print(df1)
# print(df2)
# res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
# # give the indicator a custom name
# res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
