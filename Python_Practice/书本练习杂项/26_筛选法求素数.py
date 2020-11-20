primes = [1] * 300
primes[0:2] = [0, 0]
count = 0
for i in range(2, len(primes)):
    if primes[i] == 1:
        for j in range(i + 1, len(primes)):
            if primes[j] != 0 and j % i == 0:
                primes[j] = 0
print("300以内的素数是：")
for i in range(len(primes)):
    if primes[i] != 0:
        count += 1
        print(i, end=' ')
        if count == 5:
            print()
            count = 0
