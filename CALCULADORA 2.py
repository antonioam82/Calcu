from tkinter import *
ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x600")

def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)

def saludo():
    print("HOLA")

    

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
BotonC=Button(ventana,text="C",width=ancho_boton,height=alto_boton,command=saludo).place(x=197,y=300)#LO DE "saludo" ES PROVISIONAL (SOLO PARA QUE NO DE ERROR)
#BotonSum=Button(ventana,text="+",command=print(Salida)).place(x=110,y=50)

#Salida=Text(ventana,width=20,height=1)
#Salida.insert(INSERT,"")
#Salida.place(x=10,y=218)
Salida=Entry(ventana,font=('arial',20,'bold'),width=22,textvariable=input_text,bd=20,insertwidth=4,bg="powder blue",justify="right").place(x=10,y=60)
ventana.mainloop()

