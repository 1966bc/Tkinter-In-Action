#!/usr/bin/python3
from tkfontchooser import askfont

if __name__ == "__main__":
   
    dialog = askfont()

    print('You selected: {0}\n'.format(dialog))

   


