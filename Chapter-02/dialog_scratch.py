#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class App(tk.Tk):
    def __init__(self,):
        super().__init__()

        messagebox.askokcancel("MessageDialog", "Is this the coolest thing ever!", parent=self)

        dlg = simpledialog.askstring("A Question",
                                     "Who is buried in Grant's tomb?",
                                     initialvalue="Cary Grant",
                                     parent=self)
         
if __name__ == '__main__':
    app = App()
    app.mainloop()
