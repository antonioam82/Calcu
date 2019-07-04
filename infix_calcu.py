#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
ventana=Tk()
ventana.title("CALCULADORA INFIJA")
ventana.configure(background="gray36")
ventana.geometry("366x490")
numeroPantalla=StringVar()
from math import *
#numero=""
#resultado=0
#prev_sign=""
#primr=True

#numero=str(eval("log("+l_numeros[0]+")/log("+l_numeros[1]+")")) #l_numeros[0] es el numero y l_numeros[1] es la base

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
        numeroPantalla.set("ERROR")
    exc=True
        
#def sen():
    #global numero
    #global resultado
    #global exc
    #if exc==False:
        #if abs(float(numeroPantalla.get()))==abs(float(numero)):
            #numero=sin(float(numero))
            #numeroPantalla.set(numero)
        #else:
            #resultado=sin(float(resultado))
            #numeroPantalla.set(resultado)
        #exc=True##################################################################
    #if exc==True:

def loga():
    global numero
    global resultado
    global exc
    if numero!="":
        try:
            if abs(float(numeroPantalla.get()))==abs(float(numero)):
                numero=log(float(numero))
                numeroPantalla.set(numero)
            else:
                resultado=log(float(resultado))
                numeroPantalla.set(resultado)
        except:
            clear()
            numeroPantalla.set("ERROR")

def funcis(f):
    global numero
    global resultado
    global exc
    global prev_func
    if numero!="":
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
        
#def tann():
    #global numero
    #global resultado
    #global exc
    #if exc==False:
        #if abs(float(numeroPantalla.get()))==abs(float(numero)):
            #numero=tan(float(numero))
            #numeroPantalla.set(numero)
        #else:
            #resultado=tan(float(resultado))
            #numeroPantalla.set(resultado)
        #exc=True


#def cosen():
    #global numero
    #global resultado
    #global exc
    #if exc==False:
        #if abs(float(numeroPantalla.get()))==abs(float(numero)):
            #numero=cos(float(numero))
            #numeroPantalla.set(numero)
        #else:
            #resultado=cos(float(resultado))
            #numeroPantalla.set(resultado)
    #exc=True

def comas():
    global numero
    if not "." in numero and numero!="":
        numero=numero+"."
        numeroPantalla.set(numero)

def clear_error():
    global numero
    global resultado
    numero=""
    resultado=0
    numeroPantalla.set("0")

def cambio_signo():
    global numero
    global resultado
    if numero!="" and abs(float(numeroPantalla.get()))==abs(float(numero)):
        if float(numero)!=0:
            numero=float(numero)*(-1)
            numeroPantalla.set(numero)
    else:
        if resultado!=0:
            resultado=resultado*(-1)
            numeroPantalla.set(resultado)

def raiz_cuadrada():
    global numero
    global resultado
    global exc
    try:
        if abs(float(numeroPantalla.get()))==abs(float(numero)):############
            numero=sqrt(float(numero))
            numeroPantalla.set(numero)
        else:
            resultado=sqrt(resultado)
            numeroPantalla.set(resultado)
    except:
        numeroPantalla.set("ERROR")
    exc=True
        
def pee():
    global numero
    global exc
    numero=pi
    numeroPantalla.set(numero)
    exc=True

def calculo(o):
    global resultado
    global numero
    global primr
    global prev_sign
    global operacion
    global op
    global exc
    op=o
    if primr==True and numero!="":########################################
        resultado=float(numero)
        prev_sign=o
        numero=""
        primr=False
    else:
        try:
            if o==prev_sign and numero!="" and exc==False:
                print("A")
                print(o)
                if o=="+":
                    resultado=resultado+float(numero)######
                elif o=="-":
                    resultado=resultado-float(numero)
                elif o=="*":
                    resultado=resultado*float(numero)
                elif o=="/":
                    resultado=resultado/float(numero)
                elif o=="**":
                    resultado=resultado**float(numero)
                elif o=="%":
                    resultado=resultado%float(numero)
                elif o=="log":
                    resultado=log(resultado/log(float(numero)))
                    print(resultado)
            elif o!=prev_sign and numero!="" and exc==False:
                print("B")
                print(o)
                print(numero)
                print(resultado)
                if prev_sign=="+":
                    resultado=resultado+float(numero)######
                elif prev_sign=="-":
                    resultado=resultado-float(numero)######
                elif prev_sign=="*":
                    resultado=resultado*float(numero)######
                elif prev_sign=="/":
                    resultado=resultado/float(numero)
                elif prev_sign=="**":
                    resultado=resultado**float(numero)
                elif prev_sign=="%":
                    resultado=resultado%float(numero)
                elif prev_sign=="log":
                    resultado=log(resultado)/log(float(numero))
                prev_sign=o
            numeroPantalla.set(resultado)
            #operacion=o
        except:
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
    global op
    global exc
    global prev_func
    op=""
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
    if primr==True:###################################################
        resultado=float(numeroPantalla.get())#########################
        primr=False###################################################
    try:
        operacion=op
        if numero=="":
            numero=resultado
        if operacion=="+":
            resultado=resultado+float(numero)######
        elif operacion=="-":
            resultado=resultado-float(numero)######
        elif operacion=="*":
            resultado=resultado*float(numero)######
        elif operacion=="/":
            resultado=resultado/float(numero)######
        elif operacion=="**":
            resultado=resultado**float(numero)######
        elif operacion=="%":
            resultado=resultado%float(numero)
        elif operacion=="log":
            resultado=log(resultado)/log(float(numero))
        numeroPantalla.set(resultado)
        prev_sign=operacion
        print(resultado)
        print(operacion)
        print(numero)
    except:
        numeroPantalla.set("ERROR")
        
        primr=True
        numero=0
        resultado=0
        prev_sign=""
        operacion=""
    #numero=""
    #operacion=""
    exc=True
    #prev_sign=""

clear()

Entry(ventana,font=('Arial',23,'bold'),textvariable=numeroPantalla,width=21,bd=2,bg="PaleGreen3",justify="right").place(x=1,y=30)

Button(ventana,text="7",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("7")).place(x=4,y=180)
Button(ventana,text="8",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("8")).place(x=78,y=180)
Button(ventana,text="9",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("9")).place(x=152,y=180)
Button(ventana,text="CE",width=7,bg="DarkOrange2",height=2,command=clear_error).place(x=227,y=180)
Button(ventana,text="C",width=7,bg="DarkOrange2",height=2,command=clear).place(x=302,y=180)#302
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
Button(ventana,text="M1",width=6,fg="white",bg="cornflower blue",height=1).place(x=4,y=136)
Button(ventana,text="M2",width=6,fg="white",bg="cornflower blue",height=1).place(x=65,y=136)
Button(ventana,text="DEL",width=6,fg="black",bg="cornflower blue",height=1).place(x=126,y=136)
Button(ventana,text="π",width=6,fg="white",bg="gray6",height=1,command=pee).place(x=187,y=136)
Button(ventana,text="log",width=6,fg="white",bg="gray6",height=1,command=lambda:calculo("log")).place(x=248,y=136)
Button(ventana,text="ln",width=6,fg="white",bg="gray6",height=1,command=loga).place(x=309,y=136)

ventana.mainloop()






