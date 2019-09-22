#!/usr/bin/python3
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class TextFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        parent.title('Text Entry Example')
        parent.geometry("300x250")
        
        panel = tk.Frame()

        multiLabel = tk.Label(panel, text="Multi-line").grid(row=0, column=0, sticky=tk.N)
        multiText = ScrolledText(panel, bg='white', height=5, width=20,)
        
        s = "Here is a looooooooooooooong line of text set in the control.\n\nSee that it wrapped, and that this line is after a blank"
        multiText.insert(tk.END, s)
    
        multiText.grid(row=0, column=1, sticky=tk.W+tk.E)

        richLabel = tk.Label(panel, text="Multi-line").grid(row=1, column=0, sticky=tk.N)
        richText = tk.Text(panel, bg='white', height=8, width=20)
        richText.grid(row=1, column=1, sticky=tk.W+tk.E)
        s =  "If supported by the native control, this is reversed, and this is a different font."

        richText.tag_configure('color', foreground='blue', font=('Helvetica italic ', 12, 'underline bold'))
        richText.tag_configure('reverse', foreground='white', background='black',)

        s = "If supported by the native control, this is "
        richText.insert(tk.END,s)
        
        richText.insert(tk.END,'reversed', 'reverse')
        
        s = ", and this is a "
        richText.insert(tk.END,s)
        
        s = " different font"
        richText.insert(tk.END, s, 'color')

        panel.pack(fill=tk.BOTH, expand=1)
      
def main():
    app = tk.Tk()
    TextFrame(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
