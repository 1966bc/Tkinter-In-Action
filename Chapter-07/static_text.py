#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

class StaticTextFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        parent.title('Static Text Example')
        parent.geometry("400x300")
        
        panel = tk.Frame()

        ttk.Label(panel, text = "This is an example of static text").pack()

        tk.Label(panel, text="This is an example of static text",
                  bg='black',
                  fg='white').pack()
        tk.Label(panel, text="align center",
                  bg='black',
                  fg='white').pack(anchor=tk.CENTER)
        tk.Label(panel, text="align right",
                  bg='black',
                  fg='white').pack(anchor=tk.E)
        s = "You can also change the font."
        tk.Label(panel, text=s,
                 font="Helvetica 18 italic").pack(anchor=tk.W)

        panel2 = tk.Frame(panel)
        s = "Your text\ncan be split\nover multiple lines\n\neven blank ones"
        tk.Label(panel2, text=s).pack(side=tk.LEFT,anchor=tk.W)
        s = "Multi-line text\ncan also\n be right aligned\n\neven with a blank"
        tk.Label(panel2, text=s).pack(side=tk.RIGHT,anchor=tk.E)
        
        panel2.pack(fill=tk.BOTH, expand=1)
        panel.pack(fill=tk.BOTH, expand=1)
      
def main():
    app = tk.Tk()
    StaticTextFrame(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
