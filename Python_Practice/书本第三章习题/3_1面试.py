interview = []
while True:
    for i in range(3):
        interview.append(input("输入面试者数据：年龄，工作经验，所学专业："))
    if "计算机" in interview:
        if eval(interview[0]) < 25:
            print("获得面试机会")
        else:
            print("抱歉，您不符合面试要求")
    elif "电子" in interview:
        if eval(interview[1]) > 4:
            print("获得面试机会")
        else:
            print("抱歉，您不符合面试要求")
    elif "通信" in interview:
        print("获得面试机会")
    else:
        print("抱歉，您不符合面试要求")
