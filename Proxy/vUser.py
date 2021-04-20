# Import socket module
import socket
from vHSS import get_string

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 11000

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server
# print(s.recv(1024))
send_login_info = get_string()
s.send(send_login_info.encode())
received_binary = s.recv(1024)
print("Received Auth. Vector: " + received_binary.decode())
# close the connection
s.close()
