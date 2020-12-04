# 判断n是否为素数
def isprime(n):
    for j in range(2, n):
        if n % j == 0:
            return False
    else:
        return True


# 找出2-100以内的所有素数
prime = []
for i in range(2, 100 + 1):
    if isprime(i):
        prime.append(i)
print(prime)

# 找出2-100以内的孪生素数
for i in range(len(prime)):
    if i != len(prime) - 1:
        if prime[i + 1] - prime[i] == 2:
            print(prime[i], prime[i + 1])
