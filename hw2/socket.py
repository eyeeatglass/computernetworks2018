import socket
s = socket.socket()
address = '127.0.0.1'
port = 80  
try:
    s.connect((address, port)) 
    s.send()


except Exception as e: 
    print("something's wrong with %s:%d. Exception is %s" % (address, port, e))
finally:
    s.close()