# Echo client program
import socket

HOST = '192.168.21.107'    # The remote host
PORT = 50007              # The same port as used by the server
f=open("data.ogv",'rb')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("sending...")
    l = f.read(1024)
    while(l):
        print("sending...")
        s.send(l)
        l = f.read(1024)

    f.close()
    print("Done Sending!")
    print('Received', repr(l))