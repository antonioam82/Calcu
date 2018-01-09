from tkinter import *
ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x600")
from math import *

def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)
    

def clear():
    global operador
    operador=("")
    input_text.set(operador)

#def cero():
    #global operador
    #operador=("0")
    #input_text.set(operador)



def operacion():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        clear()
        opera=("ERROR")
        input_text.set(opera)


def raiz_cuad():
    try:
        opera=sqrt(int(input_text.get()))
        input_text.set(opera)
    except:
        clear()

    
ancho_boton=11
alto_boton=3

input_text=StringVar()
operador=""
Boton0=Button(ventana,text="0",width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=180)
Boton1=Button(ventana,text="1",width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=107,y=180)
Boton2=Button(ventana,text="2",width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=197,y=180)
Boton3=Button(ventana,text="3",width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=287,y=180)
Boton4=Button(ventana,text="4",width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=17,y=240)
Boton5=Button(ventana,text="5",width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=107,y=240)
Boton6=Button(ventana,text="6",width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=197,y=240)
Boton7=Button(ventana,text="7",width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=287,y=240)
Boton8=Button(ventana,text="8",width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=17,y=300)
Boton9=Button(ventana,text="9",width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=107,y=300)
BotonC=Button(ventana,text="AC",width=ancho_boton,height=alto_boton,command=clear).place(x=197,y=300)
BotonComa=Button(ventana,text=",",width=ancho_boton,height=alto_boton,command=lambda:btnClik(".")).place(x=287,y=300)
BotonSuma=Button(ventana,text="+",width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=17,y=360)
BotonResta=Button(ventana,text="-",width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=107,y=360)
BotonMulti=Button(ventana,text="*",width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=197,y=360)
BotonDiv=Button(ventana,text="/",width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=287,y=360)
BotonSqrt=Button(ventana,text="√",width=ancho_boton,height=alto_boton,command=raiz_cuad).place(x=17,y=420)
BotonParen1=Button(ventana,text="(",width=ancho_boton,height=alto_boton,command=lambda:btnClik("(")).place(x=17,y=480)
BotonParen2=Button(ventana,text=")",width=ancho_boton,height=alto_boton,command=lambda:btnClik(")")).place(x=107,y=480)
BotonC=Button(ventana,text="C",width=ancho_boton,height=alto_boton,command=clear).place(x=107,y=420)#Quiero que sea "0"
BotonExp=Button(ventana,text="EXP",width=ancho_boton,height=alto_boton,command=lambda:btnClik("**")).place(x=197,y=420)#LO DE "saludo" ES PROVISIONAL (SOLO PARA QUE NO DE ERROR)
BotonResul=Button(ventana,text="=",width=ancho_boton,height=alto_boton,command=operacion).place(x=287,y=420)

Salida=Entry(ventana,font=('arial',20,'bold'),width=22,textvariable=input_text,bd=20,insertwidth=4,bg="powder blue",justify="right").place(x=10,y=60)


ventana.mainloop()




