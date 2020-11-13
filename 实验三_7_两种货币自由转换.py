changeMoney = input("请输入要兑换的钱数，美元以$结束，人民币以￥结束：")

# 美元换人民币
if '$' in changeMoney:
    usd = eval(changeMoney[:-1])
    cny = round(usd * 6.868, 2)
    print("{}美元可以兑换人民币{}元".format(usd, cny))

# 人民币换美元
elif '￥' in changeMoney:
    cny = eval(changeMoney[:-1])
    usd = round(cny * 0.1456, 2)
    print("{}元人民币可以兑换{}美元".format(cny, usd))

else:
    print("输入有误！")
