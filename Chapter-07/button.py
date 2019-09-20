#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

class ButtonFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        panel = tk.Frame()
        self.button = ttk.Button(panel, text="Hello", command=self.OnClick)
        self.button.place(x=50, y=20)
        panel.pack(fill=tk.BOTH, expand=1)

    def OnClick(self, event=None):
        self.button["text"] ="Clicked"
                   
def main():
    app = tk.Tk()
    app.geometry("300x100")
    app.title('Button Example')
    ButtonFrame(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
