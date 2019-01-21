from tkinter import *
ventana=Tk()
ventana.title("CALCULADORA-C2")
ventana.configure(background="gray20")
ventana.geometry("392x488")
color_boton=("gray50")
cn=("white")
actb="LightCyan3"
from math import *


def clear():
    global oper
    oper=""
    input_texto.set("0")
    

input_texto=StringVar()
ancho_boton=6
#numero=("")
alto_boton=2
alto_mem=1
ancho_mem=6
input_text=StringVar()
bd=10
clear()
Button(ventana,text="0",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=21,y=200)
Button(ventana,text="1",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=80,y=200)
Button(ventana,text="2",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=139,y=200)
Button(ventana,text="3",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=198,y=200)
Button(ventana,text="4",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=21,y=248)
Button(ventana,text="5",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=80,y=248)
Button(ventana,text="6",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=139,y=248)
Button(ventana,text="7",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=198,y=248)
Button(ventana,text="8",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=257,y=248)
Button(ventana,text="9",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=316,y=248)
Button(ventana,text="π",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=21,y=296)
Button(ventana,text=".",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=80,y=296)
Button(ventana,text="+",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=139,y=296)
Button(ventana,text="-",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=198,y=296)
Button(ventana,text="*",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=257,y=296)
Button(ventana,text="/",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=316,y=296)
Button(ventana,text="√",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=21,y=344)
Button(ventana,text="(",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=198,y=344)
Button(ventana,text=")",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=257,y=344)
Button(ventana,text="%",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=80,y=344)
Button(ventana,text="ln",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=21,y=392)
Button(ventana,text="sin",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=80,y=392)
Button(ventana,text="cos",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=139,y=392)
Button(ventana,text="tan",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=198,y=392)
Button(ventana,text="MEM",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=257,y=392)
Button(ventana,text="CE",bg="red",fg=cn,activebackground="indianred1",width=ancho_boton,height=alto_boton).place(x=257,y=200)
Button(ventana,text="+/-",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=139,y=344)
Button(ventana,text="C",bg="red",fg=cn,activebackground="indianred1",width=ancho_boton,height=alto_boton).place(x=316,y=200)
Button(ventana,text="EXP",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=316,y=344)
Button(ventana,text="=",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=316,y=392)
#MEMORIZAR RESULTADOS
Button(ventana,text="MEM1",bg="gray13",fg=cn,width=ancho_mem,height=alto_mem).place(x=21,y=166)
Button(ventana,text="MEM2",bg="gray13",fg=cn,width=ancho_mem,height=alto_mem).place(x=80,y=166)
Button(ventana,text="MEM3",bg="gray13",fg=cn,width=ancho_mem,height=alto_mem).place(x=139,y=166)
Button(ventana,text="MEM4",bg="gray13",fg=cn,width=ancho_mem,height=alto_mem).place(x=198,y=166)
Button(ventana,text="MEM5",bg="gray13",fg=cn,width=ancho_mem,height=alto_mem).place(x=257,y=166)
Button(ventana,text="MEM6",bg="gray13",fg=cn,width=ancho_mem,height=alto_mem).place(x=316,y=166)

Entry(ventana,font=('Arial',20,"bold"),width=21,textvariable=input_texto,bd=20,insertwidth=4,bg="lavender",justify="right").place(x=16,y=50)

