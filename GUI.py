
from tkinter import *

class Convert(Frame):
    """Sets up window and widgets"""
    def __init__(self):
        Frame.__init__(self)
        self.canvas=Canvas(self, width=200,height=200, bg ="white")
        self.canvas.grid(row=0, column=0)
        
        self.master.title("Client")
        Frame(self.master,width=200,height=100)
        self.grid()
        self.grid(sticky= N+S+E+W)
        
        #Label Field for textBox
        self._fLabel=Label(self,)
        self._fLabel.grid(row=1, column=0)
        self._fVar=DoubleVar()
        self._fVar.set("")
        self._fEntry=Entry(self, textvariable=self._fVar, justify="center")
        self._fEntry.grid(row=2, column=0)

        #Command button 1
        self._button=Button(self, text="Send")
        self._button.grid(row=3, column=0,columnspan=2)
        #self._button.pack(side=BOTTOM, anchor=S)
def main():
    """Instantiate and pop up the window"""
    Convert().mainloop()

main()
        
        
