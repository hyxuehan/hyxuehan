import json
import requests
from io import BytesIO
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from jk_json import JkJson


class application(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.geometry("1000x800+300+100")
        self.title('驾考宝典')
        self.cw(*args,**kwargs)
        self.args = args


    def cw(self,*args,**kwargs):
        font = ['宋体', 14]
        if args[0].get('img'):
            ptoto = ImageTk.PhotoImage(Image.open(args[0].get('img')))
            self.lb_img = tk.Label(self, image=ptoto, width=200, height=200)
            self.lb_img.image = ptoto
            self.lb_img.pack()
        self.frame = tk.Frame(self)
        self.mess_q = tk.Message(self.frame, text='%d、%s' % (
            args[0].get('th'), args[0].get('qus')), font=font, width=600)
        self.mess_q.pack(anchor='w')

        self.v = tk.IntVar()
        self.result = tk.StringVar()
        self.foregroud = 'red'
        self.v.set(0)
        self.result.set('')

        self.rb1 = tk.Radiobutton(
            self.frame, text='A、'+args[0].get('1'), variable=self.v, value=1, font=font)
        self.rb1.pack(anchor='w')

        self.rb2 = tk.Radiobutton(
            self.frame, text='B、'+args[0].get('2'), variable=self.v, value=2, font=font)
        self.rb2.pack(anchor='w')

        self.rb3 = tk.Radiobutton(
            self.frame, text='C、'+args[0].get('3'), variable=self.v, value=3, font=font)
        if args[0].get('3'):
            self.rb3.pack(anchor='w')

        self.rb4 = tk.Radiobutton(
            self.frame, text='D、'+args[0].get('4'), variable=self.v, value=4, font=font)
        if args[0].get('4'):
            self.rb4.pack(anchor='w')
        
        self.bt = tk.Button(self.frame,text='提交',font=font,anchor='center',command=self.tj)
        self.bt1 = tk.Button(self.frame,text='下一题',font=font,anchor='center',command=self.xyt)
        
        self.bt.pack(side='left',expand=True)
        self.bt1.pack(side='right',expand=True)

        self.lb_result = tk.Label(
            self.frame, textvariable=self.result, foreground=self.foregroud, font=font)
        self.lb_result.pack()
        

        self.frame.pack(padx=100, pady=100, fill=tk.X)
        self.frame2 = tk.Frame(self)
        self.mess_js = tk.Message(
            self.frame2, text=args[0].get('explains'), font=font,width=800)
        # self.mess_js.pack()
        self.frame2.pack(padx=50,pady=50,fill = tk.X)

    def tj(self):
        if self.v.get() ==0:
            messagebox.showinfo(message='请先选择!')
        elif self.v.get() == int(self.args[0].get('answer')):
            self.result.set('回答正确!')
            self.mess_js.pack()
            self.foregroud='green'
        else:
            self.result.set('回答错误!')
            self.mess_js.pack()
            self.foregroud='#ffffff'

    def xyt(self):
        self.destroy()
        
# app = application()

# app.mainloop()

s = ''
with open('./1.txt', mode='r', encoding='utf-8') as f:
    s = f.read()
    f.close()
s = json.loads(s).get('result')
th = 1
# for i in s:
#     if i.get('url'):
#         response = requests.get(i.get('url'))
#         response = response.content
#         BytesIOobj = BytesIO()
#         BytesIOobj.write(response)

#     else:
#         BytesIOobj = None
#     params = {
#         'img' : BytesIOobj,
#         'qus': i.get('question'),
#         'th':th,
#         '1':i.get('item1'),
#         '2':i.get('item2'),
#         '3': i.get('item3'),
#         '4': i.get('item4'),
#         'answer':i.get('answer'),
#         'explains': i.get('explains')
#     }
#     th += 1
#     app = application(params)
#     app.mainloop()
jkbd = JkJson(th=3)
print(jkbd.id,jkbd.answer,jkbd.item,jkbd.question,jkbd.url)


#     print(str(th) + '、' + i.get('question'))
#     xz = ['A', 'B', 'C', 'D']
#     xznum = 0
#     for k, v in i.items():
#         if k[0:4] == 'item' and v:
#             print(xz[xznum]+'、' + v)
#             xznum += 1
#     answer = ''
#     while not answer:
#         answer = input('请回答：').upper()
#     if xz[int(i.get('answer'))-1] == answer:
#         print('回答正确')
#     else:
#         print('回答错误')
#         print('正确答案：'+xz[int(i.get('answer'))-1])
#         print('解释：' + i.get('explains'))
#     th += 1
#     input('按回车进入下一题！')
#     print('-'*50)
