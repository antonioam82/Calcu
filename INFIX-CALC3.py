#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from math import *

ventana=Tk()
ventana.title("CALCULADORA INFIJA")
ventana.configure(background="gray36")
ventana.geometry("366x450")
numeroPantalla=StringVar()
memoria=""

def numeroPulsado(n):
    global numero
    global exc
    if exc==True:
        clear()
        exc=False
    numero=numero+n
    numeroPantalla.set(numero)

def onediv():
    global numero
    global resultado
    global exc
    try:
        if abs(float(numeroPantalla.get()))==abs(float(numero)):
			numero=1/(float(numero))
            numeroPantalla.set(numero)
        else:
            resultado=1/float(resultado)
            numeroPantalla.set(resultado)
    except:
        clear()
        numeroPantalla.set("ERROR")
    exc=True

def delete():
    global memoria
    if memoria!="":
        if "M" in numeroPantalla.get():
            n=numeroPantalla.get()
            n=n.replace("M","D")
            numeroPantalla.set(n)
        t[0].config(bg="cornflower blue",fg="white")
        memoria=""
        
def memo():
    global resultado
    global memoria
    global numero
    if exc==True and numeroPantalla.get()!="ERROR":
        if memoria=="":
            memoria=float(numeroPantalla.get())
            resultado=0
            numeroPantalla.set(str(memoria)+"(M)")
            t[0].config(bg="white",fg="cornflower blue")
        else:
            numero=memoria
            numeroPantalla.set(numero)
    else:
        if memoria!="":
            numero=memoria
            numeroPantalla.set(memoria)
        

def opera_calculo(operador):
    global resultado
    if operador=="+":
        resultado=resultado+float(numero)
    elif operador=="-":
        resultado=resultado-float(numero)
    elif operador=="*":
        resultado=resultado*float(numero)
    elif operador=="/":
        resultado=resultado/float(numero)
    elif operador=="**":
        resultado=resultado**float(numero)
    elif operador=="%":
        resultado=resultado%float(numero)
    elif operador=="log":
        resultado=log(resultado)/log(float(numero))

def loga():
    global numero
    global resultado
    global exc
    if primr==True:
        if numero=="":
            numero=0
    try:
        if numero!="":
            if abs(float(numeroPantalla.get()))==abs(float(numero)):
                numero=log(float(numero))
                numeroPantalla.set(numero)
            else:
                resultado=log(float(resultado))
                numeroPantalla.set(resultado)
    except:
        clear()
        numeroPantalla.set("ERROR")


def rounde():
    global numero
    global resultado
    try:
        if abs(float(numeroPantalla.get()))==abs(float(numero)):
            numero=round(float(numero))
            numeroPantalla.set(numero)
        else:
            resultado=round(float(resultado))
            numeroPantalla.set(resultado)
    except:
        clear()
        numeroPantalla.set("ERROR")
    

def funcis(f):
    global numero
    global resultado
    global exc
    global prev_func
    if primr==True:
        if numero=="":
            numero=0
    if numero!="" and numeroPantalla.get()!="ERROR":
        li=["sin","cos","tan"]
        if exc==False or prev_func in li:
            if abs(float(numeroPantalla.get()))==abs(float(numero)):
                numero=eval(f+"("+str(numero)+")")
                numeroPantalla.set(numero)
            else:
                resultado=eval(f+"("+str(resultado)+")")
                numeroPantalla.set(resultado)
        prev_func=f
        exc=True

def comas():
    global numero
    if numero!="" and not "." in str(numero) and exc==False:
        numero=numero+"."
        numeroPantalla.set(numero)

def clear_error():
    global numero
    if numero != "" and exc == False:
		lista = list(numero)
		lista.pop()
		numero = ("").join(lista)
		if numero == "":
			numeroPantalla.set("0")
		else:
			numeroPantalla.set(numero)

def cambio_signo():
    global numero
    global resultado
    try:
        if numero!="" and abs(float(numeroPantalla.get()))==abs(float(numero)):
            if float(numero)!=0:
                numero=float(numero)*(-1)
                numeroPantalla.set(numero)
        else:
            if resultado!=0:
                resultado=resultado*(-1)
                numeroPantalla.set(resultado)
    except:
        clear()
        numeroPantalla.set("ERROR")

def raiz_cuadrada():
    global numero
    global resultado
    global exc
    try:
        if numero!="" and abs(float(numeroPantalla.get()))==abs(float(numero)):############
            numero=sqrt(float(numero))
            numeroPantalla.set(numero)
        else:
            resultado=sqrt(resultado)
            numeroPantalla.set(resultado)
    except:
        clear()#N
        numeroPantalla.set("ERROR")
    exc=True
        
def pee():
    global numero
    global exc
    if exc==True:
        clear()
    numero=str(pi)
    numeroPantalla.set(numero)

