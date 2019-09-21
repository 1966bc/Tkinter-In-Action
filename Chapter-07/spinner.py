#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

class SpinnerFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        parent.title('Spinner Example')
        parent.geometry("100x100")
        self.var = tk.IntVar()
        panel = tk.Frame()
        ttk.Spinbox(panel, from_=0, to=100, textvariable=self.var).pack()
        self.var.set(5)
        panel.pack(fill=tk.BOTH, expand=1)
      
def main():
    app = tk.Tk()
    SpinnerFrame(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
