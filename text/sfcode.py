
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# 身份证二要素验证_欢乐版 Python示例代码
if __name__ == '__main__':
    url = 'https://gwgp-pfwt2uhtvk6.n.bdcloudapi.com/idcard/validate_happy'
    params = {}
    params['name'] = '何勇'
    params['idcard'] = '342427198603260513'

    headers = {

        'Content-Type': 'application/json;charset=UTF-8',
        'X-Bce-Signature': 'a62c508947ea4379aa9a3ec86f5da117'
    }
    r = requests.request("POST", url=url, params=params, headers=headers)
    print(r.text)
