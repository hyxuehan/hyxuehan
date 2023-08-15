
# import turtle as p


# p.pensize(4)
# p.pencolor('red')
# p.fillcolor('pink')
# def ax():
#     p.begin_fill()
#     p.left(135)
#     p.forward(200)
#     p.circle(-100,180)
#     p.left(90)
#     p.circle(-100,180)
#     p.forward(200)
#     p.end_fill()
# ax()
# p.up()
# p.left(45)
# p.forward(30)
# p.left(90)
# p.forward(80)
# p.down()
# ax()
# p.done()

import turtle
import random

# turtle.Turtle().screen.delay(0)
# def love(x, y):         # 在(x,y)处画爱心lalala
#     lv = turtle.Turtle()
#     lv.hideturtle()
#     lv.up()
#     lv.goto(x, y)       # 定位到(x,y)

#     def curvemove():    # 画圆弧
#         for i in range(20):
#             lv.right(10)
#             lv.forward(2)

#     lv.color('red', 'pink')
#     lv.speed(10000000)
#     lv.pensize(1)
#     # 开始画爱心lalala
#     lv.down()
#     lv.begin_fill()
#     lv.left(140)
#     lv.forward(22)
#     curvemove()
#     lv.left(120)
#     curvemove()
#     lv.forward(22)
#     lv.write("YZ", font=("Arial", 12, "normal"), align="center")  # 写上表白的人的名字
#     lv.left(140)  # 画完复位
#     lv.end_fill()


# def tree(branchLen, t):
#     if branchLen > 5:       # 剩余树枝太少要结束递归
#         if branchLen < 20:  # 如果树枝剩余长度较短则变绿
#             t.color("green")
#             t.pensize(random.uniform((branchLen + 5) /
#                       4 - 2, (branchLen + 6) / 4 + 5))
#             t.down()
#             t.forward(branchLen)
#             love(t.xcor(), t.ycor())  # 传输现在turtle的坐标
#             t.up()
#             t.backward(branchLen)
#             t.color("brown")
#             return
#         t.pensize(random.uniform((branchLen + 5) /
#                   4 - 2, (branchLen + 6) / 4 + 5))
#         t.down()
#         t.forward(branchLen)
#         # 以下递归
#         ang = random.uniform(15, 45)
#         t.right(ang)
#         tree(branchLen - random.uniform(12, 16), t)  # 随机决定减小长度
#         t.left(2 * ang)
#         tree(branchLen - random.uniform(12, 16), t)  # 随机决定减小长度
#         t.right(ang)
#         t.up()
#         t.backward(branchLen)


# myWin = turtle.Screen()
# t = turtle.Turtle()
# t.hideturtle()
# t.speed(1000)
# t.left(90)
# t.up()
# t.backward(200)
# t.down()
# t.color("brown")
# t.pensize(32)
# t.forward(60)
# tree(100, t)
# myWin.exitonclick()

# 绘制玫瑰花并添加文字

# 设置画布大小
# turtle.screensize(canvwidth=None, canvheight=None, bg=None)
turtle.setup(width=0.6, height=0.6)
# 设置初始位置
turtle.penup()
turtle.left(90)
turtle.fd(200)
turtle.pendown()
turtle.right(90)



# 花蕊
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(10, 180)
turtle.circle(25, 110)
turtle.left(50)
turtle.circle(60, 45)
turtle.circle(20, 170)
turtle.right(24)
turtle.fd(30)
turtle.left(10)
turtle.circle(30, 110)
turtle.fd(20)
turtle.left(40)
turtle.circle(90, 70)
turtle.circle(30, 150)
turtle.right(30)
turtle.fd(15)
turtle.circle(80, 90)
turtle.left(15)
turtle.fd(45)
turtle.right(165)
turtle.fd(20)
turtle.left(155)
turtle.circle(150, 80)
turtle.left(50)
turtle.circle(150, 90)
turtle.end_fill()

# 花瓣1
turtle.left(150)
turtle.circle(-90, 70)
turtle.left(20)
turtle.circle(75, 105)
turtle.setheading(60)
turtle.circle(80, 98)
turtle.circle(-90, 40)

# 花瓣2
turtle.left(180)
turtle.circle(90, 40)
turtle.circle(-80, 98)
turtle.setheading(-83)

# 叶子1
turtle.fd(30)
turtle.left(90)
turtle.fd(25)
turtle.left(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(-80, 90)
turtle.right(90)
turtle.circle(-80, 90)
turtle.end_fill()
turtle.right(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(85)
turtle.left(90)
turtle.fd(80)

# 叶子2
turtle.right(90)
turtle.right(45)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(80, 90)
turtle.left(90)
turtle.circle(80, 90)
turtle.end_fill()
turtle.left(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(60)
turtle.right(90)
turtle.circle(200, 60)
# 输出文字
printer = turtle.Turtle()
printer.hideturtle()
printer.penup()
printer.back(200)
printer.write("赠给亲爱的 雅\n\n", align="right", font=("楷体", 16, "bold"))
printer.write("from 勇", align="center", font=("楷体", 12, "normal"))
turtle.done()
