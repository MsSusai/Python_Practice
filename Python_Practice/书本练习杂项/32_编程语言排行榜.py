ieee = {'Python', 'C++', 'C', 'Java', 'C#'}
tiobe = {'Java', 'C', 'Python', 'C++', 'VB.NET'}

print("ieee2018排行榜是：")
print(ieee)

print("tiobe2018排行榜是：")
print(tiobe)

print("前五名上榜的语言有：")
print(ieee | tiobe)

print("在两个榜单同时进前五的有：")
print(ieee & tiobe)

print("只在ieee进前五的有：")
print(ieee - tiobe)

print("只在一个榜单进前五的有：")
print(ieee ^ tiobe)
