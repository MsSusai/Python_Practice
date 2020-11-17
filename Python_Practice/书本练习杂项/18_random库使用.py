import random

money = 10
maxMoney = money
count = 0
while money > 0:
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    if num1 + num2 == 7:
        money += 4
        if money > maxMoney:
            maxMoney = money
    else:
        money -= 1
    print(money,end=' ')
print("\nmaxMoney=",maxMoney)
