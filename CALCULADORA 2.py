from tkinter import *
from math import *
ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x600")
ventana.configure(background="SkyBlue4")
color_boton=("gray77")


def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador) #ESTA PARTE SIRVE PARA VISUALIZAR LA OPERACION EN LA PANTALLA
    

def clear():
    global operador
    operador=("")
    input_text.set(operador)

def operacion():
    global operador
    try:
        opera=str(eval(operador))#SIRVE PARA REALIZAR LA OPERACIÓN PREVIAMENTE VISUALIZADA EN PANTALLA
    except:
        clear()
        opera=("ERROR")
    input_text.set(opera)#MUESTRA EL RESULTADO


    
ancho_boton=11
alto_boton=3

input_text=StringVar()
operador=""
Boton0=Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=180)
Boton1=Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=107,y=180)
Boton2=Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=197,y=180)
Boton3=Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=287,y=180)
Boton4=Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=17,y=240)
Boton5=Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=107,y=240)
Boton6=Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=197,y=240)
Boton7=Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=287,y=240)
Boton8=Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=17,y=300)
Boton9=Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=107,y=300)
BotonC=Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("pi")).place(x=197,y=300)
BotonComa=Button(ventana,text=",",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(".")).place(x=287,y=300)
BotonSuma=Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=17,y=360)
BotonResta=Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=107,y=360)
BotonMulti=Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=197,y=360)
BotonDiv=Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=287,y=360)
BotonSqrt=Button(ventana,text="√",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("sqrt")).place(x=17,y=420)
BotonParen1=Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("(")).place(x=17,y=480)
BotonParen2=Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(")")).place(x=107,y=480)
BotonResto=Button(ventana,text="%",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("%")).place(x=197,y=480)
Botonln=Button(ventana,text="ln",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("log")).place(x=287,y=480)
BotonC=Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=107,y=420)
BotonExp=Button(ventana,text="EXP",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("**")).place(x=197,y=420)
BotonResul=Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=operacion).place(x=287,y=420)

Salida=Entry(ventana,font=('arial',20,'bold'),width=22,textvariable=input_text,bd=20,insertwidth=4,bg="powder blue",justify="right").place(x=10,y=60)


ventana.mainloop()
