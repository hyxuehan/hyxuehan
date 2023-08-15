import requests
from bs4 import BeautifulSoup as bf
from urllib.request import urlopen
from urllib.request import urlretrieve
html = urlopen('https://www.baidu.com/')
res = bytes.decode(html.read())
# result = requests.get(url=url)
# res = result.text
obj = bf(html.read(), 'html.parser')
with open('./pachong1.html', 'w', encoding='utf-8') as f:
    f.write(res)
    f.close()
# title = obj.head.title
# print(title,type(title))
print("爬虫结束")


# 导入urlopen函数
# 导入BeautifulSoup
# 请求获取HTML
html = urlopen("https://www.baidu.com/")
# 用BeautifulSoup解析html
obj = bf(html.read(), 'html.parser')
# 从标签head、title里提取标题
title = obj.head.title
with open('./pachong1.html', 'w', encoding='utf-8') as f:
    f.write(bytes.decode(html.read()))
    f.close()
# 打印标题
print(html.read().decode('utf-8'))
