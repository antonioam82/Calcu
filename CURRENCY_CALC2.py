#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import Tk, filedialog, messagebox, ttk
from forex_python.converter import CurrencyRates, CurrencyCodes
import os
import threading

class Currency_calc:
    def __init__(self):
        self.rates = CurrencyRates()
        self.symbols = CurrencyCodes()
        self.root = Tk()
        self.root.title("Currency Calculator")
        self.root.geometry("541x530")
        self.root.resizable(height=tk.FALSE,width=tk.FALSE)
        self.currencies = {'US Dollar':'USD','Euro':'EUR','Canadian Dollar':'CAD','Pound':'GBP',
                           'Japanese Yen':'JPY','Australian Dollar':'AUD','New Zeland Dollar':'NZD',
                           'Swiss Franc':'CHF','Singapur Dollar':'SGD','Hong Kong Dollar':'HKD',
                           'Swedish Crown':'SEK','Norwegian Crown':'NOK','Dannish Crown':'DKK','Chinese Yuan':'CNY',
                           'Peso Mexicano':'MXN','Turkish Lira':'TRY','South African Rand':'ZAR','Polish Zloty':'PLN',
                           'Hungarian Forint':'HUF','Taiwan Dollar':'TWD'}
        
        sorted_currencies = sorted(self.currencies.keys()) # EN ORDEN ALFABETICO

        # Mostrar directorio de ejecución
        self.current_dir = tk.StringVar()
        self.current_dir.set(os.getcwd())
        entry_dir = tk.Entry(self.root,textvariable=self.current_dir,width=90)
        entry_dir.place(x=0,y=0)

        # Listas desplegables
        self.currency_selector = ttk.Combobox(self.root,width=30)
        self.currency_selector["values"] = sorted_currencies
        self.currency_selector.set('US Dollar')
        self.currency_selector.place(x=20, y=80)
        tk.Label(self.root,text="TO",width=5,font=('Arial',10,"bold")).place(x=246,y=80)
        self.ex_label = tk.Label(self.root,text="",width=30,font=('Arial',10),fg="red",anchor="w")
        self.ex_label.place(x=16,y=120)
        self.currency_selector2 = ttk.Combobox(self.root,width=30)
        self.currency_selector2["values"] = sorted_currencies
        self.currency_selector2.set('Euro')
        self.currency_selector2.place(x=317, y=80)

        # Entrada de cantidad y etiqueta para resultado
        self.amount = tk.StringVar()
        self.amount.set("")        
        self.amount_entry = tk.Entry(self.root,textvariable=self.amount,width=33,font=('Arial',20,"bold"))
        self.amount_entry.place(x=20, y=140)
        self.result_label = tk.Label(self.root,width=29,font=('Arial',20,"bold"),bg="bisque")
        self.result_label.place(x=20,y=190)

        # Botones
        tk.Button(self.root,text="7",width=21,height=2,command=lambda:self.btnClick('7')).place(x=20,y=245)
        tk.Button(self.root,text="8",width=21,height=2,command=lambda:self.btnClick('8')).place(x=192,y=245)
        tk.Button(self.root,text="9",width=21,height=2,command=lambda:self.btnClick('9')).place(x=362,y=245)
        tk.Button(self.root,text="4",width=21,height=2,command=lambda:self.btnClick('4')).place(x=20,y=300)
        tk.Button(self.root,text="5",width=21,height=2,command=lambda:self.btnClick('5')).place(x=192,y=300)
        tk.Button(self.root,text="6",width=21,height=2,command=lambda:self.btnClick('6')).place(x=362,y=300)
        tk.Button(self.root,text="1",width=21,height=2,command=lambda:self.btnClick('1')).place(x=20,y=355)
        tk.Button(self.root,text="2",width=21,height=2,command=lambda:self.btnClick('2')).place(x=192,y=355)
        tk.Button(self.root,text="3",width=21,height=2,command=lambda:self.btnClick('3')).place(x=362,y=355)
        tk.Button(self.root,text="RESET",width=21,height=2,command=self.reset_display).place(x=20,y=410)
        tk.Button(self.root,text="0",width=21,height=2,command=lambda:self.btnClick('0')).place(x=192,y=410)
        tk.Button(self.root,text=".",width=21,height=2,command=lambda:self.btnClick('.')).place(x=362,y=410)

        tk.Button(self.root,text="CALCULATE",width=70,height=2,command=self.init_task).place(x=20,y=465)

        self.root.mainloop()

    # Definir cantidad y mostrarl en el entry
    def btnClick(self,num):
        if num == "." and "." in self.amount_entry.get():
            return
        self.amount.set(self.amount_entry.get() + num)

    # Resetear display
    def reset_display(self):
        self.amount.set("")

    # Define ticker
    def create_ticker(self):
        global t2
        t1 = self.currencies[self.currency_selector.get()]
        t2 = self.currencies[self.currency_selector2.get()]
        return t1, t2

    # Descarga tipo de cambio actualizado y realiza multiplicación
    def calculate(self):
        try:

            amount = float(self.amount.get())
            ticker1, ticker2 = self.create_ticker()
            ticker2_symbol = self.symbols.get_symbol(ticker2)
            total = self.rates.convert(ticker1, ticker2, amount)
            self.result_label.configure(text=str(round(total,4))+ticker2_symbol)
            '''ticker = self.create_ticker()
            self.exchange = yf.download(ticker, period="1d", interval="1m")["Adj Close"].iloc[-1]
            total = float(self.amount.get()) * self.exchange
            self.ex_label.configure(text=ticker+' ('+str(self.exchange)+')')
            self.result_label.configure(text=str(round(total,4))+" "+tick2)'''
        except Exception as e:
            messagebox.showwarning("ERROR",str(e))
            self.result_label.configure(text="")
        
    # Inicia la ejecución de la función 'calculate()'
    def init_task(self):
        self.ex_label.configure(text="")
        if self.currency_selector.get() != "" and  self.currency_selector2.get() != "":
            if self.amount_entry.get() != "":
                self.result_label.configure(text="CALCULATING...")
                task = threading.Thread(target=self.calculate)
                task.start()
            else:
                messagebox.showwarning("ERROR","Enter amount for conversion") 
        else:
             messagebox.showwarning("ERROR","No currencies selected") 

if __name__ == '__main__':
    Currency_calc()
