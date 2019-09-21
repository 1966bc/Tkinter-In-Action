#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

class RadioBoxFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__()

        parent.title('Radio Box Example')
        parent.geometry("350x200")
        panel = ttk.Frame()
        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']
        
        w = ttk.LabelFrame(panel, text="A Radio Box",)
        
        for index, text in enumerate(sampleList):
            ttk.Radiobutton(w,
                            text=text,
                            value=index,).pack(side=tk.LEFT, anchor=tk.W)     
        w.pack(anchor=tk.W)

        for index, text in enumerate(sampleList):
            ttk.Radiobutton(panel,
                            text=text,
                            value=index,).pack(side=tk.LEFT, anchor=tk.W)

        panel.pack(fill=tk.BOTH, expand=0)
      
def main():
    app = tk.Tk()
    RadioBoxFrame(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
