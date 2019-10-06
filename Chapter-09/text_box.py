#!/usr/bin/python3
import tkinter as tk
from tkinter import simpledialog

if __name__ == "__main__":

    panel = tk.Tk()

    dialog = simpledialog.askstring("Text Entry",
                                    "What kind of text would you like to enter?",
                                    initialvalue="Default Value",
                                    parent=panel)
    
    if dialog is not None:
        print(dialog)
    else:
        print("You don't have write anything")
