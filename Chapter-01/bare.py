#!/usr/bin/python3
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bare")
        self.geometry("300x300")
        f = tk.Frame(self,).pack()
 
app = App()
app.mainloop()
