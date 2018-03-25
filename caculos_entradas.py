from tkinter import*
from tkinter import messagebox

        
def suma():
    try:
        Salida=Text(ventana,width=20,height=1)
        Salida.insert(INSERT,"")
        Salida.place(x=125,y=280)
        solucion=numero1.get()+numero2.get()
        Salida.insert(INSERT,solucion)
    except:
        messagebox.showwarning("ERROR","Operación no válida")

def resta():
    try:
        Salida=Text(ventana,width=20,height=1)
        Salida.insert(INSERT,"")
        Salida.place(x=125,y=280)
        solucion=numero1.get()-numero2.get()
        Salida.insert(INSERT,solucion)
    except:
        messagebox.showwarning("ERROR","Operación no válida")

def multi():
    try:
        Salida=Text(ventana,width=20,height=1)
        Salida.insert(INSERT,"")
        Salida.place(x=125,y=280)
        solucion=numero1.get()*numero2.get()
        Salida.insert(INSERT,solucion)
    except:
        messagebox.showwarning("ERROR","Operación no válida")
        
def division():
    try:
        Salida=Text(ventana,width=20,height=1)
        Salida.insert(INSERT,"")
        Salida.place(x=125,y=280)
        solucion=numero1.get()/numero2.get()
        Salida.insert(INSERT,solucion)
    except:
        messagebox.showwarning("ERROR","Operación no válida")

def expon():
    try:
        Salida=Text(ventana,width=20,height=1)
        Salida.insert(INSERT,"")
        Salida.place(x=125,y=280)
        solucion=numero1.get()**numero2.get()
        Salida.insert(INSERT,solucion)
    except:
        messagebox.showwarning("ERROR","Operación no válida")
    

ventana=Tk()
numero1=IntVar()
numero2=IntVar()
ventana.geometry("400x360")
color_fondo="#055#"
ventana.configure(background=color_fondo)
ventana.title("Entradas numericas")
etiqueta4=Label(ventana,text="Primer número:",bg=color_fondo,fg="#FFF").place(x=10,y=10)
numero1Caja=Entry(ventana,textvariable=numero1).place(x=142,y=10)
etiqueta5=Label(ventana,text="Segundo número:",bg=color_fondo,fg="#FFF").place(x=10,y=40)
numero2Caja=Entry(ventana,textvariable=numero2).place(x=142,y=40)
boton=Button(ventana,text="Hacer suma",command=suma,width=53).place(x=10,y=100)
boton2=Button(ventana,text="Hacer resta",command=resta,width=53).place(x=10,y=130)
boton3=Button(ventana,text="Hacer multiplicación",command=multi,width=53).place(x=10,y=160)
boton4=Button(ventana,text="Hacer división",command=division,width=53).place(x=10,y=190)
boton5=Button(ventana,text="Exponenciación",command=expon,width=53).place(x=10,y=220)
etiqueta6=Label(ventana,text="Resultado final:",bg=color_fondo,fg="#FFF").place(x=10,y=280)
Salida=Text(ventana,width=20,height=1)
Salida.insert(INSERT,"")
Salida.place(x=125,y=280)
ventana.mainloop()
