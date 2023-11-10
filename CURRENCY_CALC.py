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
        self.root.geometry("541x500")
        self.root.resizable(height=tk.FALSE,width=tk.FALSE)

        self.current_dir = tk.StringVar()
        self.current_dir.set(os.getcwd())

        entry_dir = tk.Entry(self.root,textvariable=self.current_dir,width=90)
        entry_dir.place(x=0,y=0)
        currency_selector = ttk.Combobox(self.root,width=30)
        currency_selector.place(x=20, y=80)
        currency_selector2 = ttk.Combobox(self.root,width=30)
        currency_selector2.place(x=317, y=80)

        amount_entry = tk.Entry(self.root,width=33,font=('Arial',20,"bold"))
        amount_entry.place(x=20, y=140)
        result_label = tk.Label(self.root,width=29,font=('Arial',20,"bold"),bg="blue")
        result_label.place(x=20,y=190)
        '''tk.Button(self.root,text="7",width=10,height=2).place(x=20,y=245)
        tk.Button(self.root,text="8",width=10,height=2).place(x=100,y=245)
        tk.Button(self.root,text="9",width=10,height=2).place(x=180,y=245)
        tk.Button(self.root,text="4",width=10,height=2).place(x=20,y=285)
        tk.Button(self.root,text="5",width=10,height=2).place(x=100,y=285)
        tk.Button(self.root,text="6",width=10,height=2).place(x=180,y=285)'''
        tk.Button(self.root,text="7",width=21,height=2).place(x=20,y=245)
        tk.Button(self.root,text="8",width=21,height=2).place(x=192,y=245)
        tk.Button(self.root,text="9",width=21,height=2).place(x=362,y=245)

        self.root.mainloop()


if __name__ == '__main__':
    Currency_calc()



