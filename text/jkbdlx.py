from jk_json import JkJson
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO


class myframe(tk.Tk):
    global th
    th = 0

    def __init__(self) -> None:
        super().__init__()
        # print(self.url)
        self.title('驾考宝典')
        self.withdraw()
        x = int((self.winfo_screenwidth()-1024)/2)
        y = int((self.winfo_screenheight()-800)/2)
        self.geometry('1024x800+{}+{}'.format(x, y))
        self.columnconfigure(0, weight=1)
        self.__widget()
        self.__bt_next_cd()
        self.deiconify()

    def __widget(self):
        global answer,exp
        answer = tk.StringVar()
        exp = tk.StringVar()
        self.lb_img = tk.Label(self, image='')
        self.lb_img.grid(row=0, column=0, padx=10, pady=10)

        self.lb_qus = tk.Label(self, text='')
        self.lb_qus.grid(row=1, column=0, padx=50, pady=10, sticky='w')

        self.rd_A = tk.Radiobutton(self, text='', variable=answer, value='1',command=self.__eq_answer)
        self.rd_A.deselect()
        self.rd_A.grid(row=2, column=0, padx=50, pady=5, sticky='w')

        self.rd_B = tk.Radiobutton(self, text='', variable=answer, value='2',command=self.__eq_answer)
        self.rd_B.deselect()
        self.rd_B.grid(row=3, column=0, padx=50, pady=5, sticky='w')

        self.rd_C = tk.Radiobutton(self, text='', variable=answer, value='3',command=self.__eq_answer)
        self.rd_C.deselect()
        self.rd_C.grid(row=4, column=0, padx=50, pady=5, sticky='w')

        self.rd_D = tk.Radiobutton(self, text='', variable=answer, value='4',command=self.__eq_answer)
        self.rd_D.deselect()
        self.rd_D.grid(row=5, column=0, padx=50, pady=5, sticky='w')

        self.lb_format1 = tk.Label(self, width=1, height=2)

        self.bt_next = tk.Button(self, text='下一题', command=self.__bt_next_cd)
        self.bt_next.grid(row=6, column=0, padx=10, pady=10)

        self.lb_exp = tk.Label(self,height=7,textvariable=exp,relief='sunken'
                            ,justify='left',anchor='nw',padx=10,wraplength=980)
        self.lb_exp.grid(row=7,column=0,padx=10,pady=10,sticky='we')

        self.myframe1 = tk.Frame(self, relief='sunken')
        self.myframe1.grid(row=8,column=0,padx=10,pady=10,sticky='we')
        self.myframe1.columnconfigure(20,weight=1)

        global labellist
        labellist = []
        for i in range(5):
            for j in range(20):
                self.lb_th = tk.Label(self.myframe1,text = i*20+j+1,bg='white',height=1,width=3)
                self.lb_th.grid(row=i,column=j,padx=5,pady=2)
                labellist.append(self.lb_th)
        
        self.lb_df =tk.Label(self.myframe1,text='得 分：',font=('宋体',12,'bold'),bg='blue',anchor='w')
        self.lb_df.grid(row=0,column=20,rowspan=2,padx=10,sticky='nwes')

        global score
        score = tk.IntVar()
        self.lb_score = tk.Label(self.myframe1,textvariable=score,font=('宋体',15,'bold'),bg='blue',anchor='n')
        self.lb_score.grid(row=2,column=20,rowspan=3,padx=10,sticky='nwes')

    def __bt_next_cd(self):
        global th, answer, img,answer_count
        answer_count = 0
        answer.initialize(None) 
        exp.initialize('')
        jkbd = JkJson(th=th)
        self.answer = jkbd.answer
        self.exp = jkbd.explains
        try:
            image = requests.get(jkbd.url).content
            bytesio = BytesIO()
            bytesio.write(image)
            image = Image.open(bytesio)
        except Exception:
            image = Image.new(mode='RGBA', size=(150, 150),color=(0,0,0,0))
        finally:
            image = self.__new_resize(image)
        img = ImageTk.PhotoImage(image=image)
        self.lb_img.config(image=img)

        # self.lb_img.config(image='')
        self.lb_qus.config(text='{}、{}'.format(th+1, jkbd.question))
        self.rd_A.config(text='A、{}'.format(jkbd.item.get('item1')))
        self.rd_B.config(text='B、{}'.format(jkbd.item.get('item2')))
        if not jkbd.item.get('item3'):
            self.rd_C.grid_remove()
            self.rd_D.grid_remove()
            self.lb_format1.grid(row=4, column=0, rowspan=2, pady=(0,35))
        else:
            self.rd_C.grid()
            self.rd_D.grid()
            self.lb_format1.grid_remove()
        self.rd_C.config(text='C、{}'.format(jkbd.item.get('item3')))
        self.rd_D.config(text='D、{}'.format(jkbd.item.get('item4')))

        del jkbd
        th = th + 1

    def __new_resize(self, image):
        img_w = image.size[0]
        img_h = image.size[1]
        new_img_h = 150
        new_img_w = int(new_img_h/img_h*img_w)
        return image.resize((new_img_w, new_img_h))

    def __eq_answer(self):
        global exp,answer,answer_count
        if self.answer == answer.get():
            if not answer_count:
                score.set(score.get()+1)
                answer_count = 1
            labellist[th-1].config(bg='green')
            s='回答正确\n'
        else:
            if answer_count :
                score.set(score.get()-1)
                answer_count = 0
            labellist[th-1].config(bg='red')
            s='回答错误\n'
        s = s + self.exp
        exp.set(s)



if __name__ == '__main__':

    myframe().mainloop()

