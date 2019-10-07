#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox

about_txt = """\
The validator used in this example will ensure that the text
controls are not empty when you press the Ok button, and
will not let you leave if any of the Validations fail."""

class MyDialog:
    def __init__(self, parent):
        super().__init__()

        parent.title('Validators: validating')

        
        self.panel = tk.Frame()
        r =0
        about = tk.Label(self.panel, text=about_txt).grid(row=r, column=0, columnspan=2,sticky=tk.W)

        r +=1
        name_l = tk.Label(self.panel, text="Name:").grid(row=r, column=0, sticky=tk.W)

        r +=1
        name_t = tk.Entry(self.panel, bg="white")
        name_t.grid(row=r, column=1, sticky=tk.W+tk.E)
    
        r +=1
        name_l = tk.Label(self.panel, text="Email:",).grid(row=r, column=0, sticky=tk.W)

        r +=1
        email_t = tk.Entry(self.panel, bg="white")
        email_t.grid(row=r, column=1, sticky=tk.W+tk.E)

        r +=1
        phone_l = tk.Label(self.panel, text="Phone:",).grid(row=r, column=0, sticky=tk.W)

        r +=1
        phone_t = tk.Entry(self.panel, bg="white")
        phone_t.grid(row=r, column=1, sticky=tk.W+tk.E)

        r +=1
        tk.Button(self.panel, text="OK", width = 8, command=self.OnSave).grid(row=r, column=1, sticky=tk.W, padx=5)
        tk.Button(self.panel, text="Cancel", width = 8).grid(row=r, column=1,sticky=tk.E, padx=5)

        self.panel.pack(fill=tk.BOTH, expand=1)


    def OnSave(self, evt=None):

        if self.on_fields_control(self) == False: return        


    def on_fields_control(self, container):

        msg = "Please fill all fields."

        for w in self.panel.winfo_children():
            if type(w) in(tk.Entry,):
                if not w.get():
                    w.focus()
                    w.configure({"background": "pink"})
                    messagebox.showwarning("Error", "This field must contain some text!",)
                    return 0
                             
      
def main():
    app = tk.Tk()
    MyDialog(app)
    app.mainloop()
    
if __name__ == '__main__':
    main()
