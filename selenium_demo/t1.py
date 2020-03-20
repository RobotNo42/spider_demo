import requests
from lxml import etree


rep = requests.get('https://robotno42.github.io/')
r = etree.HTML(rep.text)
content = r.xpath("//div[@class='content']")[0]
print(content.get('id'))