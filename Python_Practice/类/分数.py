import math


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        newNum = self.num * other.den + self.den * other.num
        newDen = self.den * other.den
        common = math.gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)

    def __eq__(self, other):
        firstNum = self.num * other.den
        secondNum = self.den * other.num
        return firstNum == secondNum


num1 = Fraction(1, 2)
num2 = Fraction(5, 8)
num3 = num1 + num2
print(num3)
