from random import randint

lst_who = ['小马', '小羊', '小鹿']
lst_what = ['看电影', '听故事', '吃晚饭']
lst_where = ['草地上', '电影院', '家里']
who = lst_who[randint(0, 2)]
what = lst_what[randint(0, 2)]
where = lst_where[randint(0, 2)]

print(who + '在' + where + what)
