import socket
from _thread import *
import threading
from vector_gen import generate_vector, print_buffer2
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
    received_login_info = c.recv(1024)
    print(received_login_info)
    #sep_str = received_login_info.split()
    #imsi = sep_str[0]
    #uid = sep_str[1]
    #pwd = sep_str[2]
    #key = sep_str[1]
    #op = sep_str[2]
    #r = sep_str[3]
    #sq = sep_str[4]
    #pl = sep_str[5]


    '''if UserInfo.objects.filter(loginid=uid).exists() and UserInfo.objects.filter(passwd=pwd).exists():
        auth_vector = UserInfo.objects.get(loginid=uid)
        av = model_to_dict(auth_vector)
        st = ""
        for key, value in av.items():
            if key == "autn" or key == "rand" or key == "xres" or key == "kasme":
                st += str(value) + " " '''
    #val = generate_vector(key, op, r, sq, pl)
    #print("Sent Auth. vector : " + st)
    #print_lock.release()
    #c.send(st.encode())
    rrand = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    rxres = [0] * 8
    rautn = generate_vector(rrand, rxres)
    rautn = print_buffer2(rautn)
    rxres = print_buffer2(rxres)
    print(rautn)
    print(rxres)
    reply = rautn + " " + rxres
    c.send(reply.encode())
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
