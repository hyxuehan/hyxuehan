# coding:utf-8
# 输入某年某月某日，判断这一天是这一年的第几天？
days = [0,31,28,31,30,31,30,31,31,30,31,30]
sum = 0
year = int(input('请输入年：'))
if (year%100 !=0 and year%4 == 0) or year%400 == 0:
    days[2] += 1
month = int(input('请输入月份:'))
day = int(input('请输入日:'))
for i in range(month):
    sum+=days[i]
sum+=day
print(f'今天是今年的第{sum}天')