#!/usr/bin/python3
import tkinter as tk

class RefactorExample(tk.Frame):
    def __init__(self,parent ):
        super().__init__()

        self.parent = parent
        panel = tk.Frame(self.parent,  bg="white")
        panel.pack(fill=tk.BOTH, expand=1)

        self.createMenuBar()
        self.createButtonBar(panel)
        self.createTextFields(panel)
        
    def menuData(self):
        return (("File",
                    ("Open", self.OnOpen),
                    ("Quit",self.OnCloseWindow)),
                ("Edit",
                    ("Copy",self.OnCopy),
                    ("Cut", self.OnCut),
                    ("Paste", self.OnPaste),
                    (None),
                    ("Options...", self.OnOptions)))

    def createMenuBar(self):
        #I've simplify.....
        m_main = tk.Menu(self.master, bd = 1)
        
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            sub_menu = tk.Menu(m_main, tearoff=0, bd = 1)
            m_main.add_cascade(label=menuLabel, underline=0, menu=sub_menu)
            for i in eachMenuData:
                # no so good example...:(
                if isinstance(i, tuple):
                    if i is not None:
                        sub_menu.add_command(label=i[0],underline=0, command=i[1])
                    else:
                        sub_menu.add_separator()
            
        self.master.config(menu=m_main)
        
    def buttonData(self):

        return (("First", self.OnFirst),
                ("<< PREV", self.OnPrev),
                ("NEXT >>", self.OnNext),
                ("Last", self.OnLast))

    def createButtonBar(self, panel, yPos = 0):
        xPos = 0
        for eachLabel, eachHandler in self.buttonData():
            pos = (xPos, yPos)
            button = self.buildOneButton(panel, eachLabel, eachHandler, pos)
            #it's impossible using place allign the button
            xPos += 90

    def buildOneButton(self, parent, label, handler, pos=(0,0)):
        #we must set width option because the button widget fill the len of the text option
        button = tk.Button(parent, text=label, width=8, command=handler).place(x=pos[0],y=pos[1])
        return button

    def textFieldData(self):
        return (("First Name", (10, 50)),
                ("Last Name", (10, 80)))

    def createTextFields(self, panel):
        for eachLabel, eachPos in self.textFieldData():
            self.createCaptionedText(panel, eachLabel, eachPos)

    def createCaptionedText(self, panel, label, pos):
        static = tk.Label(panel, text = label, bg="white").place(x=pos[0],y=pos[1])
        textPos = (pos[0] + 75, pos[1])
        tk.Entry(panel, width=10, bg="white").place(x=textPos[0],y=textPos[1])
        
  
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
