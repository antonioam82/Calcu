#!/usr/bin/python
# -*- coding: latin-1 -*-from tkinter import *
from Tkinter import *
ventana=Tk()
ventana.title("CALCULADORA-C2")
ventana.configure(background="dark slate gray")
ventana.geometry("392x480")
color_boton=("gray60")
cn=("black")
actb="LightCyan3"
from math import *
oper=""
numero=""
resultado=0
sign=""
opera=[]
numeroPantalla=StringVar()

def entrada(num):
    global numero
    numero=numero+num
    numeroPantalla.set(numero)


def operaciooon(s):
    global opera
    global resultado
    global numero, sign
    opera.append(numero)
    if len(opera)==2 and sign==s:
		if s=="+":
			resultado=float(opera[0])+float(opera[1])
			#numeroPantalla.set(opera[0])
			opera[0]=resultado
			opera.pop()
		elif s=="-":
			resultado=float(opera[0])-float(opera[1])
			opera[0]=resultado
			opera.pop()
    numeroPantalla.set(resultado)
    sign=s
    numero=""

def resultadoo():
    global opera
    global numero
    global resultado
    opera.append(numero)
    if len(opera)==2:
        resultado=float(opera[0])+float(opera[1])
        opera[0]=resultado
    numeroPantalla.set(opera[0])
    #opera=[]
    numero=""


def clear():
    global operacion
    global resultado
    global numero
    operacion=""
    numero=""
    numeroPantalla.set("0")
    








    
clear()    

ancho_boton=6
lista_memoria=["","","","",""]

#numero=("")
alto_boton=2

alto_mem=1
ancho_mem=6
bd=10

Button(ventana,text="0",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("0")).place(x=21,y=200+15)
Button(ventana,text="1",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("1")).place(x=80,y=200+15)
Button(ventana,text="2",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("2")).place(x=139,y=200+15)
Button(ventana,text="3",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("3")).place(x=198,y=200+15)
Button(ventana,text="4",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("4")).place(x=21,y=248+15)
Button(ventana,text="5",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("5")).place(x=80,y=248+15)
Button(ventana,text="6",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("6")).place(x=139,y=248+15)
Button(ventana,text="7",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("7")).place(x=198,y=248+15)
Button(ventana,text="8",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("8")).place(x=257,y=248+15)
Button(ventana,text="9",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("9")).place(x=316,y=248+15)
Button(ventana,text="π",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada(str(pi))).place(x=21,y=296+15)
Button(ventana,text=".",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=80,y=296+15)
Button(ventana,text="+",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:operaciooon("+")).place(x=139,y=296+15)
Button(ventana,text="-",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:operaciooon("-")).place(x=198,y=296+15)
Button(ventana,text="*",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=257,y=296+15)
Button(ventana,text="/",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=316,y=296+15)
Button(ventana,text="√",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=21,y=344+15)
Button(ventana,text="(",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=198,y=344+15)
Button(ventana,text=")",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=257,y=344+15)
Button(ventana,text="%",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=80,y=344+15)
Button(ventana,text="ln",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=21,y=392+15)
Button(ventana,text="sin",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=80,y=392+15)
Button(ventana,text="cos",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=139,y=392+15)
Button(ventana,text="tan",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=198,y=392+15)
Button(ventana,text="MEM",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=257,y=392+15)
Button(ventana,text="CE",bg="firebrick1",fg=cn,activebackground="indianred1",width=ancho_boton,height=alto_boton).place(x=257,y=200+15)
Button(ventana,text="+/-",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=139,y=344+15)
Button(ventana,text="C",bg="firebrick1",fg=cn,activebackground="indianred1",width=ancho_boton,height=alto_boton,command=clear).place(x=316,y=200+15)
Button(ventana,text="EXP",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=316,y=344+15)
Button(ventana,text="=",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=resultadoo).place(x=316,y=392+15)
Button(ventana,text="MEM1",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=21,y=166+15)
Button(ventana,text="MEM2",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=80,y=166+15)
Button(ventana,text="MEM3",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=139,y=166+15)
Button(ventana,text="MEM4",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=198,y=166+15)
Button(ventana,text="MEM5",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=257,y=166+15)
Button(ventana,text="DEL",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=316,y=166+15)
#Button(ventana,text="",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=21,y=166-15)
#Button(ventana,text="",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=80,y=166-15)
#Button(ventana,text="",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=139,y=166-15)
#Button(ventana,text="",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=139,y=166-15)
#Button(ventana,text="",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=198,y=166-15)
#Button(ventana,text="",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=257,y=166-15)
#Button(ventana,text="MODE",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=316,y=166-15)
#Button(ventana,text="NORM",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem,command=deletion).place(x=,y=166-15)
Entry(ventana,font=('Arial',20,"bold"),width=21,textvariable=numeroPantalla,bd=20,insertwidth=4,bg="lavender",justify="right").place(x=16,y=50)

ventana.mainloop()

