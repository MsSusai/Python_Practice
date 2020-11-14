start = 1
flag = 1
for i in range(365):
    if 1 <= flag <= 5:
        start += start * 0.01
        flag += 1
    if 6 <= flag <= 7:
        start -= start * 0.01
        flag += 1
        if flag > 7:
            flag = 1
print("郭大侠最终武力值为：{:.2f}".format(start))
