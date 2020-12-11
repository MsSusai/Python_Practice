user = {"john": 123, "marry": 111, "tommy": 123456}
account = input("请输入用户名：")
password = eval(input("请输入密码："))

if account in user:
    if password == user[account]:
        print("登陆成功")
    else:
        print("密码错误")
else:
    print("账户错误")
