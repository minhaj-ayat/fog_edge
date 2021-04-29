import socket
from _thread import *
import threading


def threaded(c):
    received_imsi = c.recv(1024).decode()
    print("Received imsi from UE : " + received_imsi)

    # Create a socket object
    proxys = socket.socket()
    # Define the proxy port on which you want to connect
    port = 13000
    # connect to the server on local computer
    proxys.connect(('127.0.0.1', port))
    proxys.send(received_imsi.encode())

    auth_vector = proxys.recv(1024)
    print("MME received auth_response: " + auth_vector.decode())

    sep_str = auth_vector.decode().split()
    auth_challenge = sep_str[0] + " " + sep_str[1]
    xres = sep_str[2]

    c.send(auth_challenge.encode())
    print("MME sent auth_challenge to UE : " + auth_challenge)
    # close the connection
    proxys.close()

    received_res = c.recv(1024)
    print("MME received RES from UE : " + received_res.decode())

    if xres == received_res.decode():
        success = "200 ok"
        c.send(success.encode())
        print("Authentication successful")
    else:
        failure = "Authentication failed"
        c.send(failure.encode())

    print_lock.release()
    # Close the connection with the client
    c.close()


print_lock = threading.Lock()
ues = socket.socket()
print("Edge Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12000

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
ues.bind(('', port))
print("Edge socket binded to %s" % port)

# put the socket into listening mode
ues.listen(5)
print("Edge socket is listening")

while True:
    # Establish connection with UE.
    cl, addr = ues.accept()
    print_lock.acquire()
    print('Got connection from UE', addr)
    start_new_thread(threaded, (cl,))
