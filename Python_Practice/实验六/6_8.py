from random import shuffle

ls = ['A', 'B', 'C', 'D', 'E']
flag = 0
while flag == 0:
    for item in ls:
        if (ls[1] == 'D') + (ls[2] == 'B') == 1 and \
                (ls[1] == 'C') + (ls[3] == 'E') == 1 and \
                (ls[0] == 'E') + (ls[4] == 'A') == 1 and \
                (ls[2] == 'C') + (ls[3] == 'A') == 1 and \
                (ls[1] == 'B') + (ls[4] == 'D') == 1:
            print(ls)
            flag = 1
        else:
            shuffle(ls)
