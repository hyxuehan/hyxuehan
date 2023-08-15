# coding:utf-8
"""
新冠中高风险区查询--聚合数据
"""
from ast import Str
import requests
import json
url = 'http://apis.juhe.cn/springTravel/risk'
key = {'key': '0e786d4f1e34835951f7975bd2be0912'}
res = requests.post(url=url, data=key)
result = res.json()
result = result.get('result')
high_list = result.get('high_list')
middle_list = result.get('middle_list')
low_list = result.get('low_list')
def write(file,list):
    for i in list:
        for j in i.get('communitys'):
            str = i.get('province') + '   ' + \
                i.get('city') + '   ' + i.get('county') + '   ' + j + '\n'
            file.write(str)
with open('.\zgfx1.txt', mode='w', encoding='utf-8') as f:
    f.write('----------------以下是高风险区—------------------\n')
    write(f,high_list)
    f.write('----------------以下是中风险区—------------------\n')
    write(f,middle_list)
    f.write('----------------以下是低风险区—------------------\n')
    write(f,low_list)