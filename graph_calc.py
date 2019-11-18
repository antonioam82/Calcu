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
buttons1.alignbuttons()

buttons1.add('2nd',width=5)
buttons1.add('Mode')
buttons1.add('Del')
buttons1.add('Alpha')
buttons1.add('Stat')

buttons2 = Pmw.ButtonBox(Calculadora)
buttons2.pack(fill='y', expand=1, padx=1, pady=1)
buttons2.alignbuttons()
buttons2.add('Quit',width=5)
buttons2.add("1")
buttons2.add("2")
buttons2.add("3")
buttons2.add("4")

# DX


Calculadora.mainloop()

