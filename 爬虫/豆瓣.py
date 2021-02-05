import requests
from bs4 import BeautifulSoup


def getData(url):
    try:
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/88.0.4324.146 Safari/537.36'}  # 伪装头部信息
        r = requests.get(url, timeout=30, headers=head)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception:
        print("出现错误")
        return ''


def findData(websiteData, rankList, linkList):
    soup = BeautifulSoup(websiteData, 'html.parser')
    find = soup.find_all('div', class_='hd')  # 查找所有名字为div，属性为hd的标签
    for item in find:
        span = item.find('span', class_='title')  # 查找div标签中所有的span子标签
        text = span.string  # 获得span标签中的所有内容
        rankList.append(text)
        a = item.find('a')
        linkList.append(a['href'])


def printData(rankList, linkList):
    i = 1
    for item in rankList:
        print("第{}名：".format(i) + item, end='  ')
        print("观影链接：" + linkList[i - 1])
        i += 1


def main():
    url = 'https://movie.douban.com/top250?start='
    rankList = []
    linkList = []
    for i in range(10):  # 翻页
        print("正在采集第{}页信息...".format(i + 1))
        websiteData = getData(url + str(i * 25))  # 获取网页信息
        findData(websiteData, rankList, linkList)  # 找到电影信息
    printData(rankList, linkList)  # 打印排名


if __name__ == '__main__':
    main()
