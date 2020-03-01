import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}

total_list = {}


def parse(url):
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    total = soup.find(name='div', attrs={'class': 'conMidtab'})
    citys = total.find_all('table')
    for city in citys:
        trs = city.find_all('tr')[2:]
        for tr in trs:
            tds = tr.find_all('td')
            city_td = tds[0]
            city = list(city_td.strings)[1]
            print(city)


def main():
    url = 'http://www.weather.com.cn/textFC/hb.shtml'
    parse(url)


if __name__ == '__main__':
    main()