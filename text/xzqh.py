import requests
import json

url = 'https://quhua.ipchaxun.com/api/areas/data'
name = ''
tel = '0550'
children = '4'
date ={
    'tel':tel,
    'children':children
}

reson = requests.get(url=url,params=date)
res = reson.json()
print(res,type(res))