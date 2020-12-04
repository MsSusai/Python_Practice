lst_student = ['001', '李梅', 19, '002', '刘祥', 20, '003', '张武', 18]
# 1.
lst_student.append('004')
lst_student.append('刘宁')
lst_student.append(20)
lst_student.append('006')
lst_student.append('梁峰')
lst_student.append(19)
# 2.
lst_student.insert(12, '005')
lst_student.insert(13, '林歌')
lst_student.insert(14, 20)
# print(lst_student)

# 3.
print(lst_student[6:9])

# 4.
print(lst_student[1::3])

# 5.
year = 0
# print(type(lst_student[2]))
for item in lst_student:
    if type(item) == type(lst_student[2]):
        year += item
print("平均年龄为{}".format(year / 6))
