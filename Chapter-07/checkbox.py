#!/usr/bin/python3
import tkinter as tk

class ComboBoxFrame(tk.Frame):
    def __init__(self, app):
        super().__init__()

        panel = tk.Frame()
        tk.Checkbutton(panel,text ='Alpha',).place(x=35, y=40)
        tk.Checkbutton(panel, text ='Beta',).place(x=35, y=60)
        tk.Checkbutton(panel, text ='Gamma',).place(x=35, y=80) 
        panel.pack(fill=tk.BOTH, expand=1)
                 
def main():
    app = tk.Tk()
    app.geometry("150x200")
    app.title('Checkbox Example')
    ComboBoxFrame(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
