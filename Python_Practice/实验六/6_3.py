lst_fib = [1, 1]
for i in range(28):
    lst_fib.append(lst_fib[i] + lst_fib[i + 1])

print(lst_fib)
print(len(lst_fib))