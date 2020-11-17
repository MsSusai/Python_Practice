count = 0
for i in range(1000, 2000 + 1):
    if i % 400 == 0 or (i % 100 != 0 and i % 4 == 0):
        count += 1
        print(i, end=" \t")
        if count % 5 == 0:
            print("\t")
