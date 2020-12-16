dic_city = {"张三风": ["北京", "成都"],
            "李莫愁": ["上海", "广州", "兰州"],
            "慕容复": ["太原", "西安", "济南", "上海"]}
count = 0
people = []
for key, value in dic_city.items():
    print(key + "去过" + "{}个城市".format(len(value)))
    if "上海" in value:
        count += 1
        people.append(key)
print("去过上海的有{}人，他们是".format(count), end="")
for item in people:
    print(item, end=" ")
