#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import Tk, filedialog, messagebox, ttk
import yfinance as yf

class Currency_calc:
    def __init__(self):
        self.root = Tk()
        self.root.title("Currency Calculator")
        self.root.geometry("900x500")
        self.root.resizable(height=tk.FALSE,width=tk.FALSE)

        self.root.mainloop()


if __name__ == '__main__':
    Currency_calc()
