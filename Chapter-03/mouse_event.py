#!/usr/bin/python3
import tkinter as tk

class MouseEventFrame(tk.Frame):
    def __init__(self):
        super().__init__()

        self.pack(fill=tk.BOTH, expand=1)
        
        self.panel = tk.Frame(self,)

        self.button = tk.Button(self.panel, text="Not Over",relief=tk.RAISED)
        self.button.place(x=100, y=15)
        self.button.bind("<Button-1>", self.OnButtonClick)
        self.button.bind("<Enter>", self.OnEnterWindow)
        self.button.bind("<Leave>", self.OnLeaveWindow)
        
        self.panel.pack(fill=tk.BOTH, expand=1)

    def OnButtonClick(self, event):
        self.panel["bg"]="green"

    def OnEnterWindow(self, event):
        self.button["text"]="Over Me!"
   
    def OnLeaveWindow(self, event):
        self.button["text"]="Not Over"
        

def main():

    app = tk.Tk()
    app.geometry("300x100")
    app.title('Frame With Button')
    frame = MouseEventFrame()
    app.mainloop()


if __name__ == '__main__':
    main()
