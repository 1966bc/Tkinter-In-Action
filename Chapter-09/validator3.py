#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox

about_txt = """\
The validator used in this example will validate the input on the fly
instead of waiting until the okay button is pressed.  The first field
will not allow digits to be typed, the second will allow anything
and the third will not allow alphabetic characters to be entered.
"""

class MyDialog:
    def __init__(self, parent):
        super().__init__()

        parent.title('Validators: validating')

        self.name = tk.StringVar()
        self.name.trace('w', self.validate_alpha)

        self.phone = tk.StringVar()
        self.phone.trace('w', self.validate_isdigit)
             
        self.panel = tk.Frame()
        r =0
        about = tk.Label(self.panel, text=about_txt).grid(row=r, column=0, columnspan=2,sticky=tk.W)

        r +=1
        name_l = tk.Label(self.panel, text="Name:").grid(row=r, column=0, sticky=tk.W)

        r +=1
        name_t = tk.Entry(self.panel, bg="white", textvariable = self.name)
        name_t.grid(row=r, column=1, sticky=tk.W+tk.E)
    
        r +=1
        name_l = tk.Label(self.panel, text="Email:",).grid(row=r, column=0, sticky=tk.W)

        r +=1
        email_t = tk.Entry(self.panel, bg="white")
        email_t.grid(row=r, column=1, sticky=tk.W+tk.E)

        r +=1
        phone_l = tk.Label(self.panel, text="Phone:",).grid(row=r, column=0, sticky=tk.W)

        r +=1
        phone_t = tk.Entry(self.panel, bg="white",  textvariable = self.phone)
        phone_t.grid(row=r, column=1, sticky=tk.W+tk.E)

        r +=1
        tk.Button(self.panel, text="OK", width = 8,).grid(row=r, column=1, sticky=tk.W, padx=5)
        tk.Button(self.panel, text="Cancel", width = 8).grid(row=r, column=1,sticky=tk.E, padx=5)

        self.panel.pack(fill=tk.BOTH, expand=1)


    def validate_alpha(self, *args):
        if not self.name.get().isalpha():
            corrected = ''.join(filter(str.isalpha, self.name.get()))
            self.name.set(corrected)

    def validate_isdigit(self, *args):
        if not self.phone.get().isdigit():
            corrected = ''.join(filter(str.isdigit, self.phone.get()))
            self.phone.set(corrected)                 


  
                             
def main():
    app = tk.Tk()
    MyDialog(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
