#!/usr/bin/python3
import tkinter as tk

class InsertFrame(tk.Frame):
    def __init__(self):
        super().__init__()

        self.pack(fill=tk.BOTH, expand=1)
        
        panel = tk.Frame(self,)
        #original size=(50, 50)
        button = tk.Button(panel, text="Close",height=3, width=3, relief=tk.RAISED)
        button.place(x=125, y=10)
        button.bind("<Button-1>", self.OnCloseMe)
        self.master.protocol("WM_DELETE_WINDOW", self.OnCloseWindow)
      
        panel.pack(fill=tk.BOTH, expand=1)

    def OnCloseMe(self, event):
        self.master.destroy()

    def OnCloseWindow(self,):
        self.master.destroy()       

def main():

    app = tk.Tk()
    app.geometry("300x80")
    app.title('Frame With Button')
    frame = InsertFrame()
    app.mainloop()


if __name__ == '__main__':
    main()
