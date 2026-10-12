import requests
from requests.exceptions import RequestException
class APIClient:
    def __init__(self,base_url,token):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
             'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'

            })
    def get(self,path,params=None):
        try:
            r = self.session.get(
                f'{self.base_url}{path}',
                params=params,
                timeout=10
            )
            r.raise_for_status()
            return r.json()
        except RequestException as e:
            print(f"请求出错: {e}")
            return None
client = APIClient('https://httpbin.org', 'mytoken')
result = client.get('/get', {'k': 'v'})
print(result['args'])                # {'k': 'v'}
print(result['headers']['Authorization'])  # Bearer mytoken
