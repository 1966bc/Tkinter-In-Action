#!/usr/bin/python3

from tkinter import filedialog

if __name__ == "__main__":
   
    dialog = filedialog.askopenfilename(initialdir = "/",
                                        title = "Choose a file",
                                        filetypes = (("Python source","*.py"),
                                                     ("All files","*.*")))

    print('You selected: {0}\n'.format(dialog))

   


