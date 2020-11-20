suspects = ['A', 'B', 'C', 'D']
for i in suspects:
    if 3 == (i != 'A') + (i == 'C') + (i == 'D') + (i != 'D'):
        print("小偷是{}".format(i))
        break
