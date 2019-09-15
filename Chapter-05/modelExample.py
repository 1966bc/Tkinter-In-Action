#!/usr/bin/python3
import tkinter as tk
import abstractmodel


class SimpleName(abstractmodel.AbstractModel):
    
    def __init__(self, first="", last=""):
        abstractmodel.AbstractModel.__init__(self)
        self.set(first, last)
        
    def set(self, first, last):
        self.first = first
        self.last = last
        self.update()
        
class ModelExample(tk.Frame):
    def __init__(self,parent ):
        super().__init__()

        self.parent = parent
        panel = tk.Frame(self.parent,  bg="white")
        panel.pack(fill=tk.BOTH, expand=1)

        self.textFields = {}
        self.model = SimpleName()
        self.model.addListener(self.OnUpdate)  
        self.createButtonBar(panel)
        self.createTextFields(panel)
        
    def buttonData(self):

        return (("Fredify", self.OnFred),
                ("Wilmafy", self.OnWilma),
                ("Barnify", self.OnBarney),
                ("Bettify", self.OnBetty))

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
        self.textFields[label] = tk.Entry(panel, width=10, bg="white")
        self.textFields[label].place(x=textPos[0],y=textPos[1])


    def OnUpdate(self, model):
        #if we use a direct assignment we must first delete all in the entry
        # in a really tk project we would use the tracing of some special variables as StringVar()
        self.textFields["First Name"].delete(0,tk.END)
        self.textFields["Last Name"].delete(0,tk.END)
        #so we can write
        self.textFields["First Name"].insert(0,model.first)
        self.textFields["Last Name"].insert(0,model.last)
                   
    def OnFred(self, event=None):                                   
        self.model.set("Fred", "Flintstone")                   
                                                               
    def OnBarney(self, event=None):                                 
        self.model.set("Barney", "Rubble")                     
                                                               
    def OnWilma(self, event=None):                                  
        self.model.set("Wilma", "Flintstone")                  
                                                               
    def OnBetty(self, event=None):                                  
        self.model.set("Betty", "Rubble")           
                
    def OnCloseWindow(self,):
        #it's not really necessary
        self.master.destroy()  

def main():

    app = tk.Tk()
    app.geometry("340x200")
    app.title('Flintstones')
    frame = ModelExample(app)
    app.mainloop()

if __name__ == '__main__':
    main()
