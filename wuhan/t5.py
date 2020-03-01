import json

dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
print(type(dic))  # <class 'dict'>

data = json.dumps(dic)
print("type", type(data))  # <class 'str'>
print("data", data)
with open('b.txt', 'w' ,encoding='utf-8') as f:
    json.dump(dic, f)
