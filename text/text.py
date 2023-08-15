# import turtle
# t = turtle.Pen()
# t.color("red")
# t.circle(50)

# 1、九九乘法表
# for i in range(1,10):
#     for j in range(1,10):
#         if j <= i:
#             print('{}*{}={}'.format(j,i,i*j),end="\t")
#     print()

# 2、输入成绩
# while True:
#     a = float(input("请输入成绩:"))
#     if a < 0 or a > 100 or a % 1 != 0:
#         print("你输入的成绩有误，请重新输入")
#     elif 90 <= a <= 100:
#         print("A")
#         break
#     elif 80 <= a < 90:
#         print("B")
#         break
#     elif 70 <= a < 80:
#         print("C")
#         break
#     elif 60 <= a < 70:
#         print("D")
#         break
#     elif a < 60:
#         print("E")
#         break

# 3、小明单位发了100元的购物卡，小明到超市买三类洗化用品：洗发水（15元）、香皂（2元）、牙刷（5元）。要把100元正好花掉，可有哪些购买组合？
# for i in range(7):
#     for j in range(51):
#         for k in range(21):
#             if 15*i+2*j+5*k == 100:
#                 print("可以买洗发不{}，香皂{}，牙刷{}".format(i, j, k))

# 4、首先由计算机产生一个[1,100]之间的随机整数，然后由用户猜测所产生的随机数。
# 根据用户猜测的情况给出不同提示，如猜测的数大于产生的数，则显示“High”，小于则显示“Low”，
# 等于则显示“You won !”，游戏结束。用户最多可以猜7次，如果7次均未猜中，则显示“You lost !”，
# 并给出正确答案，游戏结束。游戏结束后，询问用户是否继续游戏，选择“Y”则开始一轮新的猜数游戏；选择“N”则退出游戏。
# import random
# t=True
# while t:
#     num = int(random.randint(1, 100))
#     i=1
#     kmax = 100
#     kmin = 1
#     while i<8:
#         a = int(input("请输入你猜的数字："))
#         if a < num:
#             print("{}到{}".format(a,kmax))
#             kmin = a
#             i+=1
#         elif a > num:
#             print("{}到{}".format(kmin,a))
#             kmax = a
#             i += 1
#         else:
#             print("You won I")
#             break
#     if i > 7 :
#         print("You lost !")
#         print("正确的是：{}".format(num))
#     b= str(input("是否继续游戏（Y/N）："))
#     if b =="N" or b =="n":
#         t = False

# class my_class(object):
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age

#     def new_method(self):
#         print('abc')

#     # def new_method(self):
#     #     new_varnew_var = self.new_method()

#     # def new_method(self):
#     #     self.new_method()


# obj = my_class('张三',18)
# obj1 = my_class('李四',20)
# print(obj.name)
# print(obj1.age)
# print(my_class.__dict__)
