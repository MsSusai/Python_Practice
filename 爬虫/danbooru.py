# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2021/6/3  21:10 
# 名称：danbooru.PY
# 工具：PyCharm
import requests
from bs4 import BeautifulSoup
import re


def getData(url):
    try:
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/88.0.4324.146 Safari/537.36'
        }
        r = requests.get(url, head=head, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception:
        print('网页请求出现错误')
        return ''


def getEveryJpgUrl(webData, jpgUrlList):
    soup = BeautifulSoup(webData, 'html.parser')
    a = soup.find_all('a', {'href': re.compile(r'/posts/[0-9]+')})
    print(a)


def getEveryJpg(webData, jpgList):
    pass


def downloadJpg():
    pass


if __name__ == '__main__':
    url = 'http://danbooru.me/posts?tags=dise'
    jpgUrlList = []
    jpgList = []

    data = getData(url)
    getEveryJpgUrl(data, jpgUrlList)
