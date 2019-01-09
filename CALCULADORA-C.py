
from tkinter import *
ventana=Tk()
ventana.title("CALCULADORA-C")
ventana.configure(background="gray20")
ventana.geometry("392x488")#600
color_boton=("gray50")
cn=("white")
from math import *

def digit(n):
    global numero
    numero=numero+n
    input_text.set(numero)

def clear():
    input_text.set("0")

ancho_boton=6
alto_boton=2
input_text=StringVar()
numero=""
clear()
bd=10
Boton0=Button(ventana,text="0",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("0")).place(x=21,y=180)
Boton1=Button(ventana,text="1",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("1")).place(x=89-9,y=180)
Boton2=Button(ventana,text="2",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("2")).place(x=147-8,y=180)
Boton3=Button(ventana,text="3",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("3")).place(x=205-7,y=180)
Boton4=Button(ventana,text="4",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("4")).place(x=21,y=228)
Boton5=Button(ventana,text="5",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("5")).place(x=80,y=228)
Boton6=Button(ventana,text="6",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("6")).place(x=139,y=228)
Boton7=Button(ventana,text="7",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("7")).place(x=198,y=228)
Boton8=Button(ventana,text="8",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("8")).place(x=263-6,y=228)
Boton9=Button(ventana,text="9",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton,command=lambda:digit("9")).place(x=321-5,y=228)
BotonC=Button(ventana,text="π",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=21,y=276)
BotonComa=Button(ventana,text=",",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=80,y=276)
BotonSuma=Button(ventana,text="+",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=139,y=276)
BotonResta=Button(ventana,text="-",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=198,y=276)
BotonMulti=Button(ventana,text="*",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=263-6,y=276)
BotonDiv=Button(ventana,text="/",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=321-5,y=276)
BotonSqrt=Button(ventana,text="√",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=21,y=324)
BotonParen1=Button(ventana,text="(",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=198,y=324)
BotonParen2=Button(ventana,text=")",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=263-6,y=324)
BotonResto=Button(ventana,text="%",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=80,y=324)
Botonln=Button(ventana,text="ln",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=21,y=372)
BotonSn=Button(ventana,text="sin",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=80,y=372)
BotonCs=Button(ventana,text="cos",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=139,y=372)
BotonTn=Button(ventana,text="tan",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=198,y=372)
BotonR=Button(ventana,text="R",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=263-6,y=372)
BotonCE=Button(ventana,text="CE",bg="red",fg=cn,width=ancho_boton,height=alto_boton).place(x=263-6,y=180)
BotonCS=Button(ventana,text="+/-",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=139,y=324)
BotonC=Button(ventana,text="C",bg="red",fg=cn,width=ancho_boton,height=alto_boton).place(x=321-5,y=180)
BotonExp=Button(ventana,text="EXP",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=321-5,y=324)
BotonResul=Button(ventana,text="=",bg=color_boton,fg=cn,width=ancho_boton,height=alto_boton).place(x=321-5,y=372)


Salida=Entry(ventana,font=('Arial',20,"bold"),width=21,textvariable=input_text,bd=20,insertwidth=4,bg="lavender",justify="right").place(x=16,y=60)
#22,10

ventana.mainloop()
