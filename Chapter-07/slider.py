#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

class SliderFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        parent.title('Slider Example')
        parent.geometry("300x350")
        panel = tk.Frame()
        tk.Scale(panel, from_=1, to=100, tickinterval=11,
                 orient=tk.HORIZONTAL).pack(fill=tk.X, expand=1)
        tk.Scale(panel, from_=1, to=100, tickinterval=11,
                 orient=tk.VERTICAL).pack(fill=tk.Y, expand=1)
        panel.pack(fill=tk.BOTH, expand=1)
      
def main():
    app = tk.Tk()
    SliderFrame(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
