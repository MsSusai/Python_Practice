dic_class = {"托班": ["聪聪班", "伶伶班", "楠楠班"],
             "小班": ["小一班", "小二班"],
             "中班": ["中一班", "中二班"],
             "大班": ["大一班", "大二班"]}
dic_number = {"聪聪班": 26, "伶伶班": 23, "楠楠班": 25,
              "小一班": 32, "小二班": 31,
              "中一班": 33, "中二班": 34,
              "大一班": 32, "大二班": 33}
dic_total = {}
total = 0

for k, v in dic_class.items():
    for key, value in dic_number.items():
        if key in v:
            dic_total[k] = dic_total.get(k, 0) + value

for key, value in dic_total.items():
    total += value
    print(key + ":" + "{}人".format(value))
print("全园:{}人".format(total))