def calculo(o):
    global resultado
    global numero
    global primr
    global prev_sign
    global operacion
    global exc
    if primr==True:
        if numero=="":
            numero=0
        resultado=float(numero)
        prev_sign=o
        numero=""
        primr=False
    else:
        try:
            if numero!="" and exc==False:
                opera_calculo(prev_sign)
            prev_sign=o
            numeroPantalla.set(resultado)
        except:
            clear()
            numeroPantalla.set("ERROR")
            resultado=0
            primr=True
    
        numero=""
    exc=False

def clear():
    global numero
    global resultado
    global primr
    global prev_sign
    global operacion
    global exc
    global prev_func
    numero=""
    resultado=0
    primr=True
    prev_sign=""
    operacion=""
    exc=False
    prev_func="sin"
    numeroPantalla.set(resultado)

def result():
    global numero
    global resultado
    global prev_sign
    global operacion
    global primr
    global exc
    if primr==True:
        try:
            resultado=float(numeroPantalla.get())
            primr=False
        except:
            numeroPantalla.set(numeroPantalla.get())
    try:
        operacion=prev_sign
        if numero=="":
            numero=resultado
        opera_calculo(operacion)
        numeroPantalla.set(resultado)
    except:
        numeroPantalla.set("ERROR")
        primr=True
        numero=0
        resultado=0
        prev_sign=""
        operacion=""
    exc=True

t=[]
Entry(ventana,font=('Arial',23,'bold'),textvariable=numeroPantalla,width=21,bd=2,bg="PaleGreen3",justify="right").place(x=1,y=30)

Button(ventana,text="7",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("7")).place(x=4,y=180)
Button(ventana,text="8",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("8")).place(x=78,y=180)
Button(ventana,text="9",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("9")).place(x=152,y=180)
Button(ventana,text="CE",width=7,bg="DarkOrange2",height=2,command=clear_error).place(x=227,y=180)
Button(ventana,text="C",width=7,bg="DarkOrange2",height=2,command=clear).place(x=302,y=180)
Button(ventana,text="4",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("4")).place(x=4,y=238)
Button(ventana,text="5",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("5")).place(x=78,y=238)
Button(ventana,text="6",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("6")).place(x=152,y=238)
Button(ventana,text="x",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("*")).place(x=227,y=238)
Button(ventana,text="√",width=7,fg="white",bg="gray13",height=2,command=raiz_cuadrada).place(x=302,y=238)
Button(ventana,text="1",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("1")).place(x=4,y=296)
Button(ventana,text="2",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("2")).place(x=78,y=296)
Button(ventana,text="3",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("3")).place(x=152,y=296)
Button(ventana,text="+",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("+")).place(x=227,y=296)
Button(ventana,text="-",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("-")).place(x=302,y=296)
Button(ventana,text="0",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("0")).place(x=4,y=354)
Button(ventana,text="/",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("/")).place(x=78,y=354)
Button(ventana,text=".",width=7,fg="white",bg="gray13",height=2,command=comas).place(x=152,y=354)
Button(ventana,text="EXP",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("**")).place(x=227,y=354)
Button(ventana,text="=",width=7,fg="white",bg="gray13",height=2,command=result).place(x=302,y=354)

Button(ventana,text="+/-",width=6,fg="white",bg="gray6",height=1,command=cambio_signo).place(x=4,y=100)
Button(ventana,text="sin",width=6,fg="white",bg="gray6",height=1,command=lambda:funcis("sin")).place(x=65,y=100)
Button(ventana,text="cos",width=6,fg="white",bg="gray6",height=1,command=lambda:funcis("cos")).place(x=126,y=100)
Button(ventana,text="tan",width=6,fg="white",bg="gray6",height=1,command=lambda:funcis("tan")).place(x=187,y=100)
Button(ventana,text="%",width=6,fg="white",bg="gray6",height=1,command=lambda:calculo("%")).place(x=248,y=100)
Button(ventana,text="1/x",width=6,fg="white",bg="gray6",height=1,command=onediv).place(x=309,y=100)
Button(ventana,text="DEL",width=6,fg="white",bg="cornflower blue",height=1,command=delete).place(x=65,y=136)
Button(ventana,text="R",width=6,fg="white",bg="gray6",height=1,command=rounde).place(x=126,y=136)
Button(ventana,text="π",width=6,fg="white",bg="gray6",height=1,command=pee).place(x=187,y=136)
Button(ventana,text="log",width=6,fg="white",bg="gray6",height=1,command=lambda:calculo("log")).place(x=248,y=136)
Button(ventana,text="ln",width=6,fg="white",bg="gray6",height=1,command=loga).place(x=309,y=136)
bton_memoria=Button(ventana,text="MEM",width=6,fg="white",bg="cornflower blue",height=1,command=memo)
t.append(bton_memoria)
bton_memoria.place(x=4,y=136)
clear()

ventana.mainloop()
