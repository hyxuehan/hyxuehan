# 编程程序，从键盘任意输入1个4位数，将该数字中的每位数与7相乘，
# 然后取乘积结果的个位数对该数字进行替换，最后得到1个新的4位数。
while True:
    a= input('请输入一个四位数：')
    if len(a) ==4:
        a1=0
        for i in range(4):
            a1=a1+(int(a[i])*7%10)*(10**(3-i))
        print(a1)
        break
    else:
        print('输入有误，请重新输入')