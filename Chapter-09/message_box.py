#!/usr/bin/python3
from tkinter import messagebox

if __name__ == "__main__":
   
    retCode = messagebox.askyesno('A Message Box', "Is this explanation OK?",)

    if retCode:
        print("yes")
    else:
        print("no")

    retCode = messagebox.askyesno('A Message Box', "Is this way easier?",)        

    

   


