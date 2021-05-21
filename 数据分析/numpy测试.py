import numpy as np

a = np.array([[1, 1],
              [2, 3]])
b = np.arange(1, 5).reshape(2, 2)

print(a)
print(b)
# c = a * b
# print(c)

# 运算操作
# c_dot = np.dot(a, b)  # 矩阵乘法
# c_dot2 = a.dot(b)
# c_dot3 = a @ b
# print(c_dot)

# print(np.max(a, axis=0))  # 每一列最大的数
# print(np.max(a, axis=1))  # 每一行最大的数
#
# print(a.transpose())  # 矩阵转置
# print(a.T)

# print(a.mean(axis=0))  # 求平均数（对列）
# print(a.mean(axis=1))

# 遍历
# for row in a:  # 打印出每一行
#     print(row)

# for col in a.T: # 打印出每一列
#     print(col)

# for item in a.flat: # 打印出每一个元素
#     print(item)

# 合并
# d = np.array([1, 1, 1])
# e = np.array([2, 2, 2])
# f = np.vstack((d, e))  # 纵向合并
# g = np.hstack((d, e))  # 横向合并
# print(f)
# print(g)
# print(d.reshape(-1, 1))

# 分割
# print(np.split(a, 2, axis=0))  # 横向分割
# print(np.split(a, 2, axis=1))  # 纵向分割
# print(np.vsplit(a, 2))
# print(np.hsplit(a, 2))
# print(np.array_split(a, 3, axis=0)) # 不等分割
