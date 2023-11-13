#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import Tk, filedialog, messagebox, ttk
import yfinance as yf
import os
import threading

class Currency_calc:
    def __init__(self):
        self.root = Tk()
        self.root.title("Currency Calculator")
        self.root.geometry("541x530")
        self.root.resizable(height=tk.FALSE,width=tk.FALSE)
        self.currencies = {'US Dollar':'USD','Euro':'EUR','Canadian Dollar':'CAD','Pound':'GBP',
                           'Japanese Yen':'JPY','Australian Dollar':'AUD','New Zeland Dollar':'NZD',
                           'Swiss Franc':'CHF','Singapur Dollar':'SGD','Hong Kong Dollar':'HKD',
                           'Swedish Crown':'SEK','Norwegian Crown':'NOK','Dannish Crown':'DKK','Yuan':'CNY'}
        
        sorted_currencies = sorted(self.currencies.keys())

        self.current_dir = tk.StringVar()
        self.amount = tk.StringVar()
        self.amount.set("")
        self.current_dir.set(os.getcwd())

        entry_dir = tk.Entry(self.root,textvariable=self.current_dir,width=90)
        entry_dir.place(x=0,y=0)
        self.currency_selector = ttk.Combobox(self.root,width=30)
        self.currency_selector["values"] = sorted_currencies
        self.currency_selector.place(x=20, y=80)
        tk.Label(self.root,text="TO",width=5,font=('Arial',10,"bold")).place(x=246,y=80)
        self.currency_selector2 = ttk.Combobox(self.root,width=30)
        self.currency_selector2["values"] = sorted_currencies
        self.currency_selector2.place(x=317, y=80)

        self.amount_entry = tk.Entry(self.root,textvariable=self.amount,width=33,font=('Arial',20,"bold"))
        self.amount_entry.place(x=20, y=140)
        self.result_label = tk.Label(self.root,width=29,font=('Arial',20,"bold"),bg="bisque")
        self.result_label.place(x=20,y=190)

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

    def btnClick(self,num):
        if num == "." and "." in self.amount_entry.get():
            return
        self.amount.set(self.amount_entry.get() + num)

    def reset_display(self):
        self.amount.set("")

    def create_ticker(self):
        tick1 = self.currencies[self.currency_selector.get()]
        tick2 = self.currencies[self.currency_selector2.get()]
        return tick1+tick2+"=X"

    def calculate(self):
        try:
            ticker = self.create_ticker()
            self.exchange = yf.download(ticker, period="1d", interval="1m")["Close"].iloc[-1]
            total = float(self.amount.get()) * self.exchange
            self.result_label.configure(text=str(round(total,6)))
        except Exception as e:
            messagebox.showwarning("ERROR",str(e))
            self.result_label.configure(text="")

    def init_task(self):
        self.result_label.configure(text="CALCULATING...")
        task = threading.Thread(target=self.calculate)
        task.start()

if __name__ == '__main__':
    Currency_calc()
