def judge(password):
    judgeLevel = 0
    for char in password:
        if '0' <= char <= '9':
            judgeLevel += 1
            break
    for char in password:
        if 'a' <= char <= 'z':
            judgeLevel += 1
            break
    for char in password:
        if 'A' <= char <= 'Z':
            judgeLevel += 1
            break
    if len(password) >= 8:
        judgeLevel += 1
    return judgeLevel


password = input("请输入测试密码：")
level = judge(password)
print(password + "的密码强度为{}级".format(level))
