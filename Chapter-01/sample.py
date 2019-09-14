#!/usr/bin/python3
import tkinter as tk

class MyFrame(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("My Frame")
        self.text = tk.StringVar()
        panel = tk.Frame(self,)
        panel.bind('<Motion>', self.OnMove) 
        tk.Entry(panel, bg='white', textvariable=self.text).place(x=40, y=12)
        self.posCtrl = tk.Label(panel, text = "Pos:").place(x=10, y=10) 
        panel.pack(fill=tk.BOTH,padx=5, pady=5, expand=1)

    def OnMove(self, event): 
        pos = self.winfo_pointerxy()
        self.text.set(pos)
    
if __name__ == '__main__':
    app = MyFrame()
    app.mainloop()
