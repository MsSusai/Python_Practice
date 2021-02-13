from turtle import *


def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t)
        t.left(40)
        tree(branchLen - 10, t)
        t.right(20)
        t.backward(branchLen)


t = Turtle()
win = t.getscreen()
t.left(90)
t.speed(1000)
t.up()
t.backward(300)
t.down()
tree(110, t)
t.exitonclick()
