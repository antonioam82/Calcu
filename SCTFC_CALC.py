from tkinter import *
from math import *

class calc:
    def __init__(self):
        self.root = Tk()
        self.root.title("SCTFC CALCULATOR")
        self.root.geometry("653x342")
        self.root.configure(bg="gray60")

        self.inverted = False
        self.display=StringVar()
        self.display.set("0")

        self.screen=Entry(self.root,textvariable=self.display,bg="lavender",font=('Arial', 35, 'bold'),width=23,bd=16,justify="right")
        self.screen.place(x=10,y=11)
        self.Rad_btn=Button(self.root,text="Rad",width=11,height=2,bg="gray25",fg="white")
        self.Rad_btn.place(x=12,y=108)
        self.Deg_btn=Button(self.root,text="Deg",width=11,height=2,bg="gray25",fg="white")
        self.Deg_btn.place(x=102,y=108)
        Button(self.root,text="X!",width=11,height=2,bg="gray25",fg="white").place(x=192,y=108)
        Button(self.root,text="(",width=11,height=2,bg="gray25",fg="white").place(x=282,y=108)
        Button(self.root,text=")",width=11,height=2,bg="gray25",fg="white").place(x=372,y=108)
        Button(self.root,text="%",width=11,height=2,bg="gray25",fg="white").place(x=462,y=108)
        Button(self.root,text="AC",width=11,height=2,bg="red",fg="white").place(x=552,y=108)
        Button(self.root,text="Inv",width=11,height=2,bg="gray25",fg="white",command=self.inv).place(x=12,y=152)
        self.sin_btn=Button(self.root,text="sin",width=11,height=2,bg="gray25",fg="white")
        self.sin_btn.place(x=102,y=152)
        self.ln_btn=Button(self.root,text="ln",width=11,height=2,bg="gray25",fg="white")
        self.ln_btn.place(x=192,y=152)
        Button(self.root,text="7",width=11,height=2,bg="gray40",fg="white").place(x=282,y=152)
        Button(self.root,text="8",width=11,height=2,bg="gray40",fg="white").place(x=372,y=152)
        Button(self.root,text="9",width=11,height=2,bg="gray40",fg="white").place(x=462,y=152)
        Button(self.root,text="/",width=11,height=2,bg="gray25",fg="white").place(x=552,y=152)
        Button(self.root,text="π",width=11,height=2,bg="gray25",fg="white").place(x=12,y=196)
        self.cos_btn=Button(self.root,text="cos",width=11,height=2,bg="gray25",fg="white")
        self.cos_btn.place(x=102,y=196)
        self.log_btn=Button(self.root,text="log",width=11,height=2,bg="gray25",fg="white")
        self.log_btn.place(x=192,y=196)
        Button(self.root,text="4",width=11,height=2,bg="gray40",fg="white").place(x=282,y=196)
        Button(self.root,text="5",width=11,height=2,bg="gray40",fg="white").place(x=372,y=196)
        Button(self.root,text="6",width=11,height=2,bg="gray40",fg="white").place(x=462,y=196)
        Button(self.root,text="X",width=11,height=2,bg="gray25",fg="white").place(x=552,y=196)
        Button(self.root,text="e",width=11,height=2,bg="gray25",fg="white").place(x=12,y=240)
        self.tan_btn=Button(self.root,text="tan",width=11,height=2,bg="gray25",fg="white")
        self.tan_btn.place(x=102,y=240)
        self.sqrt_btn=Button(self.root,text="√",width=11,height=2,bg="gray25",fg="white")
        self.sqrt_btn.place(x=192,y=240)
        Button(self.root,text="1",width=11,height=2,bg="gray40",fg="white").place(x=282,y=240)
        Button(self.root,text="2",width=11,height=2,bg="gray40",fg="white").place(x=372,y=240)
        Button(self.root,text="3",width=11,height=2,bg="gray40",fg="white").place(x=462,y=240)
        Button(self.root,text="-",width=11,height=2,bg="gray25",fg="white").place(x=552,y=240)
        self.ans_btn=Button(self.root,text="Ans",width=11,height=2,bg="gray25",fg="white")
        self.ans_btn.place(x=12,y=284)
        Button(self.root,text="EXP",width=11,height=2,bg="gray25",fg="white").place(x=102,y=284)
        self.e_btn=Button(self.root,text="x**y",width=11,height=2,bg="gray25",fg="white")
        self.e_btn.place(x=192,y=284)
        Button(self.root,text="0",width=11,height=2,bg="gray40",fg="white").place(x=282,y=284)
        Button(self.root,text=".",width=11,height=2,bg="gray40",fg="white").place(x=372,y=284)
        Button(self.root,text="=",width=11,height=2,bg="gray40",fg="white").place(x=462,y=284)
        Button(self.root,text="+",width=11,height=2,bg="gray25",fg="white").place(x=552,y=284)
        
        self.root.mainloop()#

    def inv(self):
        if self.inverted == False:
            self.sin_btn.configure(text="asin")
            self.cos_btn.configure(text="acos")
            self.ln_btn.configure(text="ex")
            self.log_btn.configure(text="10x")
            self.tan_btn.configure(text="atan")
            self.sqrt_btn.configure(text="x**2")
            self.e_btn.configure(text="y√x")
            self.inverted = True
        else:
            self.sin_btn.configure(text="sin")
            self.cos_btn.configure(text="cos")
            self.ln_btn.configure(text="ln")
            self.log_btn.configure(text="log")
            self.tan_btn.configure(text="tan")
            self.sqrt_btn.configure(text="√")
            self.e_btn.configure(text="x**y")
            self.inverted = False
        

if __name__=="__main__":
    calc()
