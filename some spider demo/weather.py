import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar
from pyecharts import options as opts
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}


All_Data = []


def parse(url):
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    total = soup.find(name='div', attrs={'class': 'conMidtab'})
    citys = total.find_all('table')
    for city in citys:
        trs = city.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            if index == 0:
                city_td = tds[1]
            else:
                city_td = tds[0]
            min_temp_td = tds[-2]
            city = list(city_td.stripped_strings)[0]
            min_temp = list(min_temp_td.stripped_strings)[0]
            All_Data.append({'city': city, 'min_temp': int(min_temp)})


def main():
    urls = {'http://www.weather.com.cn/textFC/hb.shtml',
            'http://www.weather.com.cn/textFC/db.shtml',
            'http://www.weather.com.cn/textFC/hd.shtml',
            'http://www.weather.com.cn/textFC/hz.shtml',
            'http://www.weather.com.cn/textFC/hn.shtml',
            'http://www.weather.com.cn/textFC/xb.shtml',
            'http://www.weather.com.cn/textFC/xn.shtml',
            'http://www.weather.com.cn/textFC/gat.shtml'
            }
    for url in urls:
        parse(url)
    All_Data.sort(key=lambda x: x['min_temp'])
    data = All_Data[-10:]
    city = list(map(lambda x: x['city'], data))
    max_temper = list(map(lambda x: x['min_temp'], data))
    c = (
        Bar()
        .add_xaxis(city)
        .add_yaxis("各地城市", max_temper, category_gap="40%")
        .set_global_opts(title_opts=opts.TitleOpts(title="最高气温的10个城市"))
    )
    Bar.render(c, 'max.html')



if __name__ == '__main__':
    main()