#!/usr/bin/python3
import os
import tkinter as tk
from tkinter import messagebox

class MyFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.init_menu()
        self.init_toolbar()
        self.init_status_bar()

    def init_menu(self):

        m_main = tk.Menu(self, bd = 1)
        m_file = tk.Menu(m_main, tearoff=0, bd = 1)
        m_edit = tk.Menu(m_main, tearoff=0, bd=1)
        s_menu = tk.Menu(m_file)

        m_main.add_cascade(label="File", underline=0, menu=m_file)
        m_main.add_cascade(label="Edit", underline=0, menu=m_edit)

        m_edit.add_command(label="Copy",underline=0,)
        m_edit.add_command(label="Cut",underline=1,)
        m_edit.add_command(label="Paste",underline=0,)
        m_edit.add_separator()
        m_edit.add_command(label="Options", underline=0,)
        
        self.parent.config(menu=m_main)

    def init_toolbar(self):

        toolbar = tk.Frame(self, bd=1, relief=tk.RAISED)

        img_exit = tk.PhotoImage(file=os.path.join('icons', 'exit.png'))
        img_info = tk.PhotoImage(file=os.path.join('icons', 'info.png'))

        exitButton = tk.Button(toolbar,width=20, image=img_exit, relief=tk.FLAT, command=self.OnCloseMe)
        infoButton = tk.Button(toolbar,width=20, image=img_info, relief=tk.FLAT, command=self.OnAbout)
        
        exitButton.image = img_exit
        infoButton.image = img_info

        exitButton.pack(side=tk.LEFT, padx=2, pady=2)
        infoButton.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.TOP, fill=tk.X)        

    def init_status_bar(self):

        statusbar = tk.Label(self, text="Copy in status bar!", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    def OnCloseMe(self,):
        self.parent.destroy()
        
    def OnAbout(self):
        messagebox.showinfo("This is a wxPython Hello world sample", "Welcome to wxPython!", parent=self)
  
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Toolbars')
        self.geometry('300x300') 
        self.protocol("WM_DELETE_WINDOW", self.OnCloseWindow)
        frame = MyFrame(self,)
        frame.pack(fill=tk.BOTH, expand=1)
        
    def OnCloseWindow(self):
        self.destroy()               
    
if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
