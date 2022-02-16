import requests
import json

url = 'http://localhost:8080/EasyBuy/Login'
ym = 'loginName=admin&password=123456&action=login'
#my = requests.request('POST',url=url,params=ym)
my = requests.post(url=url,params=ym)
print(my.text)
#print(json.dumps(my.json(),indent=4,ensure_ascii=False))


