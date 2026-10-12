import requests

cases = [
    {"username": "admin", "password": "123456", "expect_code": 200},
    {"username": "", "password": "123456", "expect_code": 400},
    {"username": "admin", "password": "", "expect_code": 400},
]
i=0
for  case in cases:
    i=i+1
    payload = {"username": case["username"], "password": case["password"]}
    r = requests.post('https://httpbin.org/post', json=payload)

    if r.status_code == case["expect_code"]:
        print(f"用例 {i} 通过")
    else:
        print(f"用例 {i} 失败: 期望 {case['expect_code']}, 实际 {r.status_code}")
