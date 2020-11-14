from random import randint

n = eval(input("输入投掷次数："))
count0 = 0
count1 = 0

for i in range(n):
    coin = randint(0, 1)
    if coin == 0:
        count0 += 1
    else:
        count1 += 1
print("反面出现{}次，概率是{}，正面出现{}次，概率是{}".format(count0, count0 / n, count1, count1 / n))
