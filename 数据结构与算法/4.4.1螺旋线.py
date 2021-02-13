from turtle import *

t = Turtle()
win = t.getscreen()


def drawSpiral(t, lineLen):
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(t, lineLen - 5)


drawSpiral(t, 100)
win.exitonclick()
