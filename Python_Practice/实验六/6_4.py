lst_busstop = ['龙江新城市', '阳光广场', '汉江路', '嫩江路',
               '清凉山公园', '拉萨路', '五台山', '莫愁路']
start = input("请输入起始站：")
end = input("请输入终止站：")
count = lst_busstop.index(end) - lst_busstop.index(start)
if count >= 0:
    print('从' + start + '站前往' + end + '站需要{}站路'.format(count))
else:
    print("您需要乘坐反方向线路,需要乘坐{}站".format(abs(count)))
