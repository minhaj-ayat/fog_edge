# Import socket module
import socket
from vHSS import get_string


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
    c, addr = mmesock.accept()
    print('Got connection from', addr)
    received_imsi = c.recv(1024).decode()
    print("Received info : " + received_imsi)

    # Create a socket object
    fogs = socket.socket()

    # Define the port on which you want to connect
    port = 11000

    # connect to the server on local computer
    fogs.connect(('127.0.0.1', port))

    # receive data from the server
    # print(s.recv(1024))
    send_login_info = get_string(received_imsi)
    fogs.send(send_login_info.encode())
    received_binary = fogs.recv(1024)
    print("Received Auth. Vector from fog : " + received_binary.decode())
    c.send(received_binary)
    print("Sent Auth. Response to MME: " + received_binary.decode())
    # close the connection
    fogs.close()

