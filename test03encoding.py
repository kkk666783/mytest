import requests
url = "http://www.baidu.com"
r = requests.get(url)
print(r.encoding)
r.encoding = "utf-8"
print(r.encoding)
print(r.text)
#一般返回的token\session相关信息都在其中获取响应信息头信息
print(r.headers)
