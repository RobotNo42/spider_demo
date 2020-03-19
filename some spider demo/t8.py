import requests

session = requests.session()
response = session.get('http://messiless.club')
print(response.cookies.get_dict())  