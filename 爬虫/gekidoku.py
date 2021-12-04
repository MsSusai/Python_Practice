# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/12/4  23:24 
# 名称：gekidoku.PY
# 工具：PyCharm
import requests

url = "https://s3.3hentai.net/d475917/"
urlList = []
for i in range(1, 17 + 1):
    urlList.append(url + str(i) + ".jpg")
for j in range(17):
    print("正在下载第{}张".format(j + 1))
    response = requests.get(urlList[j])
    with open(str(j + 1) + '.jpg', 'wb+') as img:
        img.write(response.content)
