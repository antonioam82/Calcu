from tkinter import *
ventana=Tk()
ventana.title("CALCULADORA INFIJA")
ventana.configure(background="gray36")
ventana.geometry("360x490")
numeroPantalla=StringVar()
oper=False
prime_ope=True

Entry(ventana,font=('Arial',30,"bold"),textvariable=numeroPantalla,width=16,bd=2,bg="PaleGreen3",justify="right").place(x=1,y=30)

def numeroPulsado(num):
    global operacion
    global oper
    global prime_ope
    if oper==True:
        numeroPantalla.set(num)
        oper=False
    else:
        if prime_ope==True:
            num=num.replace(numeroPantalla.get(),num)
            prime_ope=False
            numeroPantalla.set(num)
        else:
            numeroPantalla.set(numeroPantalla.get()+num)

def clear():
    global operacion
    global resultado
    global oper
    global prime_ope
    operacion=""
    resultado=0
    oper=False
    numeroPantalla.set(resultado)
    if prime_ope==False:
        prime_ope=True

def division(num):
    global resultado
    global operacion
    global oper
    oper=True
    operacion="divi"
    if resultado!=0:
        resultado/=float(num)
    else:
        resultado+=float(num)
    numeroPantalla.set(resultado)

def multiplic(num):
    global resultado
    global operacion
    global oper
    oper=True
    operacion="multi"
    if resultado!=0:
        resultado*=float(num)
    else:
        resultado+=float(num)
    numeroPantalla.set(resultado)

def suma(num):
    global resultado
    global operacion
    global oper
    oper=True
    operacion="suma"
    resultado+=float(num)
    numeroPantalla.set(resultado)

def resta(num):
    global resultado
    global operacion
    global oper
    oper=True
    operacion="resta"
    if resultado!=0:
        resultado-=float(num)
    else:
        resultado+=float(num)
    numeroPantalla.set(resultado)

def el_resultado():
    global resultado
    if operacion=="suma":
        numeroPantalla.set(resultado+float(numeroPantalla.get()))
    if operacion=="resta":
        numeroPantalla.set(resultado-float(numeroPantalla.get()))
    if operacion=="multi":
        numeroPantalla.set(resultado*float(numeroPantalla.get()))
    if operacion=="divi":
        numeroPantalla.set(resultado/float(numeroPantalla.get()))
    resultado=0
    
clear()

Button(ventana,text="7",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("7")).place(x=4,y=180)
Button(ventana,text="8",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("8")).place(x=80,y=180)
Button(ventana,text="9",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("9")).place(x=152,y=180)
Button(ventana,text="CE",width=7,bg="DarkOrange2",height=2).place(x=224,y=180)
Button(ventana,text="C",width=7,bg="DarkOrange2",height=2,command=clear).place(x=296,y=180)
Button(ventana,text="4",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("4")).place(x=4,y=238)
Button(ventana,text="5",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("5")).place(x=80,y=238)
Button(ventana,text="6",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("6")).place(x=152,y=238)
Button(ventana,text="X",width=7,fg="white",bg="gray13",height=2,command=lambda:multiplic(numeroPantalla.get())).place(x=224,y=238)
Button(ventana,text="%",width=7,fg="white",bg="gray13",height=2).place(x=296,y=238)
Button(ventana,text="1",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("1")).place(x=4,y=296)
Button(ventana,text="2",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("2")).place(x=80,y=296)
Button(ventana,text="3",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("3")).place(x=152,y=296)
Button(ventana,text="+",width=7,fg="white",bg="gray13",height=2,command=lambda:suma(numeroPantalla.get())).place(x=224,y=296)
Button(ventana,text="-",width=7,fg="white",bg="gray13",height=2,command=lambda:resta(numeroPantalla.get())).place(x=296,y=296)
Button(ventana,text="0",width=7,fg="white",bg="gray13",height=2).place(x=4,y=354)
Button(ventana,text="+/-",width=7,fg="white",bg="gray13",height=2).place(x=80,y=354)
Button(ventana,text=".",width=7,fg="white",bg="gray13",height=2).place(x=152,y=354)
Button(ventana,text="EXP",width=7,fg="white",bg="gray13",height=2).place(x=224,y=354)
Button(ventana,text="=",width=7,fg="white",bg="gray13",height=2,command=lambda:el_resultado()).place(x=296,y=354)
ventana.mainloop()

