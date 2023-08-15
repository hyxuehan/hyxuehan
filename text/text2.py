# 该函数可以输入任意多个数，函数返回输出所有输入参数的最大值、最小值和平均值
import numpy as py
l=[]
i = int(input("请输入个数："))
for j in range(1,i+1):
    k=int(input(f'请输入第{j}个数：'))
    l.append(k)
max =max(l)
min = min(l)
avr=py.mean(l)
sum=sum(l)
print(f'这{i}个数中，最大的是{max}，最小的是{min}，和是{sum},平均数是{avr}')
