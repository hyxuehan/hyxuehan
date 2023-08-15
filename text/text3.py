# 一个人赶着鸭子去每个村庄卖，每经过一个村子卖去所赶鸭子的一半又一只。
# 这样他经过了七个村子后还剩两只鸭子，问他出发时共赶多少只鸭子？



total = 2
i = 1
def func():
    global i,total
    if i >7:
        print(total)
        return
    total=(total+1)*2
    i +=1
    func()
func()

import math
print ((2*math.sin(math.pi*85/180))/(1+math.e**2))

import math
x= float(input('请输入实数：'))
print(math.log((x+math.sqrt(1+x**2)),math.e)/2)
