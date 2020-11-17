count = 0
for i in range(2, 300):
    for j in range(2, i):
        if i % j == 0:
            break
