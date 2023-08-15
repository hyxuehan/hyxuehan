import requests
import json
url = 'http://v.juhe.cn/jztk/query'
key = '2a013b4b99a30b61f764feb442c62aa9'
subject = 1 # 1：科目1；4：科目4
model = 'c1'   #  驾照类型，可选择参数为：c1,c2,a1,a2,b1,b2；当subject=4时可省略
testType = 'rand'  # 测试类型，rand：随机测试（随机100个题目），order：顺序测试（所选科目全部题目）

Header = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'key':key,
    'subject':subject,
    'model':model,
    'testType':testType
}

respone = requests.request(method='post',url=url,data=data,headers=Header)
res = respone.text
r = json.loads(res).get('result')
with open('./1.txt',mode='w',encoding='utf-8') as f:
    f.write(res)
    f.close()
# print(res)
