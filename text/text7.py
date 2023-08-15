from turtle import rt


with open('text3.py',mode='rt',encoding='utf-8') as f:
    for line in f:
        print(line)
    res=f.read(1024)
    print(res)
    f.close()
