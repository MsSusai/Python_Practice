front = 1
behind = 1
temp = 0
cnt = 2
print(front, end=" \t")
print(behind, end=" \t")
for i in range(1, 19):
    temp = behind
    behind = behind + front
    front = temp
    print(behind, end=" \t")
    cnt += 1
    if cnt % 5 == 0:
        print("\t")
