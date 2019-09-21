#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

class ButtonFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__()

        panel = ttk.Frame()
        self.gauge = ttk.Progressbar(panel, orient=tk.HORIZONTAL)
        self.gauge.place(x=20, y=50)
        panel.pack(fill=tk.BOTH, expand=1)

    def OnIdle(self,):
        self.gauge.step(1)
        self.gauge.start()
                   
def main():
    app = tk.Tk()
    app.geometry("350x150")
    app.title('Gauge Example')
    ButtonFrame(app).OnIdle()
    app.mainloop()
    
if __name__ == '__main__':
    main()
