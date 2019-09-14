#!/usr/bin/python3
"""Hello, wxPython! program."""
import tkinter as tk
from PIL import ImageTk, Image

class Main(tk.Frame):
    """Frame class that displays an image."""
    def __init__(self, parent, image):
        super().__init__()
        """Create a Frame instance and display image."""
        self.pack(fill=tk.BOTH, expand=1)
        self.parent = parent
        self.parent.title('Hello, wxPython!')
        width, height = image.size
        self.bmp = tk.Label(self,)
        photo = ImageTk.PhotoImage(image)
        self.bmp.config(image=photo)
        self.bmp.image = photo
        self.bmp.pack(fill=tk.BOTH,expand=1)                                    
        self.parent.geometry("{0}x{1}".format(width, height))
      
class App(tk.Tk):
    """Application class."""
    def __init__(self):
        super().__init__()
        image = Image.open('wxPython.jpg')
        self.frame = Main(self,image)
        
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()
    
