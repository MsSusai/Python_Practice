import requests

url = 'http://www.baidu.com/s'


def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}  # 伪装Mozilla/5.0浏览器访问
        wd = {'wd': 'python'}
        r = requests.get(url, timeout=30, headers=kv, params=wd)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.request.url)
    except:
        print('产生异常')


getHTMLText(url)
