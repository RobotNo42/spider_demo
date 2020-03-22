from selenium import webdriver
from lxml import etree


job_list = []
class LaGouSpider(object):
    driver_path = r'D:\chromedriver\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

    def run(self):
        self.driver.get(self.url)
        self.parse_source_list(self.driver.page_source)

    def parse_source_list(self, source):
        page = etree.HTML(source)
        urls = page.xpath("//ul[@class='item_con_list']//a[@class='position_link']/@href")
        for u in urls:
            self.request_detail_page(u)

    def request_detail_page(self,url):
        self.driver.get(url)
        self.parse_page(self.driver.page_source)

    def parse_page(self,page):
        t = etree.HTML(page)
        name = t.xpath("/html/body/div[6]/div/div[1]/div/h1/text()")[0].strip()
        money = t.xpath("//dd[@class='job_request']/h3/span[1]/text()")[0].strip()
        job_list.append({
            'job_name': name,
            'money': money
        })


if __name__ == '__main__':
    spider = LaGouSpider()
    spider.run()
    print(job_list)