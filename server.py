#!/usr/bin/python
#multiclient handling server
#just double click to launch
import socket
import select
import sys
import _thread as thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);

    
ip = "127.0.0.1"
port = 7474

s.bind((ip, port))   #binds the server to the given ip and port

s.listen(50)   #listens for 50 active connections

client_list = []  #list of clients

def acceptclient(connection, address):
   connection.send(b"Welcome to the chat!")
   while True:
       try:
           message = connection.recv(2048).decode()
           if(message):
               message = (address[0] + ": " + message)
               print(message)
               broadcast(message, connection)
           else:
               remove(connection)
       except:
           continue


        
def broadcast(message, connection):
   for client in client_list:
      if client != connection:
         try:
            client.send(message).encode()    #send the message to all other clients but the one that send it
         except:
            client.close()
            remove(client)

            
def remove(connection):
   if conection in client_list:
      client_list.remove(connection)

while True:
   print("Awaiting connection...")
   connection, address = s.accept()  #accepts the connection of the client

   client_list.append(connection)      #adds client to client_list


   print(address[0] + " Connected.")

   thread.start_new_thread(acceptclient, (connection,address))

connection.close()
s.close()
