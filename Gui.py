from tkinter import *

class Convert(Frame):
    """Sets up window and widgets"""
    def __init__(self):
        
        Frame.__init__(self)
        self.master.title("Client")
        Frame(self.master,width=300,height=300)
        self.grid()

        self._tVar = StringVar()
        self.canvas=Text(self, height = 20, width = 50)
        self.canvas.grid(row=0, column=0,columnspan=1)
        self.canvas.configure(state = "disabled")
        
        #Label Field for textBox
        self._fLabel=Label(self,)
        self._fLabel.grid(row=1, column=0)
        self._sVar=StringVar()
        self._sVar.set("")
        self._fEntry=Entry(self, textvariable=self._sVar, justify="center")
        self._fEntry.grid(row=2, column=0)

        #Command button 1
        self._button=Button(self, text="Send", command = self.add_one)
        self._button.grid(row=3, column=0,columnspan=2)
        #self._button.pack(side=BOTTOM, anchor=S)

    def add_one(self):
        self.canvas.configure(state = "normal")
        s = self._sVar.get()
        s += '\n'
        self.canvas.insert(END,s)
        self.canvas.configure(state = "disabled")
        self._sVar.set("")
def main():
    """Instantiate and pop up the window"""
    Convert().mainloop()

main()
