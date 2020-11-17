from random import randint

guessNumber = randint(0, 9)
myGuess = eval(input("输入所猜的数："))
count = 1

while myGuess != guessNumber:
    if myGuess > guessNumber:
        print("遗憾，太大了")
    else:
        print("遗憾，太小了")
    myGuess = eval(input("输入所猜的数："))
    count += 1
else:
    print("预测{}次，你猜中了".format(count))
