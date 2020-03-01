from lxml import etree
import requests
import time

s = requests.session()

def douban_login():
    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'Referer': 'https://accounts.douban.com/passport/login',

    }
    data ={
        'name': '18368723168',
        'password': '946971',
        'remember': 'false',

    }
    s.post(url=login_url, headers=headers, data=data)


def parse_page(page):
    parse_url = "https://movie.douban.com/subject/27010768/reviews?start=" + str(page)
    headerer = {
        'Accept': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    }
    re = s.get(url=parse_url, headers=headerer)
    r1 = etree.HTML(re.content)
    r2 = r1.xpath('//*[@id="content"]/div/div[1]/div[1]//div//h2/a/text()')
    with open('test.txt','a+',encoding='utf8') as f:
        for i in r2:
            f.write(i+'\n')


if __name__ == '__main__':
    douban_login()
    for i in range(301):
        page = 20*i
        parse_page(page)
        time.sleep(3)





