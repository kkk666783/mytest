import requests
url = "http://www.baidu.com"
url_img = "https://www.baidu.com/img/bd_logo1.png?where=super"
r = requests.get(url_img)
#返回字典对象
#print(r.cookies)
#print(r.cookies['BDORZ'])
#字节码形式解析图片
print(r.content)
with open("./baidu.png","wb") as f:
    f.write(r.content)
