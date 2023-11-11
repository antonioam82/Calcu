#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import Tk, filedialog, messagebox, ttk
import yfinance as yf
import os

class Currency_calc:
    def __init__(self):
        self.root = Tk()
        self.root.title("Currency Calculator")
        self.root.geometry("541x530")
        self.root.resizable(height=tk.FALSE,width=tk.FALSE)
        self.currencies = {'US Dollar':'USD','Euro':'EUR','Canadian Dollar':'CAD','Pound':'GBP',
                           'Japanese Yen':'JPY','Australian Dollar':'AUD','New Zeland Dollar':'NZD',
                           'Swiss Franc':'CHF','Singapur Dollar':'SGD','Hong Kong Dollar':'HKD',
                           'Swedish Crown':'SEK','Norwegian Crown':'NOR','Dannish Crown':'DKK'}
        
        sorted_currencies = sorted(self.currencies.keys())

        self.current_dir = tk.StringVar()
        self.amount = tk.StringVar()
        #self.amount.set(" ")
        self.current_dir.set(os.getcwd())

        entry_dir = tk.Entry(self.root,textvariable=self.current_dir,width=90)
        entry_dir.place(x=0,y=0)
        currency_selector = ttk.Combobox(self.root,width=30)
        currency_selector["values"] = sorted_currencies
        currency_selector.place(x=20, y=80)
        currency_selector2 = ttk.Combobox(self.root,width=30)
        currency_selector2["values"] = list(self.currencies.keys())
        currency_selector2.place(x=317, y=80)

        self.amount_entry = tk.Entry(self.root,textvariable=self.amount,width=33,font=('Arial',20,"bold"))
        self.amount_entry.place(x=20, y=140)
        result_label = tk.Label(self.root,width=29,font=('Arial',20,"bold"),bg="blue")
        result_label.place(x=20,y=190)

        tk.Button(self.root,text="7",width=21,height=2,command=lambda:self.btnClick('7')).place(x=20,y=245)
        tk.Button(self.root,text="8",width=21,height=2,command=lambda:self.btnClick('8')).place(x=192,y=245)
        tk.Button(self.root,text="9",width=21,height=2,command=lambda:self.btnClick('9')).place(x=362,y=245)
        tk.Button(self.root,text="4",width=21,height=2,command=lambda:self.btnClick('4')).place(x=20,y=300)
        tk.Button(self.root,text="5",width=21,height=2,command=lambda:self.btnClick('5')).place(x=192,y=300)
        tk.Button(self.root,text="6",width=21,height=2,command=lambda:self.btnClick('6')).place(x=362,y=300)
        tk.Button(self.root,text="1",width=21,height=2,command=lambda:self.btnClick('1')).place(x=20,y=355)
        tk.Button(self.root,text="2",width=21,height=2,command=lambda:self.btnClick('2')).place(x=192,y=355)
        tk.Button(self.root,text="3",width=21,height=2,command=lambda:self.btnClick('3')).place(x=362,y=355)
        tk.Button(self.root,text="<<",width=21,height=2).place(x=20,y=410)
        tk.Button(self.root,text="0",width=21,height=2,command=lambda:self.btnClick('0')).place(x=192,y=410)
        tk.Button(self.root,text=".",width=21,height=2,command=lambda:self.btnClick('.')).place(x=362,y=410)

        tk.Button(self.root,text="CALCULATE",width=70,height=2).place(x=20,y=465)

        self.root.mainloop()

    def btnClick(self,num):
        self.amount.set(self.amount_entry.get() + num)
        

if __name__ == '__main__':
    Currency_calc()


