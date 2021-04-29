import socket


mmes = socket.socket()
# Define the port on which you want to connect
port = 12000

# connect to the server on local computer
mmes.connect(('127.0.0.1', port))

imsi = "111501234512345"
mmes.send(imsi.encode())
print("UE sent attach request : " + imsi)

challenge = mmes.recv(1024).decode()
print("UE received challenge from MME : " + challenge)

res = "a54211d5e3ba50bf"
mmes.send(res.encode())
print("UE sent RES to MME : " + res)

msg = mmes.recv(1024).decode()
print("Msg from MME : " + msg)
