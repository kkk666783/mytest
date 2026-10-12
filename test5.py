import requests
  
#params = {"name":"张三","age":20}
#r = requests.get("https://httpbin.org/get",params=params)
#print(r.status_code)
#print(r.json()["args"])
#if r.status_code == 200:
#    print("成功")



#url = "https://httpbin.org/post"
#data ={"username": "testuser", "password": "123456"}
#r = requests.post(url,json=data)
#print(r.json()["json"])
#print(r.headers["Content-Type"])



#headers = {"Authorization": "Bearer abc123token"}
#r = requests.get("https://httpbin.org/get",headers=headers)
#a = r.json()["headers"]["Authorization"]
#print(a)
#print(a == "Bearer abc123token")


def test_create_post():
    url = "https://httpbin.org/post"
    data ={"title": "测试文章", "body": "内容", "userId": 1}
    r = requests.post(url,json=data)
    t = r.json()
    try :
        assert r.status_code == 200,f"状态码错误: {r.status_code}"
        assert t['json']["title"] == "测试文章", "title 不匹配"
        assert t['json']["userId"] == 1,"userId 不匹配"
        assert 'application/json' in r.headers['Content-Type'],"Content-Type 错误"
        print("测试通过")
    except AssertionError as e:
        print(f"测试失败：{e}")
test_create_post()
