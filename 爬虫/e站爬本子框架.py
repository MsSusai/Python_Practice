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
        print("出现错误")
        return ''


def findEveryJpgUrl(webData, mangaList):
    soup = BeautifulSoup(webData, 'html.parser')
    gdtms = soup.find_all('div', class_='gdtm')
    for gdtm in gdtms:
        a = gdtm.find('a')
        mangaList.append(a['href'])
    # print(mangaList)


def findMangaPage(webData, mangaList):
    soup = BeautifulSoup(webData, 'html.parser')
    div = soup.find('div', id='i3')
    img = div.find('img', id='img')
    mangaList.append(img['src'])


def downloadManga(PageList):
    global count
    for page in PageList:
        print("正在保存第{}张".format(count))
        try:
            head = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/88.0.4324.146 Safari/537.36'}
            mangaData = requests.get(page, timeout=30, headers=head)
            mangaData.raise_for_status()

            with open(str(count) + '.jpg', 'wb+') as manga:
                manga.write(mangaData.content)
            count += 1
        except Exception:
            print("第{}张保存失败".format(count))
            continue


count = 1

# for j in range(5):
mangaUrlList = []
mangaPageList = []
# print("正在下载第{}页".format(j + 1))
url = 'https://e-hentai.org/g/1860095/45feb95230/'

websiteData = getData(url)
findEveryJpgUrl(websiteData, mangaUrlList)

for singleUrl in mangaUrlList:
    webJpgData = getData(singleUrl)
    findMangaPage(webJpgData, mangaPageList)

downloadManga(mangaPageList)
