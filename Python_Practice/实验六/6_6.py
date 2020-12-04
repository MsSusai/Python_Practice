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
for i in range(len(lst_student)):
    if type(lst_student[i]) == type(lst_student[2]):
        if lst_student[i] > 19:
            print(lst_student[i - 2:i + 1])
