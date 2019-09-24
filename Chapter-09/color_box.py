#!/usr/bin/python3

from tkinter import colorchooser

if __name__ == "__main__":
   
    dialog = colorchooser.askcolor()

    print('You selected: {0}\n'.format(dialog))

   


