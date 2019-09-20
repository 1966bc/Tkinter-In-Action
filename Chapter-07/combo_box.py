#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk


class ComboBoxFrame(tk.Frame):
    def __init__(self, app):
        super().__init__()

        
        panel = tk.Frame()

        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']

        tk.Label(panel, text = "Select one:").place(x=15, y=15)
        #in tkinter Combobox haven't wx.CB_DROPDOWN,wx.CB_SIMPLE option
        ttk.Combobox(panel,values=sampleList, width=5).place(x=15, y=30)
        ttk.Combobox(panel,values=sampleList, width=5).place(x=150, y=30)
        
        panel.pack(fill=tk.BOTH, expand=1)
       
               
    

def main():
    app = tk.Tk()
    app.geometry("300x300")
    app.title('Combo Box Example')
    ComboBoxFrame(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
