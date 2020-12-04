import random
import math

a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
values = [a, b, c]
values.sort()
print(values)
commonNumber1 = math.gcd(values[0], values[1])
commonNumber2 = math.gcd(commonNumber1, values[2])
leastNumber = (a * b * c) / commonNumber2
print("{}，{}，{}的最大公约数是{} 最小公倍数是{}"
      .format(a, b, c, commonNumber2, leastNumber))
