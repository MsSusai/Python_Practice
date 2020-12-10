# 第一小问
lst_floor = [1, 4, 2, 5, 7, 3]
count = 0
for i in range(6):
    if i != 5:
        count = lst_floor[i + 1] - lst_floor[i]
        if count > 0:
            print("⬆" * count, end="")
        else:
            print("⬇" * abs(count), end="")
print()
# 第二小问
cnt = 0
floor = [2]
string = "⬆⬆⬇⬇⬇⬆⬆⬇⬆⬆⬆⬆"
for item in string:
    if item == "⬆":
        floor.append(floor[cnt] + 1)
        cnt += 1
    else:
        floor.append(floor[cnt] - 1)
        cnt += 1
print(floor)
