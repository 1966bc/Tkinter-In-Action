#!/usr/bin/python3
import tkinter as tk

class DoubleEventFrame(tk.Frame):
    def __init__(self):
        super().__init__()

        self.pack(fill=tk.BOTH, expand=1)
        
        panel = tk.Frame(self,)

        self.button = tk.Button(panel, text="Click Me",relief=tk.RAISED)
        self.button.place(x=100, y=15)
        self.button.bind("<Button-1>", self.OnButtonClick)
        self.button.bind("<B1-Motion>", self.OnMouseDown)
        
        panel.pack(fill=tk.BOTH, expand=1)

    def OnButtonClick(self, event):
        self.button["bg"]="green"
   
    def OnMouseDown(self, event):
        self.button["text"]="Again!"
        

def main():

    app = tk.Tk()
    app.geometry("300x100")
    app.title('Frame With Button')
    frame = DoubleEventFrame()
    app.mainloop()


if __name__ == '__main__':
    main()
