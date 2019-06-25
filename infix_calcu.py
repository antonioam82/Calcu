from tkinter import *
ventana=Tk()
ventana.title("CALCULADORA INFIJA")
ventana.configure(background="gray36")
ventana.geometry("360x490")
numeroPantalla=StringVar()
#numero=""
#resultado=0
#prev_sign=""
#primr=True

def numeroPulsado(n):
    global numero
    numero=numero+n
    numeroPantalla.set(numero)

def calculo(o):
    global resultado
    global numero
    global primr
    global prev_sign
    global operacion
    global op
    op=o
    if primr==True:
        resultado+=float(numero)
        prev_sign=o
        numero=""
        primr=False
    else:
        try:
            if o==prev_sign and numero!="":
                if o=="+":
                    resultado+=float(numero)######
                elif o=="-":
                    resultado-=float(numero)
                elif o=="*":
                    resultado*=float(numero)
                elif o=="/":
                    resultado/=float(numero)
                elif o=="**":
                    resultado**=float(numero)
            elif o!=prev_sign and numero!="":
                print(prev_sign)
                print(numero)
                print(resultado)
                print(prev_sign)
                if prev_sign=="+":
                    resultado+=float(numero)######
                elif prev_sign=="-":
                    resultado-=float(numero)
                elif prev_sign=="*":
                    resultado*=float(numero)
                elif prev_sign=="/":
                    resultado/=float(numero)
                elif prev_sign=="**":
                    resultado**=float(numero)
                prev_sign=o
            numeroPantalla.set(resultado)
            #operacion=o
        except:
            numeroPantalla.set("ERROR")
            resultado=0
            primr=True
        numero=""

def clear():
    global numero
    global resultado
    global primr
    global prev_sign
    global operacion
    global op
    op=""
    numero=""
    resultado=0
    primr=True
    prev_sign=""
    operacion=""
    numeroPantalla.set(resultado)

def result():
    global numero
    global resultado
    global prev_sign
    global operacion
    try:
        operacion=op
        if operacion=="+":
            resultado+=float(numero)
        elif operacion=="-":
            resultado-=float(numero)
        elif operacion=="*":
            resultado*=float(numero)
        elif operacion=="/":
            resultado/=float(numero)
        elif operacion=="**":
            resultado**=float(numero)
        numeroPantalla.set(resultado)
        prev_sign=operacion
    except:
        numeroPantalla.set("ERROR")
    if operacion!="/":
        numero=0
    else:
        numero=1

clear()

Entry(ventana,font=('Arial',30,"bold"),textvariable=numeroPantalla,width=16,bd=2,bg="PaleGreen3",justify="right").place(x=1,y=30)

Button(ventana,text="7",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("7")).place(x=4,y=180)
Button(ventana,text="8",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("8")).place(x=80,y=180)
Button(ventana,text="9",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("9")).place(x=152,y=180)
Button(ventana,text="CE",width=7,bg="DarkOrange2",height=2).place(x=224,y=180)
Button(ventana,text="C",width=7,bg="DarkOrange2",height=2,command=clear).place(x=296,y=180)
Button(ventana,text="4",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("4")).place(x=4,y=238)
Button(ventana,text="5",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("5")).place(x=80,y=238)
Button(ventana,text="6",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("6")).place(x=152,y=238)
Button(ventana,text="x",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("*")).place(x=224,y=238)
Button(ventana,text="%",width=7,fg="white",bg="gray13",height=2).place(x=296,y=238)
Button(ventana,text="1",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("1")).place(x=4,y=296)
Button(ventana,text="2",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("2")).place(x=80,y=296)
Button(ventana,text="3",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("3")).place(x=152,y=296)
Button(ventana,text="+",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("+")).place(x=224,y=296)
Button(ventana,text="-",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("-")).place(x=296,y=296)
Button(ventana,text="0",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado("0")).place(x=4,y=354)
Button(ventana,text="/",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("/")).place(x=80,y=354)
Button(ventana,text=".",width=7,fg="white",bg="gray13",height=2,command=lambda:numeroPulsado(".")).place(x=152,y=354)
Button(ventana,text="EXP",width=7,fg="white",bg="gray13",height=2,command=lambda:calculo("**")).place(x=224,y=354)
Button(ventana,text="=",width=7,fg="white",bg="gray13",height=2,command=result).place(x=296,y=354)

ventana.mainloop()


