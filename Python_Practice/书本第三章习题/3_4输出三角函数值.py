import math

for i in range(0, 91, 5):
    print(i, end=' ')
    print(math.sin(math.radians(i)), end=' ')
    print(math.cos(math.radians(i)))
