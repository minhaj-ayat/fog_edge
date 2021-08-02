import codecs
import datetime
import socket
from _thread import *
import threading
from vector_gen import generate_vector, print_buffer2, generate_random
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
    print(datetime.datetime.now())
    # sep_str = received_login_info.split()
    # imsi = sep_str[0]
    # uid = sep_str[1]
    # pwd = sep_str[2]
    # key = sep_str[1]
    # op = sep_str[2]
    # r = sep_str[3]
    # sq = sep_str[4]
    # pl = sep_str[5]

    '''if UserInfo.objects.filter(loginid=uid).exists() and UserInfo.objects.filter(passwd=pwd).exists():
        auth_vector = UserInfo.objects.get(loginid=uid)
        av = model_to_dict(auth_vector)
        st = ""
        for key, value in av.items():
            if key == "autn" or key == "rand" or key == "xres" or key == "kasme":
                st += str(value) + " " '''
    # val = generate_vector(key, op, r, sq, pl)
    # print("Sent Auth. vector : " + st)
    # print_lock.release()
    # c.send(st.encode())
    # rrand = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ans = codecs.encode(received_login_info, 'hex')
    dk = ans.decode()
    print(dk)
    rand = [0] * 16
    for i in range(0, 31, 2):
        rand[int(i / 2)] = int(dk[i:i + 2], 16)

    print("Received Rand: ")
    print(rand)
    ak = [0] * 6
    ck = [0] * 16
    ik = [0] * 16
    rxres = [0] * 8
    rautn = generate_vector(rand, rxres, ak, ck, ik)
    rautn = ",".join(map(str, (rautn)))
    rxres = ",".join(map(str, (rxres)))
    ck = ",".join(map(str, (ck)))
    ik = ",".join(map(str, (ik)))
    ak = ",".join(map(str, (ak)))
    print(rautn)
    print(rxres)
    print(ck)
    print(ik)
    print(ak)
    reply = (rautn) + " " + (rxres) + " " + (ck) + " " + (ik) + " " + (ak)
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
