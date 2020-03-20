from selenium import webdriver
from selenium.webdriver import ActionChains
driver_path = r'D:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')
driver.save_screenshot('k1.png')
inputTag = driver.find_element_by_id('kw')
submitTag = driver.find_element_by_id('su')
ac = ActionChains(driver)
ac.send_keys_to_element(inputTag, 'python')
ac.click(submitTag)
ac.perform()