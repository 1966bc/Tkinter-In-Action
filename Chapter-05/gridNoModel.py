#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()

        
        self.title("Grid")
        self.init_ui()

    def init_ui(self):

        #tkinte doesn't have a grid widget but we can use the powerfull ttk.Treeview....

        f = ttk.Frame(self, padding=8)

        cols = (["#0",'','w',False,50,50, 'gray'],
                ["#1",'First','w',False,50,50],
                ["#2",'Last','w',False,50,50],)
        
        self.MyGrid = self.get_tree(f, cols,10)

       
        f.pack(fill=tk.BOTH,padx=5, pady=5, expand=1)

        self.set_values()


    def set_values(self,):

        data = (("CF", "Bob", "Dernier"), ("2B", "Ryne", "Sandberg"),
                ("LF", "Gary", "Matthews"), ("1B", "Leon", "Durham"),
                ("RF", "Keith", "Moreland"), ("3B", "Ron", "Cey"),
                ("C", "Jody", "Davis"), ("SS", "Larry", "Bowa"),
                ("P", "Rick", "Sutcliffe"))


        for i in data:
            self.MyGrid.insert('', tk.END,
                                       iid=i[0],
                                       text=i[0],
                                       values=(i[1],i[2]),)            



    def get_tree(self, container, cols, size=None, show=None):

        ttk.Style().configure("Treeview.Heading", font=('Helvetica', 12, 'bold' ))

        headers = []

        for col in cols:
            headers.append(col[1])
        del headers[0]

        if show is not None:
            w = ttk.Treeview(container,show=show)

        else:
            w = ttk.Treeview(container,)
              
        w['columns']=headers
          
        for col in cols:
            w.heading(col[0], text=col[1], anchor=col[2],)
            w.column(col[0], anchor=col[2], stretch=col[3],minwidth=col[4], width=col[5])
           
        sb = ttk.Scrollbar(container)
        sb.configure(command=w.yview)
        w.configure(yscrollcommand=sb.set)


        w.pack(side=tk.LEFT, fill=tk.BOTH, expand =1)
        sb.pack(fill=tk.Y, expand=1)

        return w        
                        
if __name__ == '__main__':
    app = App()
    app.mainloop()
