from random import randint

set1 = {1, 3, 6, 4}
set2 = set()
set3 = {1, 4}
for i in range(20):
    set2.add(randint(1, 20))
print(set2)

print(set1)
set1.discard(6)
print(set1)
set1.add(8)
print(set1)

print(set1 | set3)
print(set1 & set3)
print(set1 - set3)
print(set1 ^ set3)
