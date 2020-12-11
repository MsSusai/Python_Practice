f = lambda x: x < 0
list = [3, -5, 4, -3, -20]
for i in filter(f, list):
    print(i)

for i in filter(lambda x: x % 3 == 0 and x % 10 == 5, range(1, 100 + 1)):
    print(i)

dict_data = {"化1704": 33, "化1702": 28, "化1701": 34, "化1703": 30}
print(sorted(dict_data))  # 按键排序，输出键值
print(sorted(dict_data.items()))  # 按键排序，输出键值对
print(sorted(dict_data.items(), key=lambda x: x[1]))  # 按值排序，输出键值对
print(sorted(dict_data.items(), key=lambda x: x[1] % 10))  # 按值个位数排序，输出键值对
