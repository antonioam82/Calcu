#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        self.calc_string = ""
        self.mode = "d"

        self.screen=Entry(self.root,textvariable=self.display,bg="lavender",font=('Arial', 35, 'bold'),width=23,bd=16,justify="right")
        self.screen.place(x=10,y=11)
        self.md_btn=Button(self.root,text="Deg",width=11,height=2,bg="gray25",fg="white",command=self.change_mod)
        self.md_btn.place(x=12,y=108)
        self.Deg_btn=Button(self.root,text="X!",width=11,height=2,bg="gray25",fg="white",command=lambda:self.input("self.factorial("))#
        self.Deg_btn.place(x=102,y=108)#
        Button(self.root,text="(",width=11,height=2,bg="gray25",fg="white",command=lambda:self.input("(")).place(x=192,y=108)
        Button(self.root,text=")",width=11,height=2,bg="gray25",fg="white",command=lambda:self.input(")")).place(x=282,y=108)
        Button(self.root,text="%",width=11,height=2,bg="gray25",fg="white").place(x=372,y=108)
        Button(self.root,text="AC",width=11,height=2,bg="red",fg="white",command=self.deletion).place(x=462,y=108)
        Button(self.root,text="C",width=11,height=2,bg="red",fg="white",command=self.clear).place(x=552,y=108)
        Button(self.root,text="Inv",width=11,height=2,bg="gray25",fg="white",command=self.inv).place(x=12,y=152)
        self.sin_btn=Button(self.root,text="sin",width=11,height=2,bg="gray25",fg="white",command=lambda:self.input("sin("))
        self.sin_btn.place(x=102,y=152)
        self.ln_btn=Button(self.root,text="ln",width=11,height=2,bg="gray25",fg="white")
        self.ln_btn.place(x=192,y=152)
        Button(self.root,text="7",width=11,height=2,bg="gray40",fg="white",command=lambda:self.input("7")).place(x=282,y=152)
        Button(self.root,text="8",width=11,height=2,bg="gray40",fg="white",command=lambda:self.input("8")).place(x=372,y=152)
        Button(self.root,text="9",width=11,height=2,bg="gray40",fg="white",command=lambda:self.input("9")).place(x=462,y=152)
        Button(self.root,text="/",width=11,height=2,bg="gray25",fg="white",command=lambda:self.input("/")).place(x=552,y=152)
        Button(self.root,text="π",width=11,height=2,bg="gray25",fg="white",command=lambda:self.input('pi')).place(x=12,y=196)
        self.cos_btn=Button(self.root,text="cos",width=11,height=2,bg="gray25",fg="white",command=lambda:self.input("cos("))
        self.cos_btn.place(x=102,y=196)
        self.log_btn=Button(self.root,text="log",width=11,height=2,bg="gray25",fg="white",command=lambda:self.input('log('))
        self.log_btn.place(x=192,y=196)
        Button(self.root,text="4",width=11,height=2,bg="gray40",fg="white",command=lambda:self.input("4")).place(x=282,y=196)
        Button(self.root,text="5",width=11,height=2,bg="gray40",fg="white",command=lambda:self.input("5")).place(x=372,y=196)
        Button(self.root,text="6",width=11,height=2,bg="gray40",fg="white",command=lambda:self.input("6")).place(x=462,y=196)
        Button(self.root,text="X",width=11,height=2,bg="gray25",fg="white",command=lambda:self.input("*")).place(x=552,y=196)
        Button(self.root,text="e",width=11,height=2,bg="gray25",fg="white",command=lambda:self.input("e")).place(x=12,y=240)
        self.tan_btn=Button(self.root,text="tan",width=11,height=2,bg="gray25",fg="white",command=lambda:self.input("tan("))
        self.tan_btn.place(x=102,y=240)
        self.sqrt_btn=Button(self.root,text="√",width=11,height=2,bg="gray25",fg="white",command=lambda:self.input("sqrt("))
        self.sqrt_btn.place(x=192,y=240)
        Button(self.root,text="1",width=11,height=2,bg="gray40",fg="white",command=lambda:self.input("1")).place(x=282,y=240)
        Button(self.root,text="2",width=11,height=2,bg="gray40",fg="white",command=lambda:self.input("2")).place(x=372,y=240)
        Button(self.root,text="3",width=11,height=2,bg="gray40",fg="white",command=lambda:self.input("3")).place(x=462,y=240)
        Button(self.root,text="-",width=11,height=2,bg="gray25",fg="white",command=lambda:self.input("-")).place(x=552,y=240)
        self.ans_btn=Button(self.root,text="Ans",width=11,height=2,bg="gray25",fg="white")
        self.ans_btn.place(x=12,y=284)
        Button(self.root,text="EXP",width=11,height=2,bg="gray25",fg="white").place(x=102,y=284)
        self.e_btn=Button(self.root,text="x**y",width=11,height=2,bg="gray25",fg="white")
        self.e_btn.place(x=192,y=284)
        Button(self.root,text="0",width=11,height=2,bg="gray40",fg="white",command=lambda:self.input("0")).place(x=282,y=284)
        Button(self.root,text=".",width=11,height=2,bg="gray40",fg="white",command=lambda:self.input(".")).place(x=372,y=284)
        Button(self.root,text="=",width=11,height=2,bg="gray40",fg="white",command=self.resolve).place(x=462,y=284)
        Button(self.root,text="+",width=11,height=2,bg="gray25",fg="white",command=lambda:self.input("+")).place(x=552,y=284)
        
        self.root.mainloop()#

    def input(self,c):
        self.calc_string = self.calc_string + c
        self.display.set(self.calc_string)

    def factorial(self,n):
        if n==0 or n==1:
            result=1
        elif n>1:
            result=n*factorial(n-1)
        return result

    def change_mod(self):
        if self.mode == "d":
            self.md_btn.configure(text="Rdn")
            self.mode = "r"
        else:
            self.md_btn.configure(text="Deg")
            self.mode = "d"
            

    def resolve(self):
        if self.calc_string != "":
            try:
                self.result = eval(self.calc_string)
                self.display.set(self.result)
            except Exception as e:
                #self.display.set("ERROR")
                print(str(e))
                self.calc_string = ""

    def clear(self):
        self.display.set("0")
        self.calc_string = ""

    def deletion(self):
        if len(self.calc_string) > 0:
            self.calc_string = self.calc_string.replace(self.calc_string[-1],"",1)
            self.display.set(self.calc_string)
            if len(self.calc_string) <= 0:
                self.display.set("0")
            else:
                self.display.set(self.calc_string)
        print(self.calc_string)
            

    def inv(self):
        if self.inverted == False:
            self.sin_btn.configure(text="asin",command=lambda:self.input("asin("))
            self.cos_btn.configure(text="acos",command=lambda:self.input("acos("))
            self.ln_btn.configure(text="ex")
            self.log_btn.configure(text="10x")
            self.tan_btn.configure(text="atan",command=lambda:self.input("atan("))
            self.sqrt_btn.configure(text="x**2",command=lambda:self.input("**2"))
            self.e_btn.configure(text="y√x")
            self.inverted = True
        else:
            self.sin_btn.configure(text="sin",command=lambda:self.input("sin("))
            self.cos_btn.configure(text="cos",command=lambda:self.input("cos("))
            self.ln_btn.configure(text="ln")
            self.log_btn.configure(text="log")
            self.tan_btn.configure(text="tan",command=lambda:self.input("tan("))
            self.sqrt_btn.configure(text="√",command=lambda:self.input("sqrt("))
            self.e_btn.configure(text="x**y")
            self.inverted = False
        

if __name__=="__main__":
    calc()

