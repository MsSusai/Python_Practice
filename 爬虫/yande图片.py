# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/4/29  20:13 
# 名称：yande图片.PY
# 工具：PyCharm
import requests
from bs4 import BeautifulSoup


def getData(url):
    try:
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/88.0.4324.146 Safari/537.36'}
        r = requests.get(url, timeout=30, headers=head)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception:
        print("请求网页时出现错误")
        return ''


def getImgPage():
    pass


def getImgData():
    pass


def downloadImg():
    pass


if __name__ == '__main__':
    count = 1
    imgPageList = []
    imgDataList = []

    url = input("输入yande.re站的具体网址：")
    webData = getData(url)
    getImgPage()

    for imgUrl in imgPageList:
        imgData = getData(imgUrl)
        getImgData()

    downloadImg()
