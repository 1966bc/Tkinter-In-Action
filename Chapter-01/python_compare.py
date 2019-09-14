#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class MyFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.init_menu()
        self.init_status_bar()

    def init_menu(self):

        m_main = tk.Menu(self, bd = 1)
        m_file = tk.Menu(m_main, tearoff=0, bd = 1)
        s_menu = tk.Menu(m_file)

        m_main.add_cascade(label="File", underline=0, menu=m_file)
        m_file.add_command(label="About...",underline=0, command=self.OnAbout)
        m_file.add_separator()
        m_file.add_command(label="Exit", underline=0, command=self.parent.OnQuit)
        
        self.parent.config(menu=m_main)

    def init_status_bar(self):

        statusbar = tk.Label(self, text="Welcome to wxPython!", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def OnAbout(self):
        messagebox.showinfo("This is a wxPython Hello world sample", "Welcome to wxPython!", parent=self)
  
class MyApp(tk.Tk):
    """Start here"""

    def __init__(self):
        super().__init__()

        self.title('Hello World')
        self.geometry('450x340+50+60') 
        self.protocol("WM_DELETE_WINDOW", self.OnQuit)
        frame = MyFrame(self,)
        frame.pack(fill=tk.BOTH, expand=1)
        
    def OnQuit(self):
        self.destroy()               
    
if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
