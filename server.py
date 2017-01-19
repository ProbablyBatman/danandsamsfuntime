import socket               # Import socket module
from threading import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = ''
PORT = 2718

global CLIENT_LIST
CLIENT_LIST = []
s.bind((HOST, PORT))
global displayMessages
def broadcast(c, msg):
    c.send(bytes(msg, 'utf-8'))

def handle_client(c,addr):
    displayMessages = []
    while 1:

        fragments = []
        try:
            data = c.recv(1024)
        except:
            print(addr, " has disconnected.")
            CLIENT_LIST.remove(c)
            break

        fragments.append(data.decode())
        message = "".join(fragments)

        """
        for client in CLIENT_LIST:                          #This code will send data back to the client
            broadcast(client, message)

        """
        message = ""
    c.close()
    return
s.listen(5)                 # Now wait for client connection.
print("Listening on port ", PORT)
while True:
    c, addr = s.accept()
    print("Got connection from ", addr)
    CLIENT_LIST.append(c)
    t = Thread(target=handle_client, args=(c,addr)).start()
