#  coding:utf-8
#  有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
num=0
for i in [1,2,3,4]:
    for j in [1,2,3,4]:
        if i != j:
            for k in [1,2,3,4]:
                if i != k and j != k:
                    print(f'{i}{j}{k}')
                    num += 1
print(f'共有{num}个数')
