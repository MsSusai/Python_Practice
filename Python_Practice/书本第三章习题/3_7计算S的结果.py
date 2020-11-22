flag = 1
s = 1
denominator = 1
numerator = 1

while numerator / denominator > 1e-7:
    denominator += 2
    s = flag * (numerator / denominator)
    flag *= -1
print("结果为：{}".format(s))
