# coding:utf-8
# def fib(n):
#     return 1 if n <= 2 else fib(n-1)+fib(n-2)


# for i in range(1, 100):
#     print(fib(i), end='  ')
#     if i % 10 == 0:
#         print()
import time
fib1,fib = 1,1
print(fib1,fib,end='  ')
for i in range(0,98):
    fib1,fib = fib,fib1+fib
    print(fib,end='  ')
    if i > 0 and (i-2) % 5 == 0:
        print()
        time.sleep(1)