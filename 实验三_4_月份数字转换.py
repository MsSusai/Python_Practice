month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
select = eval(input("请输入数字月份1~12："))
if 0 <= select <= 12:
    monthSelect = month[select - 1]
    print("{}月对应的缩写是：".format(select) + monthSelect)
else:
    print("输入月份错误！")
