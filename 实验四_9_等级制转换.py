score = eval(input("输入成绩："))
if score < 60:
    print("不及格")
elif score < 70:
    print("及格")
elif score < 80:
    print("中")
elif score < 90:
    print("良")
else:
    print("优")
