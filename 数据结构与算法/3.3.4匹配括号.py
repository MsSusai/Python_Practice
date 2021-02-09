from pythonds.basic import Stack


def parChecker(symbolString):
    s = Stack()
    flag = True
    index = 0
    while index < len(symbolString) and flag:
        item = symbolString[index]
        if item in '([{':
            s.push(item)
        else:
            if s.isEmpty():
                flag = False
            else:
                top = s.pop()
                if not matches(top, item):
                    flag = False

        index += 1

    if flag and s.isEmpty():
        print("匹配成功！")
    else:
        print("匹配失败！")


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


parChecker("(())")
parChecker("((())))")
parChecker("{([])}")
parChecker("([())])")
