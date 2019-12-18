#from tkinter import *
import Pmw
from tkinter import Button, Label
import string
from math import *
import numpy as np

Calculadora = Pmw.initialise(fontScheme = 'pmw1')
#Calculadora = Tk()
Calculadora.title("GRAPH_CALC")
Calculadora.config(bg='gray40')
Calculadora.geometry("321x500")
formula = ""
result = ""
mem = ""
ndact = False
type_op = "MATH"

def push(car):
    global formula
    formula=formula+car
    #print(formula)
    display.appendtext(car)

def typer(m):
    global type_op
    type_op = m
    print(type_op)
    clear()
    #display.appendtext(type_op+"\n")

def del_():
    global mem
    if mem!="":
        mem=""
    
def clear():
    global formula, mem, result
    formula = ""
    mem = ""
    result = ""
    display.clear()

def store():
    global mem
    if mem=="" and result!="" and result!="ERROR":
        mem = str(result)
        #display.appendtext("STORED: "+mem+"\n\n")
    else:
        push(mem)
    
def matr_demo():
    a1 = np.array([[1,2,3],[1,2,8]], float)
    a2 = np.array([[4,5,6],[2,3,4]], float)
    display.appendtext(a1+a2)

def change_sign():
    global result
    if result!="ERROR" and result!="":
        result = eval(str(result)+"*(-1)")
        text = '{:^29}'.format(str(result))
        display.appendtext((text)+"\n")

def nd():
    global ndact
    if ndact == False:
        ndact = True

def pi():
    if ndact == True:
        #numb = pi
        #display.appendtext(pi)
        push('3.141592653589793')
        
def operation():
    global formula, result
    print(formula)
    if type_op=="MATH" and formula!="":
        try:
            result = eval(formula)
        except:
            result = "ERROR"
        text = '{:^30}'.format(str(result))
        display.appendtext("\n"+text+"\n\n")
        formula=""

#PANTALLA
display = Pmw.ScrolledText(Calculadora, hscrollmode='none',#dynamic
                      vscrollmode='dynamic', hull_relief='sunken',#vscrollmode=dynamic
                      hull_background='gray40', hull_borderwidth=10, 
                      text_background='honeydew4', text_width=29, #ancho pantalla #29
                      text_foreground='black', text_height=9,#alto pantalla
          text_padx=10, text_pady=10, text_relief='groove',
                      text_font=('Arial', 12, 'bold') )
display.place(x=0,y=0)



Label(master=Calculadora,text='Quit',fg='steelblue3',bg='gray40').place(x=69,y=215)
Label(master=Calculadora,text='Ins',fg='steelblue3',bg='gray40').place(x=133,y=215)
Label(master=Calculadora,text='Lock',fg='steelblue3',bg='gray40').place(x=197,y=215)
Label(master=Calculadora,text='List',fg='steelblue3',bg='gray40').place(x=261,y=215)
#buttons1.pack(fill='both', expand=1, padx=1, pady=1)


Button(Calculadora,text='2nd',bg='steelblue3',fg='white',width=5).place(x=5,y=236) #activebackground="blue".place(x=8,y=243)
Button(Calculadora,text='Mode',bg='gray30',fg='white',width=5).place(x=69,y=236)
Button(Calculadora,text='Del',bg='gray30',fg='white',width=5).place(x=133,y=236)
Button(Calculadora,text='Alpha',bg='gray50',fg='white',width=5).place(x=197,y=236)
Button(Calculadora,text='Stat',bg='gray30',fg='white',width=5).place(x=261,y=236)
Calculadora.mainloop()





