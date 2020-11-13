cny = input("请输入要兑换的人民币币值，以￥结束：")
cny = eval(cny[:-1])
usd = round(cny * 0.1456, 2)
print("{}元人民币可以兑换{}美元".format(cny, usd))
