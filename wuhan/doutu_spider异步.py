import requests
import queue
from threading import Thread
from lxml import etree
import os
import re
import urllib
from urllib import request


class Producer(Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'Connection': 'keep-alive',
        'Host': 'www.doutula.com',
        'Upgrade-Insecure-Requests': '1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Cookie': '__cfduid=d4fa7d451b9b04bff923ac5671051baa91564992925; _ga=GA1.2.1344126117.1564992925; Hm_lvt_24b7d5cc1b26f24f256b6869b069278e=1565090453; UM_distinctid=170ec5b99db6db-056a565aa0ce4e-4313f6a-100200-170ec5b99dc4fd; _gid=GA1.2.84758893.1584513392; __gads=ID=4c024843125dd66d:T=1584513393:S=ALNI_MZ2dk-_K9SA44tsZ2BDhFrcNTxJmw; _agep=1584513393; _agfp=7d0b2856222f14e7bd1419b931a243ff; _agtk=c1a47918fe89fed0f6b6fd6845dfd1b2; CNZZDATA1256911977=414691280-1584510367-%7C1584521290; XSRF-TOKEN=eyJpdiI6IkJQOXFsU0NCWlY5SnFQdHdNSHJjQlE9PSIsInZhbHVlIjoiWGJyUnFXeUhTQU9OWStJTmp6YUdBYm5UVjh5WDZ5c1drTzgzXC9LUnlnQ1IrQm1tQ0hzcFhCNTdlR3U3RUxFR3IiLCJtYWMiOiJjMzIyOGRkYzNiYTdmMzA5ZWYyODU1MWQyZDhlODJmMDhkMGRkYWZkNzQwMWFiMjVjZjUzZmNiYjk2ZjdiYTMwIn0%3D; doutula_session=eyJpdiI6IjR0STlqUUlcL2c5VkJ2dEpvcUdGZWxRPT0iLCJ2YWx1ZSI6IlBRbENxOUhTS0hLVGlNNzVXUGFqT1FtZmI2NFlkTVRuR1RsM3NBSGZPUmRFbDhjS1hZdkxHS1BEeVpnakw3MVEiLCJtYWMiOiIzMGJiZTViODhlYzYxYjAxM2JlNDljMGE3YjAxNmU4ODliY2U2YTc4YzBjMGIxYTllYjcxYmY4ZThlMDZjNDFkIn0%3D'
    }

    def __init__(self, url_queue, img_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.url_queue = url_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.url_queue.empty():
                break
            url = self.url_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        rep = requests.get(url, headers=self.headers)
        lxml_parse = etree.HTML(rep.content)
        imgs = lxml_parse.xpath("//div[@class='col-sm-9 center-wrap']//img[@class!='gif']")
        for img in imgs:
            img_url = img.get('data-original')
            img_ext = os.path.splitext(img_url)[1]
            alt = img.get('alt')
            # 图片名字可能包含特殊字符，所以要提前处理
            alt = re.sub(r'[\?？\.。，#\$\r\n：:\b/]', '', alt)
            file_name = alt + img_ext
            self.img_queue.put((img_url, file_name))


class Consumer(Thread):
    def __init__(self, url_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.url_queue = url_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.url_queue.empty():
                break
            img_url,file_name = self.img_queue.get()
            # 解决出现urllib.error.HTTPError: HTTP Error 403: Forbidden的问题
            opener = request.build_opener()
            opener.addheaders = [('User-Agent',
                                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'),
                                 ('Connection', 'keep-alive'),
                                 ('Cache-Control', 'max-age=3600')]
            request.install_opener(opener)
            # 因为url可能有问题，会报错
            try:
                request.urlretrieve(img_url, 'images/' + file_name)
                print(file_name+'下载成功')
            except urllib.error.HTTPError:
                print('该图片找不到')


def main():
    url_queue = queue.Queue(100)
    img_queue = queue.Queue(1000)
    for i in range(1, 101):
        page_url = 'http://www.doutula.com/article/list/?page=%d' % i
        url_queue.put(page_url)
    for x in range(5):
        t = Producer(url_queue,img_queue)
        t.start()
    for y in range(5):
        t = Consumer(url_queue,img_queue)
        t.start()


if __name__ == '__main__':
    main()
