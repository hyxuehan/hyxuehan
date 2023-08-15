
import hashlib
import random



pwd = ''
char_list = [[97,122],[65,90],[48,57]]
for _ in range(16):
    rd_list = random.choice(char_list)
    rd_ascii = random.randint(*rd_list)
    char = chr(rd_ascii)
    pwd += char
md=hashlib.md5()
md.update(pwd.encode('utf-8'))
pwd_md5 = md.hexdigest()
print(pwd_md5)
print(pwd)