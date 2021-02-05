import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def fillRankList(rankList, html):
    soup = BeautifulSoup(html, 'html.parser')

    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):

            td = tr('td')
            print(td)
            rankList.append([td[4].string, td[1].string, td[2].string])
            print(rankList)


def printRankList(rankList, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    for i in range(num):
        university = rankList[i]
        print("{:^10}\t{:^6}\t{:^10}".format(university[0], university[1], university[2]))


rank = []
website = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
htmlText = getHTMLText(website)
fillRankList(rank, htmlText)
printRankList(rank, 20)
