#!/usr/bin/python3
import sys
import tkinter as tk

class Frame(tk.Frame):
    def __init__(self, parent):
        print ("Frame __init__")
        super().__init__()

class App(tk.Tk):
    def __init__(self):
        print ("App __init__")
        super().__init__()

        self.protocol("WM_DELETE_WINDOW", self.OnExit)
        self.geometry("300x300")
        self.OnInit()

    def OnInit(self):
        print ("OnInit")
        self.title("Startup")
        frame = Frame(self,)
        print (sys.stderr, "A pretend error message")
        frame.pack(fill=tk.BOTH, expand=1)
    
    def OnExit(self):
        print ("OnExit")
        self.destroy()               
    
if __name__ == '__main__':
    app = App()
    print ("before MainLoop")
    fred = app.mainloop()
    print ("after MainLoop", fred)
