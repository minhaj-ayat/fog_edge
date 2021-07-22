# Import socket module
import codecs
import socket
from _thread import *
import threading
from vHSS import get_string

def threaded(c):
    received_imsi = c.recv(1024)
    print(received_imsi)
    #c.send("Got it".encode())

    # Create a socket object
    fogs = socket.socket()

    # Define the port on which you want to connect
    port = 11000

    # connect to the server on local computer
    fogs.connect(('127.0.0.1', port))

    # receive data from the server
    # print(s.recv(1024))
    #send_login_info = get_string(received_imsi)
    fogs.send(received_imsi)
    received_binary = fogs.recv(1024)
    print("Received Auth. Vector from fog : " + received_binary.decode())
    c.send(received_binary)
    print("Sent Auth. Response to MME: " + received_binary.decode())
    print_lock.release()
    # close the connection
    fogs.close()


print_lock = threading.Lock()
mmesock = socket.socket()
print("Proxy Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 13000

mmesock.bind(('', port))
print("Proxy socket binded to %s" % port)

# put the socket into listening mode
mmesock.listen(5)
print("Proxy socket is listening")

while True:
    cl, addr = mmesock.accept()
    print_lock.acquire()
    print('Got connection from', addr)
    start_new_thread(threaded, (cl,))
