num = eval(input("输入一个数字，输入-1结束\n"))
count = 0
sum = 0
min = num
max = num
while num != -1:
    count += 1
    sum += num
    if min > num:
        min = num
    if max < num:
        max = num
    num = eval(input("输入一个数字，输入-1结束\n"))
if count > 0:
    print("最小值为：{} 最大值为：{} 均值为：{:.2f}\n".format(min, max, sum/count))
else:
    print("输入为空\n")


