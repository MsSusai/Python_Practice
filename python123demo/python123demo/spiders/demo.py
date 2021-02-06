import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['python123.io']
    start_urls = ['https://python123.io/ws/demo.html']

    def parse(self, response):
        fileName = response.url.split('/')[-1]
        with open(fileName, 'wb') as f:
            f.write(response.body)
        self.log('已保存文件%s' % fileName)
        pass
