import requests
import json
from lxml import etree
url = 'http://www.baidu.com'

respone = requests.get(url=url)
res = respone.text
html = etree.parse('./html.html',etree.HTMLParser())
result = html.xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table//td/text()')
print(res)
print(result)
