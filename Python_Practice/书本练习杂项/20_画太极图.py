from turtle import *

color('black', 'black')

begin_fill()

circle(-50, 180)

circle(50, 180)

circle(100, 180)

pu()

left(90)

fd(40)

right(90)

circle(10)

end_fill()

color('black', 'white')

left(90)

fd(100)

pd()

right(90)

begin_fill()

circle(10)

end_fill()

pu()

home()

pd()

circle(-100, -180)

hideturtle()
