from random import randint

list1 = [randint(10, 99) for i in range(10)]
list2 = [randint(10, 99) for i in range(10)]
list1.sort()
list2.sort(reverse=True)
list3 = list1 + list2
print(list3)
