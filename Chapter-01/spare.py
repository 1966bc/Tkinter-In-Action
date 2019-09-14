#!/usr/bin/python3
import tkinter as tk
"""Spare.py is a starting point for simple wxPython programs."""

class Frame(tk.Frame):
    pass

class App(tk.Tk):
    """Start here"""

    def __init__(self):
        super().__init__()

        self.title('Spare')
        self.geometry("400x200")
        frame = Frame(self,)
        frame.pack(fill=tk.BOTH, expand=1)

if __name__ == '__main__':
    app = App()
    app.mainloop()
