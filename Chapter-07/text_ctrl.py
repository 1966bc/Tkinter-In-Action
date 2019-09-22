#!/usr/bin/python3
import tkinter as tk

class TextFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        parent.title('Text Entry Example')
        parent.geometry("300x100")
        
        panel = tk.Frame()

        basicLabel = tk.Label(panel, text="Basic Control:").grid(row=0, column=0, sticky=tk.W)
        basicText = tk.Entry(panel, bg="white")
        basicText.grid(row=0, column=1, sticky=tk.W+tk.E)
        basicText.insert(0, "I've entered some text!")
        
        pwdLabel = tk.Label(panel, text="Password:",).grid(row=1, column=0, sticky=tk.W)
        pwdText = tk.Entry(panel, bg="white", show="*")
        pwdText.grid(row=1, column=1, sticky=tk.W+tk.E)
        pwdText.insert(0, "password")
       
        panel.pack(fill=tk.BOTH, expand=1)
      
def main():
    app = tk.Tk()
    TextFrame(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
