# Echo server program
import socket

HOST = ''                 
PORT = 50007
f = open("recievedData.ogv",'wb')              
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    while True:
        with conn:
            print('Connected by', addr)
            print("recieving...")
            data = conn.recv(1024)
            while(data):
                print("Recieving...")
                data = conn.recv(1024)
        
            conn.sendall(data)
            f.close()
            print("Done Recieving")
            conn.send("File Recieved!")
            conn.close()

        