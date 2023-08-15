# encoding:utf-8

# 汽车OBD故障码查询--聚合数据

import requests

error_code ={
    '10001':'错误的请求KEY',
    '10002':'该KEY无请求权限',
    '10003':'KEY过期',	
    '10004':'错误的OPENID',
    '10005':'应用未审核超时，请提交认证',
    '10007':'未知的请求源',
    '10008':'被禁止的IP',
    '10009':'被禁止的KEY',
    '10011':'当前IP请求超过限制',
    '10012':'请求超过次数限制',
    '10013':'测试KEY超过请求限制',
    '10014':'系统内部异常(调用充值类业务时，请务必联系客服或通过订单查询接口检测订单，避免造成损失',
    '10020':'接口维护',
    '10021':'接口停用'
}

code = input('请输入故障码:')

url = 'http://apis.juhe.cn/obdcode/query'
data = {
    'key': '57667db89127ef00f6a86ffda9ce14c4',
    'code':code
}
headers = {'Content-Type':'application/x-www-form-urlencoded'}
response = requests.post(url=url,data=data,headers=headers)
res = response.json()


if res.get('reason').strip() != 'success':
    print('请求失败，错误原因：',error_code.get(str(res.get('error_code')).strip()))
    exit()
if res.get('result') is None:
    print('未查询到此故障码')
    exit()
    
result = res.get('result')

dic = {
    'sycx':'适用车型:',
    'zwhy':'中文含义:',
    'ywhy':'英文含义:',
    'gzfw':'故障范围:',
    'ms':'故障描述:'
}
for k,v in result.items():
    if dic.get(k) is not None:
        print('\033[0;31m'+dic.get(k)+'\033[0m',v)

