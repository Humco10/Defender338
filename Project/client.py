"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import sys
from tkinter import *

class GUI(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("ChatApp")
        Frame(self.master,width=300,height=300)
        self.grid()
        self._msg = StringVar()
        self._msg.set("Type Message Here:")
        #messages_frame = Frame(top) # top = tkinter.tk()
        scrollbar = Scrollbar(self)  # To navigate through past messages.
        # Following will contain the messages.
        self.canvas=Text(self, height = 20, width = 50)
        self.canvas.grid(row=0, column=0,columnspan=1)
        #self._msg_list.pack(side=LEFT, fill=BOTH)
        #self._msg_list.pack()
        #self._messages_frame.pack()

        self._entry_field = Entry(self, textvariable=self._msg)
        self._entry_field.bind("<Return>", send)
        self._entry_field.grid(row = 1, column = 0, columnspan = 1)
        #self._entry_field.pack()
        self._send_button = Button(self, text="Send", command=self.send)
        self._send_button.grid(row   = 2, column = 0, columnspan = 1)
        #self._send_button.pack()

        #self.protocol("WM_DELETE_WINDOW", on_closing)
    def send(self,event=None):  # event is passed by binders.
        """Handles sending of messages."""
        msg = self._msg.get()
        self._msg.set("")  # Clears input field.
        client_socket.send(bytes(msg, "utf8"))
        if msg == "QUIT":
            client_socket.close()
            quit()


gui = GUI()
def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            gui.canvas.insert(END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    self._msg.set("QUIT")
    send()

#----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 3000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()


GUI().mainloop()  # Starts GUI execution.


