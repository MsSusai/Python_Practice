from bs4 import BeautifulSoup
import requests

url = 'http://www.baidu.com'


def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}  # 伪装Mozilla/5.0浏览器访问
        # wd = {'wd': 'python'}
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        soup = BeautifulSoup(demo, 'html.parser')
        print(soup.title)
    except:
        print('产生异常')


getHTMLText(url)
