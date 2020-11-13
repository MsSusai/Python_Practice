usd = input("请输入要兑换的美元币值，以$结束：")
usd = eval(usd[:-1])
cny = round(usd * 6.868, 2)
print("{}美元可以兑换人民币{}元".format(usd, cny))
