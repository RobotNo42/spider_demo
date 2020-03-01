import requests
from bs4 import BeautifulSoup


def parse():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    r = requests.get('https://robotno42.github.io', headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    b = soup.find_all('article', attrs={'class': 'post post-type-normal'})
    for i in b:
        i1 = i.find_all('a', attrs={'class', 'post-title-link'})[0].strings
        print(list(i1)[0])


if __name__ == '__main__':
    parse()