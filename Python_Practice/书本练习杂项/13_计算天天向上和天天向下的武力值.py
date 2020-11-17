guolianxi = 1
guobulianxi = 1
for i in range(1, 366):
    guolianxi += guolianxi * 0.01

for j in range(1, 366):
    guobulianxi -= guobulianxi * 0.01
print("练功{}，不练功{}".format(guolianxi, guobulianxi))
