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
Calculadora.geometry("321x668")
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

def twond_():
    global ndact
    if ndact == True:
        ndact = False
    else:
        ndact = True
    nd()
    ##################################################################
    
def clear():
    global formula, mem, result, ndact
    formula = ""
    mem = ""
    result = ""
    ndact = False
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
    if ndact == True:
        btDiv.configure(command=lambda:push("sqrt("))
        btPhin.configure(command=pi)
        btMult.configure(command=lambda:push("["))
        btRest.configure(command=lambda:push("]"))
        btOpen.configure(command=lambda:push("{"))
        btClose.configure(command=lambda:push("}"))
        btChang.configure(command=lambda:push("abs("))
        btSin.configure(command=lambda:push("asin("))
        btCos.configure(command=lambda:push("acos("))
        btTan.configure(command=lambda:push("atan("))
    else:
        btDiv.configure(command=lambda:push("/"))
        #btPhin.configure(command...
        btMult.configure(command=lambda:push("*"))
        btRest.configure(command=lambda:push("-"))
        btOpen.configure(command=lambda:push("("))
        btClose.configure(command=lambda:push(")"))
        btChang.configure(command=change_sign)
        btSin.configure(command=lambda:push("sin("))
        btCos.configure(command=lambda:push("cos("))
        btTan.configure(command=lambda:push("tan("))
        
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

labels = [' ','Quit','Ins','Lock','List','Test','Angle','Draw','Yvar',' ',
          'Abs','Sin-1','Cos-1','Tan-1','π','Root','EE','{','}','√','10x',
          'Un-1','Vn-1','n','[','ex','L4','L5','L6',']','RCL','L1','L2','L3',
          'MEM',' ',' ',':','ANS','Entry']

#64
#55
c=5
f=215
for l in labels:
    Label(Calculadora,text=l,bg='gray40',fg='steelblue3').place(x=c,y=f)
    c+=64
    if c==325:
        c=5
        f+=55

Button(Calculadora,text='2nd',bg='steelblue3',fg='white',width=5,command=twond_).place(x=5,y=236) #################################activebackground="blue".place(x=8,y=243)
Button(Calculadora,text='Mode',bg='gray30',fg='white',width=5).place(x=69,y=236)
Button(Calculadora,text='Del',bg='gray30',fg='white',width=5,command=del_).place(x=133,y=236)
Button(Calculadora,text='Alpha',bg='gray50',fg='white',width=5).place(x=197,y=236)
Button(Calculadora,text='Stat',bg='gray30',fg='white',width=5).place(x=261,y=236)

Button(Calculadora,text='Math',bg='gray30',fg='white',width=5).place(x=5,y=291)
Button(Calculadora,text='Mtrx',bg='gray30',fg='white',width=5).place(x=69,y=291)
Button(Calculadora,text='Prgm',bg='gray30',fg='white',width=5).place(x=133,y=291)
Button(Calculadora,text='Vars',bg='gray30',fg='white',width=5).place(x=197,y=291)
Button(Calculadora,text='Clr',bg='gray30',fg='white',width=5).place(x=261,y=291)

btChang=Button(Calculadora,text='x-1',bg='gray30',fg='white',width=5,command=change_sign)
btChang.place(x=5,y=346)
btSin=Button(Calculadora,text='Sin',bg='gray30',fg='white',width=5,command=lambda:push("sin("))
btSin.place(x=69,y=346)
btCos=Button(Calculadora,text='Cos',bg='gray30',fg='white',width=5,command=lambda:push("cos("))
btCos.place(x=133,y=346)
btTan=Button(Calculadora,text='Tan',bg='gray30',fg='white',width=5,command=lambda:push("tan("))
btTan.place(x=197,y=346)
btPhin=Button(Calculadora,text='^',bg='gray30',fg='white',width=5)
btPhin.place(x=261,y=346)

Button(Calculadora,text='x2',bg='gray30',fg='white',width=5).place(x=5,y=401)
Button(Calculadora,text=',',bg='gray30',fg='white',width=5,command=lambda:push(",")).place(x=69,y=401)
btOpen=Button(Calculadora,text='(',bg='gray30',fg='white',width=5,command=lambda:push("("))
btOpen.place(x=133,y=401)
btClose=Button(Calculadora,text=')',bg='gray30',fg='white',width=5,command=lambda:push(")"))
btClose.place(x=197,y=401)
btDiv=Button(Calculadora,text='/',bg='steelblue3',fg='white',width=5,command=lambda:push("/"))
btDiv.place(x=261,y=401)################################################################################################################

Button(Calculadora,text='Log',bg='gray30',fg='white',width=5).place(x=5,y=456)
Button(Calculadora,text='7',bg='gray50',fg='white',width=5,command=lambda:push("7")).place(x=69,y=456)
Button(Calculadora,text='8',bg='gray50',fg='white',width=5,command=lambda:push("8")).place(x=133,y=456)
Button(Calculadora,text='9',bg='gray50',fg='white',width=5,command=lambda:push("9")).place(x=197,y=456)
btMult=Button(Calculadora,text='x',bg='steelblue3',fg='white',width=5,command=lambda:push("*"))
btMult.place(x=261,y=456)

Button(Calculadora,text='Ln',bg='gray30',fg='white',width=5).place(x=5,y=511)
Button(Calculadora,text='4',bg='gray50',fg='white',width=5,command=lambda:push("4")).place(x=69,y=511)
Button(Calculadora,text='5',bg='gray50',fg='white',width=5,command=lambda:push("5")).place(x=133,y=511)
Button(Calculadora,text='6',bg='gray50',fg='white',width=5,command=lambda:push("6")).place(x=197,y=511)
btRest=Button(Calculadora,text='-',bg='steelblue3',fg='white',width=5,command=lambda:push("-"))
btRest.place(x=261,y=511)

Button(Calculadora,text='STO',bg='gray30',fg='white',width=5,command=store).place(x=5,y=566)
Button(Calculadora,text='1',bg='gray50',fg='white',width=5,command=lambda:push("1")).place(x=69,y=566)
Button(Calculadora,text='2',bg='gray50',fg='white',width=5,command=lambda:push("2")).place(x=133,y=566)
Button(Calculadora,text='3',bg='gray50',fg='white',width=5,command=lambda:push("3")).place(x=197,y=566)
Button(Calculadora,text='+',bg='steelblue3',fg='white',width=5,command=lambda:push("+")).place(x=261,y=566)

Button(Calculadora,text='Off',bg='gray30',fg='white',width=5,command=clear).place(x=5,y=621)
Button(Calculadora,text='0',bg='gray50',fg='white',width=5,command=lambda:push("0")).place(x=69,y=621)
Button(Calculadora,text='.',bg='gray50',fg='white',width=5,command=lambda:push(".")).place(x=133,y=621)
Button(Calculadora,text='(-)',bg='gray50',fg='white',width=5).place(x=197,y=621)
Button(Calculadora,text='Enter',bg='steelblue3',fg='white',width=5,command=operation).place(x=261,y=621)

Calculadora.mainloop()





