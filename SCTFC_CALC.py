from tkinter import *
from math import *

class calc:
    def __init__(self):
        self.root = Tk()
        self.root.title("SCTFC CALCULATOR")
        self.root.geometry("653x400")

        self.display=StringVar()
        self.display.set("0")

        self.screen=Entry(self.root,textvariable=self.display,font=('Arial', 35, 'bold'),width=23,bd=16,justify="right")
        self.screen.place(x=10,y=11)
        Rad_btn=Button(self.root,text="Rad",width=11,height=2)
        Rad_btn.place(x=12,y=108)
        Deg_btn=Button(self.root,text="Deg",width=11,height=2)
        Deg_btn.place(x=102,y=108)
        Button(self.root,text="X!",width=11,height=2).place(x=192,y=108)
        Button(self.root,text="(",width=11,height=2).place(x=282,y=108)
        Button(self.root,text=")",width=11,height=2).place(x=372,y=108)
        Button(self.root,text="%",width=11,height=2).place(x=462,y=108)
        Button(self.root,text="AC",width=11,height=2).place(x=552,y=108)
        Button(self.root,text="Inv",width=11,height=2).place(x=12,y=152)
        sin_btn=Button(self.root,text="sin",width=11,height=2)
        sin_btn.place(x=102,y=152)
        ln_btn=Button(self.root,text="ln",width=11,height=2)
        ln_btn.place(x=192,y=152)
        Button(self.root,text="7",width=11,height=2).place(x=282,y=152)
        Button(self.root,text="8",width=11,height=2).place(x=372,y=152)
        Button(self.root,text="9",width=11,height=2).place(x=462,y=152)
        Button(self.root,text="/",width=11,height=2).place(x=552,y=152)
        Button(self.root,text="π",width=11,height=2).place(x=12,y=196)
        cos_btn=Button(self.root,text="cos",width=11,height=2)
        cos_btn.place(x=102,y=196)
        log_btn=Button(self.root,text="log",width=11,height=2)
        log_btn.place(x=192,y=196)
        Button(self.root,text="4",width=11,height=2).place(x=282,y=196)
        Button(self.root,text="5",width=11,height=2).place(x=372,y=196)
        Button(self.root,text="6",width=11,height=2).place(x=462,y=196)
        Button(self.root,text="X",width=11,height=2).place(x=552,y=196)
        
        
        self.root.mainloop()#

if __name__=="__main__":
    calc()
