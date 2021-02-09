from pythonds.basic import Stack


def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ''
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    print(newString)


baseConverter(147, 2)
baseConverter(147, 8)
baseConverter(147, 10)
baseConverter(147, 16)
