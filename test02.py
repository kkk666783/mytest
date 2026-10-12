import requests
url = "https://httpbin.org/post"
headers = {"Content-Type":"application/json"}
data = {
        "data" : [
                 {
                    "id":"100",
                    "d_name":"test",
                    "m_name":"tmaster"
                  }
                  ]
        }
r=requests.post(url,json=data,headers=headers)
 
print(r.json())
print(r.status_code)
