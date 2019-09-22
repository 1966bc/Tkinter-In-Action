#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
import images


class ShapedFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        parent.title('Shaped Window')
 
        panel = tk.Frame()

        img = tk.PhotoImage(data=images.getVippiData())

        w = ttk.Label(panel, image=img)

        w.image = img

        w.pack()

        panel.pack(fill=tk.BOTH, expand=1)

    def OnExit(self,):
        self.destroy()
      
def main():
    app = tk.Tk()
    ShapedFrame(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
