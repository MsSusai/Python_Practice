# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/5/6  21:46 
# 名称：超星学习通课件.PY
# 工具：PyCharm
import requests


def getData(url):
    try:
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/88.0.4324.146 Safari/537.36'}
        r = requests.get(url, timeout=30, headers=head)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.content
    except Exception:
        print("请求网页时出现错误")
        return ''


def downloadPPT(pptUrlList):
    count = 1
    for pptUrl in pptUrlList:
        print("正在保存第{}张".format(count))
        try:
            ppt = getData(pptUrl)
            with open(str(count) + '.png', 'wb+') as f:
                f.write(ppt)
            count += 1
        except Exception:
            print("第{}张保存失败".format(count))
            count += 1
            continue


if __name__ == '__main__':
    url = 'https://s3.ananas.chaoxing.com/doc/3e/ad/8d/776d85eef4a0b86c79793efc1b014c31/thumb/'
    urlList = []
    page = input("输入有几页：")
    for i in range(1, int(page) + 1):
        urlList.append(url + str(i) + '.png')
    downloadPPT(urlList)
