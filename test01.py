import requests
url = "http://www.baidu.com"
params={"id":"1001,1002","key":"北京"}
r = requests.get(url,params=params)

print(r.url)
print(r.status_code)
print(r.text)
