#!/usr/bin/python3
import tkinter as tk

class RefactorExample(tk.Frame):
    def __init__(self,parent ):
        super().__init__()

        
        self.parent = parent

        panel = tk.Frame(self.parent,  bg="white")

        prevButton = tk.Button(panel, text="<< PREV",  command=self.OnPrev).place(x=50, y=0)
        nextButton = tk.Button(panel, text="NEXT >>",command=self.OnNext ).place(x=130, y=0)
        
        
        panel.pack(fill=tk.BOTH, expand=1)
     

        m_main = tk.Menu(self.master, bd = 1)
        m_file = tk.Menu(m_main, tearoff=0, bd = 1)
        s_menu = tk.Menu(m_file)
        m_edit = tk.Menu(m_main, tearoff=0, bd=1)

        m_main.add_cascade(label="File", underline=0, menu=m_file)
        m_main.add_cascade(label="Edit", underline=0, menu=m_edit)
        m_file.add_command(label="Open", underline=0, command=self.OnOpen)
        m_file.add_command(label="Quit", underline=0, command=self.OnCloseWindow)

        m_edit.add_command(label="Copy",underline=0,command=self.OnCopy)
        m_edit.add_command(label="Cut",underline=1,command=self.OnCut)
        m_edit.add_command(label="Paste",underline=0,command=self.OnPaste)
        
        
        self.master.config(menu=m_main)


        static = tk.Label(panel, text = "First Name", bg="white").place(x=10, y=50)
        #tk.Entry doesn't have property of "height"
        text = tk.Entry(panel, width=10, bg="white").place(x=80, y=50)

        static2 = tk.Label(panel, text = "Last Name", bg="white").place(x=10, y=80)
        #tk.Entry doesn't have property of "height"
        text2 = tk.Entry(panel, width=10, bg="white").place(x=80, y=80)
        
        firstButton = tk.Button(panel, text="FIRST",  command=self.OnFirst).place(x=0, y=0)
        lastButton = tk.Button(panel, text="LAST",  command=self.OnLast).place(x=210, y=0)

        m_edit.add_separator()
        m_edit.add_command(label="Options", underline=0, command=self.OnOptions)


    def OnPrev(self, event): pass
    def OnNext(self, event): pass
    def OnLast(self, event): pass
    def OnFirst(self, event): pass
    def OnOpen(self, event): pass
    def OnCopy(self, event): pass
    def OnCut(self, event): pass
    def OnPaste(self, event): pass
    def OnOptions(self, event): pass
        

    def OnCloseWindow(self,):
        self.master.destroy()  


def main():

    app = tk.Tk()
    app.geometry("340x200")
    app.title('Refactor Example')
    frame = RefactorExample(app)
    app.mainloop()


if __name__ == '__main__':
    main()
