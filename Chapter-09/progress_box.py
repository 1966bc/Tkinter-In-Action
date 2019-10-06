#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime, timedelta

class ProgressBar(ttk.Frame):
    def __init__(self, parent):
        super().__init__()

        self.elapsing = tk.StringVar()
        self.remaning = tk.StringVar()
        
        panel = ttk.Frame()
        tk.Label(panel, text="Time remaining",bg="lightgray").pack()
        self.progress_bar = ttk.Progressbar(panel, length = 200, orient=tk.HORIZONTAL)
        self.progress_bar.pack()
        
        tk.Label(panel, text="Elapsing time:",bg="lightgray").place(x=20, y=50)
        tk.Label(panel, textvariable=self.elapsing,bg="lightgray").place(x=140, y=50)
        tk.Label(panel, text = "Remaning time:",bg="lightgray").place(x=20, y=80)
        tk.Label(panel, textvariable=self.remaning,bg="lightgray").place(x=140, y=80)

        panel.pack(fill=tk.BOTH, expand=1)

    def OnIdle(self,):
        progressMax = 100
        self.keepGoing = True
        count = 0
        while self.keepGoing and count < progressMax:
            
            count = count + 10
            self.progress_bar['value'] = count
            self.update_idletasks() 
            time.sleep(1)
            x = timedelta(seconds=count)
            self.elapsing.set(x)
            y = timedelta(seconds=(progressMax-count))
            self.remaning.set(y)
              
def main():
    app = tk.Tk()
    app.geometry("350x150")
    app.title('A progress box')
    ProgressBar(app).OnIdle()
    app.mainloop()
    
if __name__ == '__main__':
    main()
