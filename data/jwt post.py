import requests
import json
import jsonpath

#生成token接口
url = "http://localhost:8000/login"
#python 字典--》json
jw = {
    "username":"admin",
    "password":"admin"
}
jwt = requests.post(url=url,json=jw)
#使用json包，打印json格式换行并且前面四个空格，通过ascii防止乱码
print(json.dumps(jwt.json(), indent=4, ensure_ascii=False))
#返回值十个列表，所以要加索引
#print(jsonpath.jsonpath(jwt.json(),"$..token")[0])


#登录jwt接口
urllogin = "http://localhost:8000/auth/hello"
#使用jsonpath来提取
token = "Bearer " + jsonpath.jsonpath(jwt.json(), "$..token")[0]
headers = {
    "Authorization":token
}
wt = requests.get(url=urllogin,headers=headers)
print(json.dumps(wt.json(), indent=4, ensure_ascii=False))


#上传文件接口
url = "http://httpbin.org/post"
#准备一个文件
file = open("C:\\Users\\EDZ\\Desktop\\ymw.txt","rb")
#参数
files ={
    "file":file
}
ww = requests.post(url=url,files=files)
#print(jwt.json())
print(json.dumps(ww.json(),indent=4,ensure_ascii=False))
