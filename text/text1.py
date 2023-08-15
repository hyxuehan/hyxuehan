# 建立1个包含10个字符的字符串，并根据键盘输入的数字n输出字符串中的第n个字符。
# 当n值超过字符串的索引时，自动转为输出字符串中的最后1个字符。

s='abcdefghijklmn'
i = int(input('请输入第几个字符：'))
l=list(s)
try:
    print(l[i-1])
except:
    print(l[len(l)-1])