mates = ['木合塔尔', '朱兆轩']
print(mates)
mates.append('刘浩然')
print(mates)
mates.insert(3, '李金洺')
print(mates)
print('liu' in mates)
print(mates.count('刘浩然'))
matesCopy = mates.copy()
matesCopy.sort()
matesCopy.remove('刘浩然')
print(matesCopy)
print(mates[1:])
extend = ['刘浩然']
mates.extend(extend)
print(mates)
del matesCopy
