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

def numeroPulsado(n):
    global numero
    #global resultado
    global exc
    if exc==True:
        clear()
        exc=False
    numero=numero+n
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
    print(numero)
    if numeroPantalla.get()==numero:
        numero=float(numero)*(-1)
        numeroPantalla.set(numero)
    else:
        resultado=resultado*(-1)
        numeroPantalla.set(resultado)

def raiz_cuadrada():
    global numero
    global resultado
    print(resultado)
    try:
        if numeroPantalla.get()==numero:
            numero=sqrt(float(numero))
            numeroPantalla.set(numero)
        else:
            resultado=sqrt(resultado)
            numeroPantalla.set(resultado)
    except:
        numeroPantalla.set("ERROR")
        numero=""
        
def pee():
    global numero
    numero=pi
    numeroPantalla.set(numero)

def calculo(o):
    global resultado
    global numero
    global primr
    global prev_sign
    global operacion
    global op
    global exc
    op=o
    if primr==True:
        print("C")
        resultado=float(numero)
        print("N",numero)
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
                    print("bbbb")
                    resultado=resultado**float(numero)
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
    op=""
    numero=""
    resultado=0
    primr=True
    prev_sign=""
    operacion=""
    exc=False
    numeroPantalla.set(resultado)

def result():
    global numero
    global resultado
    global prev_sign
    global operacion
    global primr
    global exc
    try:
        operacion=op
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
        numeroPantalla.set(resultado)
        prev_sign=operacion
    except:
        numeroPantalla.set("ERROR")
        print(resultado)
        print(operacion)
        print(numero)
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
Button(ventana,text="%",width=7,fg="white",bg="gray13",height=2).place(x=302,y=238)
Button(ventana,text="1",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("1")).place(x=4,y=296)
Button(ventana,text="2",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("2")).place(x=78,y=296)
Button(ventana,text="3",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("3")).place(x=152,y=296)
Button(ventana,text="+",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("+")).place(x=227,y=296)
Button(ventana,text="-",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("-")).place(x=302,y=296)
Button(ventana,text="0",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("0")).place(x=4,y=354)
Button(ventana,text="/",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("/")).place(x=78,y=354)
Button(ventana,text=".",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado(".")).place(x=152,y=354)
Button(ventana,text="EXP",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("**")).place(x=227,y=354)
Button(ventana,text="=",width=7,fg="white",bg="gray13",height=2,command=result).place(x=302,y=354)

Button(ventana,text="+/-",width=6,fg="white",bg="gray6",height=1,command=cambio_signo).place(x=4,y=100)
Button(ventana,text="sin",width=6,fg="white",bg="gray6",height=1).place(x=65,y=100)
Button(ventana,text="cos",width=6,fg="white",bg="gray6",height=1).place(x=126,y=100)
Button(ventana,text="tan",width=6,fg="white",bg="gray6",height=1).place(x=187,y=100)
Button(ventana,text="√",width=6,fg="white",bg="gray6",height=1,command=raiz_cuadrada).place(x=248,y=100)
Button(ventana,text="1/x",width=6,fg="white",bg="gray6",height=1).place(x=309,y=100)
Button(ventana,text="M1",width=6,fg="white",bg="cornflower blue",height=1).place(x=4,y=136)
Button(ventana,text="M2",width=6,fg="white",bg="cornflower blue",height=1).place(x=65,y=136)
Button(ventana,text="DEL",width=6,fg="black",bg="cornflower blue",height=1).place(x=126,y=136)
Button(ventana,text="π",width=6,fg="white",bg="gray6",height=1,command=pee).place(x=187,y=136)
Button(ventana,text="log",width=6,fg="white",bg="gray6",height=1).place(x=248,y=136)
Button(ventana,text="ln",width=6,fg="white",bg="gray6",height=1).place(x=309,y=136)

ventana.mainloop()





