from tkinter import *
from tkinter import messagebox
class application(Frame):
    def __init__(self, master =None):
        super().__init__(master)
        self.master=master
        # self.pack()
        self.createWidget()

    def createWidget(self):
        self.bt = Button(root,text='送花',font=["微软雅黑",20],width=10,height=1,command=self.songhua)
        self.bt.pack()
    
    def songhua(self):
        messagebox.showinfo('送花','送花1')

root = Tk()
root.title('送花')
root.geometry("400x400")
app = application(root)
root.mainloop()