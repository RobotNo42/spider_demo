from selenium import webdriver
from lxml import etree
import time

job_list = []


class LaGouSpider(object):
    driver_path = r'D:\chromedriver\chromedriver.exe'

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

    # 因为selenium没有判断元素存不存在的方法，所以我们自己写一个方法，有可能会用得到
    def isElementExist(self, element):
        flag = True
        browser = self.driver
        try:
            browser.find_element_by_xpath(element)
            return flag
        except Exception:
            flag = False
            return flag

    def run(self):
        self.driver.get(self.url)
        n = 1
        while True:
            source = self.driver.page_source
            self.parse_source_list(source)
            # 因为第一次会弹广告，所以要判断广告存不存在
            if n == 1:
                self.driver.find_element_by_xpath("//div[@class='body-btn']").click()
                n = 0
            try:
                next_bt = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
                if "pager_next_disabled" in next_bt.get_attribute("class"):
                    print('last')
                else:
                    next_bt.click()
                    # 一定要加等待时间，不然页面还没加载出来，爬的又是第一页的数据
                    time.sleep(2)
            except:
                print('debug')
            print("=="*100)

    def parse_source_list(self, source):
        page = etree.HTML(source)
        urls = page.xpath("//ul[@class='item_con_list']//a[@class='position_link']/@href")
        for u in urls:
            self.request_detail_page(u)

    def request_detail_page(self,url):
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.parse_page(self.driver.page_source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_page(self,page):
        t = etree.HTML(page)
        name = t.xpath("//div[@class='job-name']//h1/text()")[0].strip()
        money = t.xpath("//dd[@class='job_request']/h3/span[1]/text()")[0].strip()
        address = t.xpath("//dd[@class='job_request']/h3/span[2]/text()")[0].strip()
        work_years = t.xpath("//dd[@class='job_request']/h3/span[3]/text()")[0].strip()
        new_job = {
            'job_name': name,
            'money': money,
            'address': address,
            'work_years': work_years

        }
        job_list.append(new_job)
        print(new_job)


if __name__ == '__main__':
    spider = LaGouSpider()
    spider.run()
    print(job_list)