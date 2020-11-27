dictionary = {'中国': 960.1, '美国': 850.4}
print(dictionary)

del dictionary['中国']
print(dictionary)

dictionary['中国'] = 960.1
print(dictionary)

area = dictionary.pop('意大利', '未找到国家')
print(area)

get = dictionary.get('巴西', '未知')
get1 = dictionary.get('中国')
print(get, get1)
