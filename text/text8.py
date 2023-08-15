import sys
import os
import win32com.client
import urllib.request
# 用python下载百度文库的代码

# 一个用python下载百度文库的代码，需要的同志请修改，下面有提示 先去下载一个叫SWFToImage.dll的东西
# 再建立一个bat文件，并运行：
# 复制代码 代码如下:

# COPY SWFToImage.dll % windir %\system32
# regsvr32 % windir %\system32\SWFToImage.dll

# 复制代码 代码如下:

# 用python下载百度文库的代码，需要的同志请修改，下面有提示
# http://www.cnblogs.com/dearplain/
# code by plain

if __name__ == '__main__':
    # os.system('');
    os.chdir('E:\wk')  # 保存到哪个文件夹
    # SWFToImage = win32com.client.Dispatch("{479A1AAC-C148-40BB-9868-A9773DA66AF9}")
'''
allfile=os.listdir(".")
findrecord=0
for file in allfile:
if file==".record":
record=open(file,'rw')
findrecord=1
break
if findrecord==0:
record=open('.record','w')
'''
# url="http://wenku.baidu.com/view/8d3ed840be1e650e52ea9938.html?from=rec&pos=1&weight=2&lastweight=2&count=5"
url="http://wenku.baidu.com/view/f2fe7a3987c24028915fc37a.html?from=related&hasrec=1"
# url就是你要下载的文档的地址
url = sys.argv[1]
if url.find("http://") != 0:
    print("error! the url is not correct")
    sys.exit()
print("downloading %s" % url)
try:
    urlReferer = url[url.index('http'):url.index('/v')]
    print(urlReferer)
# urlbody=url[url.index('/v')-1:]
    urlnum = url[url.index('ew/')+3:url.index('.htm')]
except ValueError:
    print("parse url error")
    sys.exit()
# print urlnum
wenku = 'wenku.baidu.com'
reurl = '/play/'
pagefrom = '?pn='
downnum = '&rn='
# try to get title and make dir
req = urllib.Request(url)
res = urllib.urlopen(req)
data = res.read()
try:
    sfrom = data.index('<title>')+len('<title>')
# print sfrom
    sbefore = sfrom+data[sfrom:].index('</title>')
# print sbefore
    title = data[sfrom:sbefore]
    title = title[:title.rindex('_')]
    print ('downloading '+title)
except ValueError:
    print ("get title error")
    sys.exit()
allfile = os.listdir(".")
if (title in allfile) == False:
    os.mkdir(title)
    os.chdir('./'+title)
# get the first swf
req = urllib.Request('http://wenku.baidu.com'+reurl +
                      urlnum+pagefrom+'1'+downnum+'1')
req.add_header("Referer", urlReferer)
res = urllib.urlopen(req)
data = res.read()
res.close()
head = data[0:45]
pagenum = 0
sfrom = head.index('":"')+len('":"')
sbefore = sfrom+head[sfrom:].index('"')
pagenum = int(head[sfrom:sbefore])
print ('pagenum:'+str(pagenum))
if pagenum <= 0 or pagenum > 2000:
    print ("error!!!pagenum<0 or pagenum>2000")
    sys.exit()
data = data[106:]

swf = open("1.pywenku", 'wb')
swf.write(data)
swf.close()
i = 1
SWFToImage.InputSWFFileName = "%d.pywenku" % i
SWFToImage.ImageOutputType = 1
SWFToImage.ImageWidth = 1048
SWFToImage.ImageHeight = 1478
SWFToImage.Execute_Begin()
SWFToImage.FrameIndex = 1
SWFToImage.Execute_GetImage()
SWFToImage.SaveToFile("%d.jpg" % i)
SWFToImage.Execute_End()
os.rename("%d.pywenku" % i, "%d.swf" % i)
allfile = os.listdir(".")
# 从第二页下到最后一页
for i in range(2, pagenum+1):

    if '%d.swf' % i in allfile:
        continue
    # not find in the dir mean
    req = urllib.Request('http://wenku.baidu.com'+reurl +
                        urlnum+pagefrom+str(i)+downnum+'1')
    res = urllib.urlopen(req)
    data = res.read()
    data = data[106:]
    swf = open("%d.pywenku" % i, 'wb')
    swf.write(data)
    swf.close()
    SWFToImage.InputSWFFileName = "%d.pywenku" % i
    SWFToImage.ImageOutputType = 1
    SWFToImage.Execute_Begin()
    SWFToImage.FrameIndex = 1
    SWFToImage.Execute_GetImage()
    SWFToImage.SaveToFile("%d.jpg" % i)
    SWFToImage.Execute_End()
    os.rename("%d.pywenku" % i, "%d.swf" % i)
    res.close()
    print ('task complete')
