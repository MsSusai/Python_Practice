count = 1
while True:
    if count % 1 == 0 and count % 2 == 1 and count % 3 == 0 and count % 4 == 1 and count % 5 == 1 and count % 6 == 3 and count % 7 == 0 and count % 8 == 1 and count % 9 == 0:
        break
    else:
        count += 1
print("盒子里至少有{}个糖果".format(count))
