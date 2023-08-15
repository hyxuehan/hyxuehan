# encoding:utf-8

# 新华字典--聚合数据

import requests

url = 'http://v.juhe.cn/xhzd/query'
while True:
    word = input('请输入要查询的汉字:')
    if '\u4e00' <= word <= '\u9fff' and len(word) == 1:
        break
    print('请输入单个汉字!')

date = {
    'key': '055c896b4f6ec76aac2076915b018b79',
    'word': word
}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
response = requests.post(url=url, data=date, headers=headers)
dic = response.json()


dic1 = {
    "zi": "汉字",
    "py": "拼音",
    "wubi": "五笔",
    "pinyin": "读音",
    "bushou": "部首",
    "bihua": "笔划",
    "jijie": "简介",
    "xiangjie": "详解"
}


for k, v in dic.get('result').items():
    if k == 'id':
        continue
    try:
        print(dic1.get(k), ':\n', '  ' + v)
    except TypeError:
        print(dic1.get(k))
        for i in v:
            print('  ', i)
    finally:
        print('查询结束！')
