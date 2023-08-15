
import requests
url = 'http://apis.juhe.cn/springTravel/risk'
key = {'key': '0e786d4f1e34835951f7975bd2be0912'}
res = requests.post(url=url,data=key)
result = res.json()
print(result)