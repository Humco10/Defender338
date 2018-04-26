#!/usr/bin/python
#client that works with multiclients erver
#enter into cmd py client.py 127.0.0.1 7474 from the same computer or other computers will have to replace the 127.0.0.1 with the host ip
import socket
import select
import sys
import msvcrt

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Incorrect usage: Please enter in the following format. \nIP, port")
    exit()
    
ip = str(sys.argv[1])
port = int(sys.argv[2])

s.connect((ip, port))

while True:
    socket_list = [s]

    read_sockets = select.select([s], [] , [], 1)[0]
    if msvcrt.kbhit():
        read_sockets.append(sys.stdin)

    for socks in read_sockets+[sys.stdin]:
        if socks == s:
            message = socks.recv(2048).decode()
            print(message)
            break
        else:
            message = input('Enter Message: ')
            s.send(message.encode())
            sys.stdout.write("You: ")
            sys.stdout.write(message + "\n")
            sys.stdout.flush()
s.close()
