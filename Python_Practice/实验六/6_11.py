lst_info = [['李玉', '男', 25], ['金忠', '男', 23],
            ['刘妍', '女', 21], ['莫心', '女', 24], ['沈冲', '男', 28]]
deleteName = input("输入要删除的员工姓名，输入0结束：")
while deleteName != '0':
    for i in range(5):
        if lst_info[i][0] == deleteName:
            del lst_info[i]
            print("删除成功！")
            print("目前员工名单为：", end='')
            print(lst_info)
            break
    else:
        print("删除失败，不存在公司员工")
    deleteName = input("输入要删除的员工姓名，输入0结束：")
