#!/usr/bin/python3

from tkinter.filedialog import askdirectory

if __name__ == "__main__":

    options = {}

    options['title'] = "Choose a directory:"

    options['initialdir'] = "/"
   
    dialog = askdirectory(**options)

    print('You selected: {0}\n'.format(dialog))

   


