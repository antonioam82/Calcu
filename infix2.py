#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
ventana=Tk()
ventana.title("CALCULADORA INFIJA-B")
ventana.configure(background="gray36")
ventana.geometry("366x510")#490
numeroPantalla=StringVar()
gradte=StringVar()
from math import *
Entry(ventana,font=('Arial',7,'bold'),textvariable=gradte,width=71,bd=2,bg="PaleGreen3",justify="left").place(x=1,y=10)
Entry(ventana,font=('Arial',23,'bold'),textvariable=numeroPantalla,width=21,bd=2,bg="PaleGreen3",justify="right").place(x=1,y=30)

Button(ventana,text="7",width=7,fg="white",bg="gray13",height=2).place(x=4,y=240)
Button(ventana,text="8",width=7,fg="white",bg="gray13",height=2).place(x=78,y=240)
Button(ventana,text="9",width=7,fg="white",bg="gray13",height=2).place(x=152,y=240)
Button(ventana,text="CE",width=7,bg="DarkOrange2",height=2).place(x=227,y=240)
Button(ventana,text="C",width=7,bg="DarkOrange2",height=2).place(x=302,y=240)#302
Button(ventana,text="4",width=7,fg="white",bg="gray13",height=2).place(x=4,y=308)
Button(ventana,text="5",width=7,fg="white",bg="gray13",height=2).place(x=78,y=308)
Button(ventana,text="6",width=7,fg="white",bg="gray13",height=2).place(x=152,y=308)
Button(ventana,text="x",width=7,fg="white",bg="gray13",height=2).place(x=227,y=308)
Button(ventana,text="√",width=7,fg="white",bg="gray13",height=2).place(x=302,y=308)
Button(ventana,text="1",width=7,fg="white",bg="gray13",height=2).place(x=4,y=376)
Button(ventana,text="2",width=7,fg="white",bg="gray13",height=2).place(x=78,y=376)
Button(ventana,text="3",width=7,fg="white",bg="gray13",height=2).place(x=152,y=376)
Button(ventana,text="+",width=7,fg="white",bg="gray13",height=2).place(x=227,y=376)
Button(ventana,text="-",width=7,fg="white",bg="gray13",height=2).place(x=302,y=376)
Button(ventana,text="0",width=7,fg="white",bg="gray13",height=2).place(x=4,y=444)
Button(ventana,text="/",width=7,fg="white",bg="gray13",height=2).place(x=78,y=444)
Button(ventana,text=".",width=7,fg="white",bg="gray13",height=2).place(x=152,y=444)
Button(ventana,text="EXP",width=7,fg="white",bg="gray13",height=2).place(x=227,y=444)
Button(ventana,text="=",width=7,fg="white",bg="gray13",height=2).place(x=302,y=444)
Label(ventana,text="TAB",width=6,bg="gray36",fg="orange",height=1).place(x=126,y=75)
Button(ventana,text="SHIFT",width=6,bg="orange",height=1).place(x=4,y=94)
Button(ventana,text="DRG",width=6,fg="white",bg="gray6",height=1).place(x=65,y=94)
Button(ventana,text="FSE",width=6,fg="white",bg="gray6",height=1).place(x=126,y=94)
Button(ventana,text="MR",width=6,fg="blue2",bg="gray6",height=1).place(x=187,y=94)
Button(ventana,text="MS",width=6,fg="blue2",bg="gray6",height=1).place(x=248,y=94)
Button(ventana,text="M+",width=6,fg="blue2",bg="gray6",height=1).place(x=309,y=94)
Button(ventana,text="hyp",width=6,fg="white",bg="gray6",height=1).place(x=4,y=140)
Button(ventana,text="sin",width=6,fg="white",bg="gray6",height=1).place(x=65,y=140)
Button(ventana,text="cos",width=6,fg="white",bg="gray6",height=1).place(x=126,y=140)
Button(ventana,text="tan",width=6,fg="white",bg="gray6",height=1).place(x=187,y=140)
Button(ventana,text="ln",width=6,fg="white",bg="gray6",height=1).place(x=248,y=140)
Button(ventana,text="log",width=6,fg="white",bg="gray6",height=1).place(x=309,y=140)
Button(ventana,text="y^​x",width=6,fg="white",bg="gray6").place(x=4,y=186)#"cornflower blue"
Button(ventana,text="√",width=6,fg="white",bg="gray6").place(x=65,y=186)#"cornflower blue"
Button(ventana,text="x^​2",width=6,fg="white",bg="gray6",height=1).place(x=126,y=186)
Button(ventana,text="%",width=6,fg="white",bg="gray6",height=1).place(x=187,y=186)
Button(ventana,text="(",width=6,fg="white",bg="gray6",height=1).place(x=248,y=186)
Button(ventana,text=")",width=6,fg="white",bg="gray6",height=1).place(x=309,y=186)

ventana.mainloop()