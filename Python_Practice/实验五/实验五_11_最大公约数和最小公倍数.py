from random import randint
import math

RND1 = randint(0, 100)
RND2 = randint(0, 100)
if RND1 < RND2:
    RND1, RND2 = RND2, RND1
commonNumber = math.gcd(RND1, RND2)
leastNumber = (RND1 * RND2) / commonNumber
print("{}和{}的最大公约数为{}，最小公倍数为{}".format(RND1, RND2, commonNumber, leastNumber))
