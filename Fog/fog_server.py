import socket
from _thread import *
import threading
from django.forms.models import model_to_dict
import sys

'''print(sys.path)'''
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FogEdge.settings')
import django

django.setup()
from Fog.models import UserInfo


def threaded(c):
    # send a thank you message to the client.
    # st = 'Thank you for connecting'
    # c.send(st.encode())
    received_login_info = c.recv(1024).decode()
    print("Received info : " + received_login_info)
    sep_str = received_login_info.split()
    uid = sep_str[1]
    pwd = sep_str[2]
    imsi = sep_str[0]

    if UserInfo.objects.filter(loginid=uid).exists() and UserInfo.objects.filter(passwd=pwd).exists():
        auth_vector = UserInfo.objects.get(loginid=uid)
        av = model_to_dict(auth_vector)
        st = ""
        for key, value in av.items():
            if key == "autn" or key == "rand" or key == "xres" or key == "kasme":
                st += str(value) + " "
        print("Sent Auth. vector : " + st)
        print_lock.release()
        c.send(st.encode())
    # Close the connection with the client
    c.close()


print_lock = threading.Lock()
# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 11000

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" % port)

# put the socket into listening mode
s.listen(5)
print("socket is listening")

# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    cl, addr = s.accept()
    print_lock.acquire()
    print('Got connection from', addr)
    start_new_thread(threaded, (cl,))
