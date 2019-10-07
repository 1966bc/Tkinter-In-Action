#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox

class MyFrame(tk.Frame):
    def __init__(self, ):
        super().__init__()

        self.pack(fill=tk.BOTH, expand=1)
        self.init_menu()
   

    def init_menu(self):

        m_main = tk.Menu(self.master, bd = 1)
        m_file = tk.Menu(m_main, tearoff=0, bd = 1)
        s_menu = tk.Menu(m_file)

        m_main.add_cascade(label="Simple Menu", underline=0, menu=m_file)
        m_file.add_command(label="Simple menu item", underline=0, command=self.OnSimple)
        m_file.add_separator()
        m_file.add_command(label="Exit", underline=0, command=self.OnExit)
        
        self.master.config(menu=m_main)

    def OnSimple(self):
        messagebox.showwarning("", "You selected the simple menu item",)
        
    def OnExit(self,):
        self.master.destroy()  


def main():

    app = tk.Tk()
    app.geometry("300x100")
    app.title('Simple Menu Example')
    frame = MyFrame()
    app.mainloop()


if __name__ == '__main__':
    main()
