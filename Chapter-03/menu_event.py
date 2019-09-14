#!/usr/bin/python3
import tkinter as tk

class MenuEventFrame(tk.Frame):
    def __init__(self, ):
        super().__init__()

        self.pack(fill=tk.BOTH, expand=1)
        self.init_menu()
   

    def init_menu(self):

        m_main = tk.Menu(self.master, bd = 1)
        m_file = tk.Menu(m_main, tearoff=0, bd = 1)
        s_menu = tk.Menu(m_file)

        m_main.add_cascade(label="File", underline=0, menu=m_file)
        m_file.add_command(label="Exit...", underline=0, command=self.OnCloseMe)
        
        self.master.config(menu=m_main)

    def OnCloseMe(self,):
        self.master.destroy()  


def main():

    app = tk.Tk()
    app.geometry("300x100")
    app.title('Menus')
    frame = MenuEventFrame()
    app.mainloop()


if __name__ == '__main__':
    main()
