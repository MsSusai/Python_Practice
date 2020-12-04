goodPerson = ['甲', '乙', '丙', '丁']

for x in goodPerson:
    if (x != '甲') + (x == '丙') + (x == '丁') + (x != '丁') == 3:
        print(x)
