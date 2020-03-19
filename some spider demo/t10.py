import re

# phone = 'wangzc946971@163.com27800334'
# ret = re.match('\w+@[a-z0-9]+\.com',phone)
# print(ret.group())
text = 'wzc price is 34.45,lsy price is 300'
r = re.compile("""
    \d+ #小数点前面
    \.? #小数点本身
    \d* #小数点后面
""", re.VERBOSE)
ret = re.findall(r, text)
print(ret)