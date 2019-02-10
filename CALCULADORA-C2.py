from tkinter import *
ventana=Tk()
ventana.title("CALCULADORA-C2")
ventana.configure(background="dark slate gray")
ventana.geometry("392x488")
color_boton=("gray60")
cn=("black")
actb="LightCyan3"
from math import *

def mem1(n):
    global to_mem, active_mem, lista_memoria, active_del,oper
    if active_mem==True and active_del==False:
        try:
            salida=(str(eval(to_mem)))+("(MEM")+str(n+1)+(")")
            lista_memoria[n]=str(eval(to_mem))
        except:
            salida="ERROR"
        input_texto.set(salida)
        active_mem=False
        print(lista_memoria)
    else:
        if active_del==True:
            lista_memoria[n]=""
            print(lista_memoria)
            active_del==False
        else:
            if lista_memoria[n]!="":
                oper=oper+str(lista_memoria[n])
                input_texto.set(oper)
                
def cambio_signo():
    global result, to_mem
    if result!="ERROR" and result!="" and result!=0:
        result=result*(-1)
        to_mem=str(result*(-1))
        input_texto.set(to_mem)

def deletion():
    global active_del
    active_del=True
    
def entrada(n):
    global oper, to_mem
    oper=oper+n
    to_mem=oper
    input_texto.set(oper)

def memorize():
    global active_mem
    active_mem=True

def resultado():
    global oper
    global result
    try:
        result=eval(oper)
    except:
        result="ERROR"
    input_texto.set(result)

def clear():
    global oper
    global to_mem
    global active_del
    oper=""
    to_mem=""
    active_del=False
    input_texto.set("0")
    

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
Button(ventana,text="0",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("0")).place(x=21,y=200)
Button(ventana,text="1",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("1")).place(x=80,y=200)
Button(ventana,text="2",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("2")).place(x=139,y=200)
Button(ventana,text="3",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("3")).place(x=198,y=200)
Button(ventana,text="4",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("4")).place(x=21,y=248)
Button(ventana,text="5",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("5")).place(x=80,y=248)
Button(ventana,text="6",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("6")).place(x=139,y=248)
Button(ventana,text="7",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("7")).place(x=198,y=248)
Button(ventana,text="8",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("8")).place(x=257,y=248)
Button(ventana,text="9",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("9")).place(x=316,y=248)
Button(ventana,text="π",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("pi")).place(x=21,y=296)
Button(ventana,text=".",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada(".")).place(x=80,y=296)
Button(ventana,text="+",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("+")).place(x=139,y=296)
Button(ventana,text="-",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("-")).place(x=198,y=296)
Button(ventana,text="*",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("*")).place(x=257,y=296)
Button(ventana,text="/",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("/")).place(x=316,y=296)
Button(ventana,text="√",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("sqrt")).place(x=21,y=344)
Button(ventana,text="(",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("(")).place(x=198,y=344)
Button(ventana,text=")",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada(")")).place(x=257,y=344)
Button(ventana,text="%",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("%")).place(x=80,y=344)
Button(ventana,text="ln",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("log")).place(x=21,y=392)
Button(ventana,text="sin",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("sin")).place(x=80,y=392)
Button(ventana,text="cos",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("cos")).place(x=139,y=392)
Button(ventana,text="tan",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("tan")).place(x=198,y=392)
Button(ventana,text="MEM",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=memorize).place(x=257,y=392)
Button(ventana,text="CE",bg="firebrick1",fg=cn,activebackground="indianred1",width=ancho_boton,height=alto_boton).place(x=257,y=200)
Button(ventana,text="+/-",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=cambio_signo).place(x=139,y=344)
Button(ventana,text="C",bg="firebrick1",fg=cn,activebackground="indianred1",width=ancho_boton,height=alto_boton,command=clear).place(x=316,y=200)
Button(ventana,text="EXP",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=lambda:entrada("**")).place(x=316,y=344)
Button(ventana,text="=",bg=color_boton,fg=cn,activebackground=actb,width=ancho_boton,height=alto_boton,command=resultado).place(x=316,y=392)
Button(ventana,text="MEM1",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem,command=lambda:mem1(0)).place(x=21,y=166)
Button(ventana,text="MEM2",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem,command=lambda:mem1(1)).place(x=80,y=166)
Button(ventana,text="MEM3",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem,command=lambda:mem1(2)).place(x=139,y=166)
Button(ventana,text="MEM4",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem,command=lambda:mem1(3)).place(x=198,y=166)
Button(ventana,text="MEM5",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem,command=lambda:mem1(4)).place(x=257,y=166)
Button(ventana,text="DEL",bg="gray48",fg=cn,width=ancho_mem,height=alto_mem,command=deletion).place(x=316,y=166)

Entry(ventana,font=('Arial',20,"bold"),width=21,textvariable=input_texto,bd=20,insertwidth=4,bg="lavender",justify="right").place(x=16,y=50)

ventana.mainloop()

