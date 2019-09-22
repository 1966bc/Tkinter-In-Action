#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk


class SketchFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        parent.title('Sketch Frame')
        parent.geometry("800x600")
        self.statusbar_text = tk.StringVar()
        self.statusbar_text.set("Welcome to wxPython!")
        
        panel = tk.Frame()

        self.w = tk.Canvas(panel,)

        self.w.bind( "<B1-Motion>", self.OnSketchMotion)

        self.w.pack(expand=tk.YES, fill=tk.BOTH)

        statusbar = tk.Label(panel, textvariable=self.statusbar_text, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)

        panel.pack(fill=tk.BOTH, expand=1)


    def OnSketchMotion(self, event):
        color = "black"
        x1, y1 = (event.x - 1 ), ( event.y - 1 )
        x2, y2 = (event.x + 1 ), (event.y + 1 )
        self.w.create_oval( x1, y1, x2, y2, fill=color)
        pos = self.winfo_pointerxy()
        s = "Pos x1: {0} Pos y1: {1} Pos x2: {2} Pos y2: {3} winfo_pointerxy(): {4}".format(x1,y1,x2,y2,pos)  
        self.statusbar_text.set(s)
        
      
def main():
    app = tk.Tk()
    SketchFrame(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
