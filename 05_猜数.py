import random

target = random.randint(1, 100)
print("已经产生一个1-100的数")

while True:
    guess = eval(input())
    if guess > target:
        print("太大了")
    elif guess < target:
        print("太小了")
    else:
        print("猜中了")
        break
