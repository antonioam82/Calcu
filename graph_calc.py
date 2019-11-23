from tkinter import *
import Pmw
import string

Calculadora = Pmw.initialise(fontScheme = 'pmw1')
#Calculadora = Tk()
Calculadora.title("GRAPH_CALC")

#PANTALLA
display = Pmw.ScrolledText(Calculadora, hscrollmode='none',#dynamic
                      vscrollmode='none', hull_relief='sunken',#vscrollmode=dynamic
                      hull_background='gray40', hull_borderwidth=10, 
                      text_background='honeydew4', text_width=28, #ancho pantalla
                      text_foreground='black', text_height=10, #alto pantalla
          text_padx=10, text_pady=10, text_relief='groove',
                      text_font=('arial', 12, 'bold'))
display.pack(padx=0,pady=0)
buttons1 = Pmw.ButtonBox(Calculadora)
buttons1.pack(fill='y', expand=1, padx=1, pady=1)
#buttons1.alignbuttons()

buttons1.add('2nd',width=5)
buttons1.add('Mode')
buttons1.add('Del')
buttons1.add('Alpha')
buttons1.add('Stat')

buttons2 = Pmw.ButtonBox(Calculadora)
buttons2.pack(fill='y', expand=1, padx=1, pady=1)
#buttons2.alignbuttons()
buttons2.add('Math',width=5)
buttons2.add("Mtrx")
buttons2.add("Pgrm")
buttons2.add("Vars")
buttons2.add("Clr")

buttons3 = Pmw.ButtonBox(Calculadora)
buttons3.pack(fill='y', expand=1, padx=1, pady=1)
buttons3.add('X-1',width=5)
buttons3.add("Sin")
buttons3.add("Cos")
buttons3.add("Tan")
buttons3.add("^")

buttons4 = Pmw.ButtonBox(Calculadora)
buttons4.pack(fill='y', expand=1, padx=1, pady=1)
buttons4.add('X2',width=5)
buttons4.add(",")
buttons4.add("(")
buttons4.add(")")
buttons4.add("/",bg='steelblue1')

buttons5 = Pmw.ButtonBox(Calculadora)
buttons5.pack(fill='y', expand=1, padx=1, pady=1)
buttons5.add('Log',width=5)
buttons5.add("7")
buttons5.add("8")
buttons5.add("9")
buttons5.add("x",bg='steelblue1')

buttons6 = Pmw.ButtonBox(Calculadora)
buttons6.pack(fill='y', expand=1, padx=1, pady=1)
buttons6.add('Ln',width=5)
buttons6.add("4")
buttons6.add("5")
buttons6.add("6")
buttons6.add("-",bg='steelblue1')

buttons7 = Pmw.ButtonBox(Calculadora)
buttons7.pack(fill='y', expand=1, padx=1, pady=1)
buttons7.add('STO',width=5)
buttons7.add("1")
buttons7.add("2")
buttons7.add("3")
buttons7.add("+",bg='steelblue1')

buttons8 = Pmw.ButtonBox(Calculadora)
buttons8.pack(fill='y', expand=1, padx=1, pady=1)
buttons8.add('Off',width=5)
buttons8.add("0")
buttons8.add(".")
buttons8.add("(-)")
buttons8.add("Enter",bg='steelblue1')

bts = (buttons1,buttons2,buttons3,buttons4,buttons5,buttons6,
       buttons7,buttons8)
for i in bts:
    i.alignbuttons()


Calculadora.mainloop()

