#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

class ListBoxFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__()

        parent.geometry("350x150")
        parent.title('List Box Example')
        panel = ttk.Frame()
        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                      'twelve', 'thirteen', 'fourteen']
        listBox = tk.Listbox(panel)
        listBox.pack(side=tk.LEFT,fill=tk.BOTH, expand =0) 
        panel.pack(fill=tk.BOTH, expand=1)

        for i in sampleList:
            listBox.insert(tk.END, i)

        listBox.selection_set(3)            

  
def main():
    app = tk.Tk()
    ListBoxFrame(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
