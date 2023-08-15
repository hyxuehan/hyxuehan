# 输入某年某月某日，判断这一天是这一年的第几天


y = int(input('请输入年：'))
while True:
    m = int(input('请输入月：'))
    if 1 <= m <= 12:
        break
    print('输入有误')
sfrn = False
if (y % 100 != 0 and y % 4 == 0) or (y % 400 == 0):
    sfrn = True
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if sfrn:
    day[1] = 29
while True:
    d = int(input('请输入日：'))
    if 1 <= d <= day[m-1]:
        break
    print('输入有误')
total = 0
for i in range(m-1):
    total = total + day[i]
total += d
print(f'{y}年{m}月{d}日是全年的第{total}天')
