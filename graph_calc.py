from tkinter import *
import Pmw
import string

Calculadora = Tk()

display = Pmw.ScrolledText(Calculadora, hscrollmode='dynamic',
                      vscrollmode='dynamic', hull_relief='sunken',
                      hull_background='gray40', hull_borderwidth=10, 
                      text_background='honeydew4', text_width=16, #ancho pantalla
                      text_foreground='black', text_height=6, #alto pantalla
          text_padx=10, text_pady=10, text_relief='groove',
                      text_font=('arial', 12, 'bold'))

display.pack(padx=1,pady=1)

Calculadora.mainloop()
