import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([9, 8, 7, 6, 5])
c = a ** 2 + b ** 3
print(c)
print(c.dtype)
print(c.ndim)
print(c.shape)
print(c.size)
print(c.itemsize)
d = np.eye(9)
print(d)


def foo(n):
    yield n * n


for j in range(3):
    for i in foo(j):
        print(i)
