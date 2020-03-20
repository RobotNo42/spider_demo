from selenium import webdriver
from lxml import etree


class LaGouSpider(object):
    driver_path = r'D:\chromedriver\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

    def run(self):
        self.driver.get(self.url)
        print(self.driver.page_source)


if __name__ == '__main__':
    spider = LaGouSpider()
    spider.run()