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
buttons = Pmw.ButtonBox(Calculadora)
buttons.pack(fill='y', expand=1, padx=1, pady=1)
buttons.alignbuttons()

buttons.add('2nd')
buttons.add('Mode')
buttons.add('Del')
buttons.add('Alpha')
buttons.add('Stat')
#buttons.add('Quit')



Calculadora.mainloop()

