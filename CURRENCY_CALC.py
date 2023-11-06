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
        self.root.geometry("900x500")
        self.root.resizable(height=tk.FALSE,width=tk.FALSE)

        self.current_dir = tk.StringVar()
        self.current_dir.set(os.getcwd())

        entry_dir = tk.Entry(self.root,textvariable=self.current_dir,width=149)
        entry_dir.place(x=0,y=0)

        self.root.mainloop()


if __name__ == '__main__':
    Currency_calc()
