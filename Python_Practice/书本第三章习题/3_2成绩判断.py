score = eval(input("输入成绩："))
if 0 <= score < 60:
    print("E")
elif 60 < score < 70:
    print("D")
elif 70 < score < 80:
    print("C")
elif 80 < score < 90:
    print("B")
elif 90 < score <= 100:
    print("A")
else:
    print("成绩有误")
