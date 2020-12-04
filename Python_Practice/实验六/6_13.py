string = input("输入一段英文：")
string = string.lower()
print(string)
char = []
for item in string:
    if item not in char and item != ' ':
        char.append(item)
char.sort()
print(char)
