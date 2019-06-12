from tkinter import *
ventana=Tk()
ventana.title("CALCULADORA-C2")
ventana.configure(background="dark slate gray")
ventana.geometry("392x480")
color_boton=("gray60")
cn=("black")
actb="LightCyan3"
from math import *
oper=True
numeroPantalla=StringVar()
#def mem1(n):
    #global to_mem, active_mem, lista_memoria, active_del,oper
    #if active_mem==True and active_del==False:
        #try:
            #salida=(str(eval(to_mem)))+("(MEM")+str(n+1)+(")")
            #lista_memoria[n]=str(eval(to_mem))
        #except:
            #salida="ERROR"
        #input_texto.set(salida)
        #active_mem=False
        #print(lista_memoria)
    #else:
        #if active_del==True:
            #lista_memoria[n]=""
            #print(lista_memoria)
            #active_del==False
        #else:
            #if lista_memoria[n]!="":
                #oper=oper+str(lista_memoria[n])
                #input_texto.set(oper)
                
#def deletion():
    #global active_del
    #active_del=True
    

#def memorize():
    #global active_mem, oper, to_mem
    #active_mem=True
    #if oper!="":
        #try:
            #to_mem=str(eval(oper))
        #except:
            #imput_texto.set("ERROR")
        #oper=""


def clear():
    global operacion
    global resultado
    global oper
    operacion=""
    resultado=0
    oper=False
    numeroPantalla.set(resultado)
    








    
clear()    

input_texto=StringVar()
ancho_boton=6
lista_memoria=["","","","",""]
result=0
#numero=("")
alto_boton=2
active_mem=False
alto_mem=1
ancho_mem=6
bd=10
clear()
Button(ventana,text="0",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=21,y=200+15)
Button(ventana,text="1",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=80,y=200+15)
Button(ventana,text="2",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=139,y=200+15)
Button(ventana,text="3",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=198,y=200+15)
Button(ventana,text="4",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=21,y=248+15)
Button(ventana,text="5",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=80,y=248+15)
Button(ventana,text="6",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=139,y=248+15)
Button(ventana,text="7",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=198,y=248+15)
Button(ventana,text="8",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=257,y=248+15)
Button(ventana,text="9",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=316,y=248+15)
Button(ventana,text="π",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=21,y=296+15)
Button(ventana,text=".",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=80,y=296+15)
Button(ventana,text="+",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=139,y=296+15)
Button(ventana,text="-",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=198,y=296+15)
Button(ventana,text="*",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=257,y=296+15)
Button(ventana,text="/",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=316,y=296+15)
Button(ventana,text="√",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=21,y=344+15)
Button(ventana,text="(",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=198,y=344+15)
Button(ventana,text=")",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=257,y=344+15)
Button(ventana,text="%",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=80,y=344+15)
Button(ventana,text="ln",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=21,y=392+15)
Button(ventana,text="sin",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=80,y=392+15)
Button(ventana,text="cos",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=139,y=392+15)
Button(ventana,text="tan",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=198,y=392+15)
Button(ventana,text="MEM",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=257,y=392+15)
Button(ventana,text="CE",bg="firebrick1",fg=cn,activebackground="indianred1",width=ancho_boton,height=alto_boton).place(x=257,y=200+15)
Button(ventana,text="+/-",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=139,y=344+15)
Button(ventana,text="C",bg="firebrick1",fg=cn,activebackground="indianred1",width=ancho_boton,height=alto_boton,command=clear).place(x=316,y=200+15)
Button(ventana,text="EXP",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=316,y=344+15)
Button(ventana,text="=",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton).place(x=316,y=392+15)
Button(ventana,text="MEM1",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=21,y=166+15)
Button(ventana,text="MEM2",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=80,y=166+15)
Button(ventana,text="MEM3",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=139,y=166+15)
Button(ventana,text="MEM4",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=198,y=166+15)
Button(ventana,text="MEM5",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=257,y=166+15)
Button(ventana,text="DEL",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=316,y=166+15)
#Button(ventana,text="",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=21,y=166-15)
#Button(ventana,text="",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=80,y=166-15)
#Button(ventana,text="",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=139,y=166-15)
#Button(ventana,text="",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=139,y=166-15)
#Button(ventana,text="",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=198,y=166-15)
#Button(ventana,text="",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=257,y=166-15)
#Button(ventana,text="MODE",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem).place(x=316,y=166-15)
#Button(ventana,text="NORM",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem,command=deletion).place(x=,y=166-15)
Entry(ventana,font=('Arial',20,"bold"),width=21,textvariable=numeroPantalla,bd=20,insertwidth=4,bg="lavender",justify="right").place(x=16,y=50)

ventana.mainloop()

