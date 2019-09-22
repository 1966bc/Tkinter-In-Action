#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk


class SketchFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        parent.title('Sketch Frame')
        parent.geometry("800x600")
 
        panel = tk.Frame()

        self.w = tk.Canvas(panel,)

        self.w.bind( "<B1-Motion>", self.paint)

        self.w.pack(expand=tk.YES, fill=tk.BOTH)

        panel.pack(fill=tk.BOTH, expand=1)


    def paint(self, event):
        color = "black"
        x1, y1 = (event.x - 1 ), ( event.y - 1 )
        x2, y2 = (event.x + 1 ), (event.y + 1 )
        self.w.create_oval( x1, y1, x2, y2, fill=color)
      
def main():
    app = tk.Tk()
    SketchFrame(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
